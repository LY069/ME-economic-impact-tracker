#!/usr/bin/env python3
"""
Repair research CSVs whose rows carry unquoted commas in free-text fields.

The research agents wrote several rows with bare commas inside `event`,
`measure`, `quantified_impact` and `note`, which makes those rows wider than
their header and silently shifts every column to the right of the break. The
data is all still there -- it just needs to be re-associated with the right
columns and written back with proper quoting.

Rather than guess where the break fell, each table is realigned against an
anchor that cannot be confused with free text:

* **ws1_timeline** -- the `products` column draws on a closed vocabulary
  (crude, LNG, naphtha, urea, ...), so the first middle field whose
  semicolon-separated tokens are all known product names marks the boundary.
  Everything before it is `event`, everything after is `quantified_impact`.
* **ws4_policy** -- `announce_date` is an ISO date at a known header index, so
  the offset between where a date actually appears and where it belongs gives
  the exact number of surplus fields, which are folded back into `measure`.
* **long-format files** -- `note` is the final column, so any overflow simply
  rejoins onto the end (handled in scripts/build_dataset.py at read time).

Rows that cannot be realigned confidently are left untouched and reported, so
nothing is silently mangled.

Usage:
    python3 scripts/repair_csvs.py [--dry-run]
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from typing import List

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "data", "raw")

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

PRODUCT_VOCAB = {
    "crude", "crude_oil", "condensate", "crude_and_condensate", "lng", "lpg",
    "naphtha", "gasoil", "diesel", "gasoline", "jet", "kerosene", "fuel_oil",
    "refined_products", "all_products", "methanol", "meg", "urea", "ammonia",
    "sulphur", "sulfur", "polyethylene", "polypropylene", "base_oils",
    "fertilizer", "petrochemicals", "aluminium", "aluminum", "natural_gas",
    "shipping_security", "all_vessels", "shipping", "power", "electricity",
    "coal", "uranium", "freight", "insurance",
}


def is_product_field(value: str) -> bool:
    v = value.strip()
    if not v or len(v) > 60:
        return False
    tokens = [t.strip().lower().replace(" ", "_") for t in v.split(";") if t.strip()]
    return bool(tokens) and all(t in PRODUCT_VOCAB for t in tokens)


def repair_timeline(rows: List[List[str]], header: List[str]) -> tuple:
    """date, event, products, quantified_impact, quality, source_url"""
    n = len(header)
    out, fixed, failed = [header], 0, []
    for lineno, r in enumerate(rows, 2):
        if len(r) == n:
            out.append(r)
            continue
        if len(r) < n:
            failed.append((lineno, "too few fields"))
            out.append(r)
            continue
        date, quality, url = r[0], r[-2], r[-1]
        middle = r[1:-2]
        idx = next((i for i, f in enumerate(middle) if is_product_field(f)), None)
        if idx is None:
            failed.append((lineno, "no product anchor found"))
            out.append(r)
            continue
        event = ",".join(middle[:idx]).strip()
        products = middle[idx].strip()
        impact = ",".join(middle[idx + 1:]).strip()
        out.append([date, event, products, impact, quality, url])
        fixed += 1
    return out, fixed, failed


def repair_policy(rows: List[List[str]], header: List[str]) -> tuple:
    """Fold surplus fields back into `measure`, located via the announce_date anchor."""
    n = len(header)
    try:
        date_idx = header.index("announce_date")
    except ValueError:
        return [header] + rows, 0, [(0, "no announce_date column")]

    out, fixed, failed = [header], 0, []
    for lineno, r in enumerate(rows, 2):
        if len(r) == n:
            out.append(r)
            continue
        if len(r) < n:
            failed.append((lineno, "too few fields"))
            out.append(r)
            continue
        actual = next((i for i, f in enumerate(r) if DATE_RE.match(f.strip())), None)
        if actual is None or actual < date_idx:
            failed.append((lineno, "no date anchor found"))
            out.append(r)
            continue
        surplus = actual - date_idx
        if len(r) - surplus != n:
            failed.append((lineno, f"anchor implies {surplus} surplus, width mismatch"))
            out.append(r)
            continue
        measure = ",".join(r[1:2 + surplus]).strip()
        out.append([r[0], measure] + r[2 + surplus:])
        fixed += 1
    return out, fixed, failed


def repair_long(rows: List[List[str]], header: List[str]) -> tuple:
    """Long format: `note` is last, so surplus rejoins onto it."""
    n = len(header)
    out, fixed, failed = [header], 0, []
    for lineno, r in enumerate(rows, 2):
        if len(r) == n:
            out.append(r)
            continue
        if len(r) < n:
            failed.append((lineno, "too few fields"))
            out.append(r)
            continue
        out.append(r[:n - 1] + [",".join(r[n - 1:]).strip()])
        fixed += 1
    return out, fixed, failed


HANDLERS = {
    "ws1_timeline.csv": repair_timeline,
    "ws4_policy.csv": repair_policy,
}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    total_fixed, total_failed = 0, 0
    for name in sorted(os.listdir(RAW)):
        if not name.endswith(".csv"):
            continue
        path = os.path.join(RAW, name)
        with open(path, encoding="utf-8-sig", newline="") as fh:
            rows = list(csv.reader(fh))
        if not rows:
            continue
        header, body = rows[0], rows[1:]
        if not any(len(r) != len(header) for r in body):
            continue

        handler = HANDLERS.get(name, repair_long)
        new_rows, fixed, failed = handler(body, header)
        total_fixed += fixed
        total_failed += len(failed)

        print(f"{name}: realigned {fixed} row(s)"
              + (f", {len(failed)} could not be repaired" if failed else ""))
        for lineno, why in failed:
            print(f"    line {lineno}: {why}", file=sys.stderr)

        if not args.dry_run:
            with open(path, "w", encoding="utf-8", newline="") as fh:
                csv.writer(fh, quoting=csv.QUOTE_MINIMAL).writerows(new_rows)

    if args.dry_run:
        print("dry run - nothing written")
    print(f"total: {total_fixed} repaired, {total_failed} unrepaired")
    return 1 if total_failed else 0


if __name__ == "__main__":
    sys.exit(main())
