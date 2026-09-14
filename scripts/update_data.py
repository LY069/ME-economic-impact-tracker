#!/usr/bin/env python3
"""
Live-data refresher for the Middle East economic impact tracker.

What this does
--------------
Pulls the market and macro series the dashboard tracks from public endpoints,
merges them into `app/data.json` alongside the research-derived analytical
dataset, and stamps each series with its source and retrieval time.

Why it is a separate script
---------------------------
The analytical dataset (supply-loss volumes, dependency ratios, reserve runway)
comes from sourced research and changes only when an analyst revises it.  The
market series (Brent, JKM proxy, FX) change daily.  Keeping the two apart means
a refresh can never silently overwrite a researched figure with a scraped one.

Egress note
-----------
Every provider below is a public, key-free or key-optional endpoint.  Some
sandboxed environments restrict outbound traffic to an allowlist, in which case
this script degrades gracefully: it keeps the previous values, marks the series
`stale`, and exits 0 so a scheduled run never fails the build.  Run it locally
or in CI (GitHub Actions has open egress) for genuine live tracking.

Usage
-----
    python3 scripts/update_data.py                # refresh in place
    python3 scripts/update_data.py --dry-run      # fetch and report, write nothing
    python3 scripts/update_data.py --require-live # exit 1 if nothing could be fetched
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from typing import Callable, Dict, List, Optional

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_JSON = os.path.join(ROOT, "app", "data.json")
TIMEOUT = 30
UA = "Mozilla/5.0 (compatible; ME-impact-tracker/1.0; +https://github.com/)"


def _get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.read()


# ---------------------------------------------------------------------------
# Providers.  Each returns a list of {date, value} dicts, oldest first.
# ---------------------------------------------------------------------------

def stooq(symbol: str) -> List[Dict]:
    """Stooq daily CSV — key-free. Symbols: cb.f Brent, cl.f WTI, ng.f HH gas."""
    raw = _get(f"https://stooq.com/q/d/l/?s={symbol}&i=d").decode("utf-8", "replace")
    rows = list(csv.DictReader(io.StringIO(raw)))
    out = []
    for r in rows:
        try:
            out.append({"date": r["Date"], "value": float(r["Close"])})
        except (KeyError, ValueError):
            continue
    return out[-900:]


def fred(series_id: str, api_key: Optional[str]) -> List[Dict]:
    """FRED — needs a free API key in FRED_API_KEY. Skipped when absent."""
    if not api_key:
        raise RuntimeError("FRED_API_KEY not set")
    url = (
        f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}"
        f"&api_key={api_key}&file_type=json&observation_start=2024-01-01"
    )
    js = json.loads(_get(url))
    return [
        {"date": o["date"], "value": float(o["value"])}
        for o in js.get("observations", [])
        if o.get("value") not in (".", "", None)
    ]


def eia(series_path: str, api_key: Optional[str]) -> List[Dict]:
    """EIA v2 — needs a free API key in EIA_API_KEY. Skipped when absent."""
    if not api_key:
        raise RuntimeError("EIA_API_KEY not set")
    url = (
        f"https://api.eia.gov/v2/{series_path}&api_key={api_key}"
        "&sort[0][column]=period&sort[0][direction]=desc&length=500"
    )
    js = json.loads(_get(url))
    rows = js.get("response", {}).get("data", [])
    out = []
    for r in rows:
        try:
            out.append({"date": r["period"], "value": float(r["value"])})
        except (KeyError, TypeError, ValueError):
            continue
    return sorted(out, key=lambda x: x["date"])


def worldbank(country: str, indicator: str) -> List[Dict]:
    url = (
        f"https://api.worldbank.org/v2/country/{country}/indicator/{indicator}"
        "?format=json&per_page=100&date=2015:2026"
    )
    js = json.loads(_get(url))
    if not isinstance(js, list) or len(js) < 2 or js[1] is None:
        raise RuntimeError("unexpected World Bank payload")
    return sorted(
        [
            {"date": f"{o['date']}-12-31", "value": float(o["value"])}
            for o in js[1]
            if o.get("value") is not None
        ],
        key=lambda x: x["date"],
    )


# ---------------------------------------------------------------------------
# Series registry: what the dashboard tracks live.
# ---------------------------------------------------------------------------

def build_registry() -> List[Dict]:
    fred_key = os.environ.get("FRED_API_KEY")
    eia_key = os.environ.get("EIA_API_KEY")

    return [
        {
            "id": "brent_usd_bbl",
            "label": "Brent crude",
            "unit": "USD/bbl",
            "source": "Stooq (cb.f front-month)",
            "source_url": "https://stooq.com/q/?s=cb.f",
            "fetch": lambda: stooq("cb.f"),
        },
        {
            "id": "wti_usd_bbl",
            "label": "WTI crude",
            "unit": "USD/bbl",
            "source": "Stooq (cl.f front-month)",
            "source_url": "https://stooq.com/q/?s=cl.f",
            "fetch": lambda: stooq("cl.f"),
        },
        {
            "id": "henry_hub_usd_mmbtu",
            "label": "Henry Hub natural gas",
            "unit": "USD/mmbtu",
            "source": "Stooq (ng.f front-month)",
            "source_url": "https://stooq.com/q/?s=ng.f",
            "fetch": lambda: stooq("ng.f"),
        },
        {
            "id": "usdjpy",
            "label": "USD/JPY",
            "unit": "JPY per USD",
            "source": "Stooq",
            "source_url": "https://stooq.com/q/?s=usdjpy",
            "fetch": lambda: stooq("usdjpy"),
        },
        {
            "id": "usdcny",
            "label": "USD/CNY",
            "unit": "CNY per USD",
            "source": "Stooq",
            "source_url": "https://stooq.com/q/?s=usdcny",
            "fetch": lambda: stooq("usdcny"),
        },
        {
            "id": "jp_cpi_yoy",
            "label": "Japan CPI, all items, YoY",
            "unit": "% YoY",
            "source": "FRED (JPNCPIALLMINMEI-derived) — needs FRED_API_KEY",
            "source_url": "https://fred.stlouisfed.org/series/JPNCPIALLMINMEI",
            "fetch": lambda: fred("JPNCPIALLMINMEI", fred_key),
        },
        {
            "id": "brent_spot_eia",
            "label": "Brent spot (EIA official)",
            "unit": "USD/bbl",
            "source": "EIA v2 petroleum spot prices — needs EIA_API_KEY",
            "source_url": "https://www.eia.gov/opendata/",
            "fetch": lambda: eia(
                "petroleum/pri/spt/data/?frequency=daily&data[]=value"
                "&facets[series][]=RBRTE",
                eia_key,
            ),
        },
    ]


# ---------------------------------------------------------------------------
# Merge and write
# ---------------------------------------------------------------------------

def load_existing() -> dict:
    if os.path.exists(DATA_JSON):
        with open(DATA_JSON, "r", encoding="utf-8") as fh:
            return json.load(fh)
    return {}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--require-live", action="store_true",
                    help="exit non-zero if no series could be refreshed")
    args = ap.parse_args()

    doc = load_existing()
    live = doc.get("live", {})
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")

    ok, failed = [], []
    for spec in build_registry():
        sid = spec["id"]
        try:
            obs = spec["fetch"]()
            if not obs:
                raise RuntimeError("empty series")
            live[sid] = {
                "label": spec["label"],
                "unit": spec["unit"],
                "source": spec["source"],
                "source_url": spec["source_url"],
                "observations": obs,
                "latest": obs[-1],
                "status": "live",
                "retrieved_at": now,
            }
            ok.append(f"{sid} ({len(obs)} obs, latest {obs[-1]['date']} = {obs[-1]['value']})")
        except Exception as exc:  # noqa: BLE001 - report, never crash a scheduled run
            prev = live.get(sid)
            if prev:
                prev["status"] = "stale"
                prev["last_error"] = f"{type(exc).__name__}: {exc}"
                prev["last_attempt_at"] = now
            else:
                live[sid] = {
                    "label": spec["label"],
                    "unit": spec["unit"],
                    "source": spec["source"],
                    "source_url": spec["source_url"],
                    "observations": [],
                    "latest": None,
                    "status": "unavailable",
                    "last_error": f"{type(exc).__name__}: {exc}",
                    "last_attempt_at": now,
                }
            failed.append(f"{sid}: {type(exc).__name__}: {exc}")

    doc["live"] = live
    doc["live_refreshed_at"] = now
    doc["live_status"] = {
        "refreshed": len(ok),
        "failed": len(failed),
        "note": (
            "Series marked 'stale' or 'unavailable' could not be reached from the "
            "environment that ran this script. The analytical dataset is unaffected."
        ),
    }

    print(f"refreshed {len(ok)} series, {len(failed)} failed")
    for line in ok:
        print(f"  OK   {line}")
    for line in failed:
        print(f"  FAIL {line}")

    if args.dry_run:
        print("dry run - no file written")
        return 0

    os.makedirs(os.path.dirname(DATA_JSON), exist_ok=True)
    with open(DATA_JSON, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=2, ensure_ascii=False)
    print(f"wrote {DATA_JSON}")

    if args.require_live and not ok:
        print("ERROR: --require-live set and no series refreshed", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
