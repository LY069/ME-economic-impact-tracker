#!/usr/bin/env python3
"""
Consolidate the research CSVs in data/raw/ into a curated dataset and the
app payload.

Two kinds of input
------------------
1. **Long-format observation files** with the canonical columns
   `series_id,country,product,metric,unit,date,value,quality,source_url,note`.
   These are concatenated into one tidy master table, which is the file an
   analyst should cite.
2. **Structured tables** (timeline, substitutability, policy inventory, runway,
   demand-destruction log, elasticities) whose natural shape is not one
   observation per row. These are passed through as named tables, schema
   checked but not forced into the long format.

Everything is emitted to `app/data.json` under `analysis`, so the dashboard and
the Python model read from exactly one source of truth.

Usage:
    python3 scripts/build_dataset.py [--strict]

`--strict` turns schema warnings into a non-zero exit, for CI.
"""

from __future__ import annotations

import argparse
import csv
import glob
import json
import os
import sys
from collections import defaultdict
from datetime import datetime, timezone
from typing import Dict, List

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "data", "raw")
CURATED = os.path.join(ROOT, "data", "curated")
APP_DATA = os.path.join(ROOT, "app", "data.json")

LONG_COLUMNS = [
    "series_id", "country", "product", "metric", "unit",
    "date", "value", "quality", "source_url", "note",
]

# Files whose shape is intentionally not the long format.
STRUCTURED = {
    "ws1_timeline": "timeline",
    "ws2_substitutability": "substitutability",
    "ws3_demand_destruction": "demand_destruction",
    "ws3_elasticities": "elasticities",
    "ws4_policy": "policy",
    "ws5_runway": "runway",
}

VALID_QUALITY = {"hard", "est", "calc"}


def read_csv(path: str) -> List[Dict[str, str]]:
    """Read a research CSV, tolerating unquoted commas in the final column.

    The `note` column is free text and research agents routinely leave commas
    in it unquoted, which makes the row wider than the header. csv.DictReader
    parks the overflow under a None key. Those extras are always the tail of
    the last column, so rejoining them with commas recovers the original text
    instead of discarding the row.
    """
    out: List[Dict[str, str]] = []
    with open(path, "r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fields = reader.fieldnames or []
        last = fields[-1] if fields else None
        for row in reader:
            extras = row.pop(None, None)
            clean = {
                (k or "").strip(): ("" if v is None else str(v)).strip()
                for k, v in row.items()
            }
            if extras and last:
                tail = ",".join(str(e) for e in extras if e is not None)
                clean[last] = (clean.get(last, "") + "," + tail).strip(",").strip()
            out.append(clean)
    return out


def normalise_date(value: str) -> str:
    """Accept the date spellings the research agents plausibly produce.

    Monthly data given as 2026-08 becomes month-end; a bare year becomes
    year-end. Anything unparseable is returned untouched and flagged upstream.
    """
    v = value.strip()
    if not v:
        return ""
    for fmt, transform in (
        ("%Y-%m-%d", lambda d: d.strftime("%Y-%m-%d")),
        ("%Y/%m/%d", lambda d: d.strftime("%Y-%m-%d")),
        ("%Y-%m", lambda d: _month_end(d)),
        ("%Y", lambda d: d.replace(month=12, day=31).strftime("%Y-%m-%d")),
    ):
        try:
            return transform(datetime.strptime(v, fmt))
        except ValueError:
            continue
    return v


def _month_end(d: datetime) -> str:
    if d.month == 12:
        nxt = d.replace(year=d.year + 1, month=1, day=1)
    else:
        nxt = d.replace(month=d.month + 1, day=1)
    return (nxt - (nxt - d).__class__(days=1)).strftime("%Y-%m-%d")


def parse_number(value: str):
    """Return a float where possible, else None.

    Research CSVs carry 'NA', '~', ranges like '1.2-1.5', and stray units. A
    range is collapsed to its midpoint and recorded as such by the caller; the
    alternative -- dropping it -- loses real information.
    """
    v = value.strip().replace(",", "").replace("%", "")
    if v in ("", "NA", "n/a", "N/A", "-", "--", "null", "None"):
        return None, "missing"
    try:
        return float(v), "exact"
    except ValueError:
        pass
    # range midpoint, e.g. "1.2-1.5" or "1.2 to 1.5"
    for sep in ("-", "to", "~"):
        parts = [p.strip() for p in v.replace(" to ", "-").split("-") if p.strip()]
        if sep and len(parts) == 2:
            try:
                lo, hi = float(parts[0]), float(parts[1])
                return (lo + hi) / 2.0, f"range_midpoint[{lo},{hi}]"
            except ValueError:
                break
    return None, f"unparsed[{value.strip()}]"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    os.makedirs(CURATED, exist_ok=True)
    warnings: List[str] = []
    long_rows: List[Dict] = []
    structured: Dict[str, List[Dict]] = defaultdict(list)

    files = sorted(glob.glob(os.path.join(RAW, "*.csv")))
    if not files:
        print(f"No CSVs found in {RAW}", file=sys.stderr)
        return 1

    for path in files:
        stem = os.path.splitext(os.path.basename(path))[0]
        rows = read_csv(path)
        if not rows:
            warnings.append(f"{stem}: file is empty")
            continue

        table = STRUCTURED.get(stem)
        if table:
            for r in rows:
                r["_source_file"] = stem
                q = r.get("quality", "")
                if q and q not in VALID_QUALITY:
                    warnings.append(
                        f"{stem}: quality '{q}' not in {sorted(VALID_QUALITY)}"
                    )
            structured[table].extend(rows)
            print(f"  structured  {stem}: {len(rows)} rows -> {table}")
            continue

        missing = [c for c in LONG_COLUMNS if c not in rows[0]]
        if missing:
            warnings.append(
                f"{stem}: not long-format (missing {missing}); "
                "passed through as table '{stem}'"
            )
            for r in rows:
                r["_source_file"] = stem
            structured[stem].extend(rows)
            print(f"  passthrough {stem}: {len(rows)} rows")
            continue

        kept = 0
        for i, r in enumerate(rows, start=2):
            value, how = parse_number(r.get("value", ""))
            date = normalise_date(r.get("date", ""))
            q = r.get("quality", "")
            if q and q not in VALID_QUALITY:
                warnings.append(f"{stem} line {i}: quality '{q}' invalid")
            if not r.get("source_url"):
                warnings.append(f"{stem} line {i}: missing source_url")
            if value is None and how != "missing":
                warnings.append(f"{stem} line {i}: value {how}")
            long_rows.append({
                "series_id": r.get("series_id", ""),
                "country": r.get("country", ""),
                "product": r.get("product", ""),
                "metric": r.get("metric", ""),
                "unit": r.get("unit", ""),
                "date": date,
                "value": value,
                "value_raw": r.get("value", ""),
                "parse": how,
                "quality": q,
                "source_url": r.get("source_url", ""),
                "note": r.get("note", ""),
                "_source_file": stem,
            })
            kept += 1
        print(f"  long        {stem}: {kept} observations")

    # ---- write curated master table ------------------------------------
    master = os.path.join(CURATED, "master_observations.csv")
    cols = [
        "series_id", "country", "product", "metric", "unit", "date",
        "value", "value_raw", "parse", "quality", "source_url", "note",
        "_source_file",
    ]
    with open(master, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(long_rows)
    print(f"\nwrote {master} ({len(long_rows)} observations)")

    for table, rows in structured.items():
        out = os.path.join(CURATED, f"{table}.csv")
        keys: List[str] = []
        for r in rows:
            for k in r:
                if k not in keys:
                    keys.append(k)
        with open(out, "w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=keys, extrasaction="ignore")
            w.writeheader()
            w.writerows(rows)
        print(f"wrote {out} ({len(rows)} rows)")

    # ---- merge into the app payload ------------------------------------
    doc = {}
    if os.path.exists(APP_DATA):
        with open(APP_DATA, "r", encoding="utf-8") as fh:
            doc = json.load(fh)

    by_quality: Dict[str, int] = defaultdict(int)
    for r in long_rows:
        by_quality[r["quality"] or "unlabelled"] += 1

    # The dashboard runs a JS port of the scenario model, so it needs the same
    # parameter file the Python model reads. Embedding it here is what keeps
    # the two implementations from drifting apart.
    param_path = os.path.join(ROOT, "analysis", "parameters.json")
    if os.path.exists(param_path):
        with open(param_path, "r", encoding="utf-8") as fh:
            doc["parameters"] = json.load(fh)
        print(f"embedded {param_path}")
    else:
        warnings.append("analysis/parameters.json not found - the dashboard's "
                        "scenario explorer will be inert")

    doc["analysis"] = {
        "observations": long_rows,
        "tables": dict(structured),
        "built_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "counts": {
            "observations": len(long_rows),
            "by_quality": dict(by_quality),
            "tables": {k: len(v) for k, v in structured.items()},
        },
    }
    os.makedirs(os.path.dirname(APP_DATA), exist_ok=True)
    with open(APP_DATA, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=2, ensure_ascii=False)
    print(f"wrote {APP_DATA}")

    if warnings:
        print(f"\n{len(warnings)} warning(s):", file=sys.stderr)
        for w_ in warnings[:60]:
            print(f"  - {w_}", file=sys.stderr)
        if len(warnings) > 60:
            print(f"  ... and {len(warnings) - 60} more", file=sys.stderr)
        if args.strict:
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
