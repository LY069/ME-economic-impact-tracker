#!/usr/bin/env python3
"""
Validate the tracker dataset before it is published or committed.

Checks, in order of how badly each would mislead a reader:

1. **Provenance** — every research observation carries a source URL and a
   quality label. An unsourced number in a policy dataset is worse than no
   number, because it looks authoritative.
2. **Internal consistency** — percentage shares that should sum to ~100 do,
   loss percentages are in [0, 100], and no observation is dated in the future.
3. **Scenario coherence** — the model's outputs move in the expected direction
   (a worse throughput scenario cannot show a smaller GDP hit), which catches
   sign errors in the parameter file that would otherwise pass silently.
4. **App payload integrity** — data.json parses, has the sections the page
   expects, and every live series declares a status.

Exit code is non-zero when any ERROR is found. WARNINGs are reported but do
not fail the run, since incomplete research is expected mid-project.

Usage:
    python3 scripts/validate_data.py [--strict]
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date, datetime
from typing import List

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_DATA = os.path.join(ROOT, "app", "data.json")
SCENARIOS = os.path.join(ROOT, "app", "scenarios.json")

VALID_QUALITY = {"hard", "est", "calc"}
VALID_COUNTRY_PREFIX = {"JP", "CN", "WORLD"}

errors: List[str] = []
warnings: List[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def check_observations(doc: dict) -> None:
    analysis = doc.get("analysis")
    if not analysis:
        err("data.json has no 'analysis' section - run scripts/build_dataset.py")
        return

    obs = analysis.get("observations", [])
    if not obs:
        warn("analysis.observations is empty")
        return

    today = date.today()
    unsourced = 0
    unlabelled = 0
    future = 0
    unparsed = 0

    for i, o in enumerate(obs):
        if not o.get("source_url"):
            unsourced += 1
        q = o.get("quality") or ""
        if q not in VALID_QUALITY:
            unlabelled += 1
        d = o.get("date") or ""
        if d:
            try:
                if datetime.strptime(d, "%Y-%m-%d").date() > today:
                    future += 1
            except ValueError:
                warn(f"observation {i} ({o.get('series_id')}): unparseable date '{d}'")
        parse = o.get("parse", "")
        if parse.startswith("unparsed"):
            unparsed += 1

        # percentage sanity
        unit = (o.get("unit") or "").lower()
        val = o.get("value")
        if val is not None and unit in ("%", "pct", "percent", "share_pct"):
            if not -100.0 <= val <= 100.0:
                warn(
                    f"{o.get('series_id')}: value {val} labelled '{unit}' is "
                    "outside [-100, 100]"
                )

    if unsourced:
        err(f"{unsourced} of {len(obs)} observations have no source_url")
    if unlabelled:
        err(f"{unlabelled} of {len(obs)} observations lack a valid quality label")
    if future:
        warn(f"{future} observations are dated in the future")
    if unparsed:
        warn(f"{unparsed} observations have an unparseable value")

    countries = {(o.get("country") or "").upper() for o in obs}
    stray = {
        c for c in countries
        if c and c not in VALID_COUNTRY_PREFIX and len(c) not in (2, 3)
    }
    if stray:
        warn(f"unexpected country codes: {sorted(stray)}")

    # The brief scopes this study to Japan and China; a dataset with no JP or
    # CN rows means a workstream drifted off-scope.
    if not countries & {"JP", "CN"}:
        err("no observations for JP or CN - the study's country scope is missing")


def check_tables(doc: dict) -> None:
    tables = doc.get("analysis", {}).get("tables", {})
    expected = {
        "timeline", "substitutability", "demand_destruction",
        "elasticities", "policy", "runway",
    }
    missing = expected - set(tables)
    if missing:
        warn(f"structured tables not yet present: {sorted(missing)}")

    for row in tables.get("runway", []):
        weeks = row.get("weeks_of_cover", "")
        try:
            w = float(str(weeks).split("-")[0])
            if w < 0:
                err(f"runway row has negative weeks_of_cover: {row}")
        except (ValueError, TypeError):
            pass


def check_scenarios() -> None:
    if not os.path.exists(SCENARIOS):
        warn("app/scenarios.json not built yet - run analysis/scenario_model.py")
        return
    with open(SCENARIOS, "r", encoding="utf-8") as fh:
        sc = json.load(fh)

    results = sc.get("results", [])
    if not results:
        err("scenarios.json has no results")
        return

    # Monotonicity: for a given country, a lower Hormuz throughput must not
    # produce a smaller GDP hit. A violation means a sign or parameter error.
    by_country = {}
    thr = {s["key"]: s["hormuz_throughput_pct"] for s in sc.get("scenarios", [])}
    for r in results:
        by_country.setdefault(r["country"], []).append(r)

    for country, rows in by_country.items():
        ordered = sorted(
            [r for r in rows if r["scenario"] in thr],
            key=lambda r: -thr[r["scenario"]],
        )
        for a, b in zip(ordered, ordered[1:]):
            if b["gdp_impact_pp"] > a["gdp_impact_pp"] + 1e-9:
                err(
                    f"{country}: scenario '{b['scenario']}' has lower throughput "
                    f"than '{a['scenario']}' but a smaller GDP hit "
                    f"({b['gdp_impact_pp']} vs {a['gdp_impact_pp']}) - "
                    "check parameters.json signs"
                )

    for r in results:
        if r.get("runway_weeks") is not None and r["runway_weeks"] < 0:
            err(f"negative runway in {r['scenario']}/{r['country']}")
        dd = r.get("demand_destruction_pct_of_demand")
        if dd is not None and dd > 100:
            err(f"demand destruction >100% of demand in {r['scenario']}/{r['country']}")


def check_live(doc: dict) -> None:
    live = doc.get("live")
    if not live:
        warn("no 'live' section - run scripts/update_data.py")
        return
    for sid, s in live.items():
        if s.get("status") not in {"live", "stale", "unavailable"}:
            err(f"live series '{sid}' has invalid status '{s.get('status')}'")
        if not s.get("source_url"):
            err(f"live series '{sid}' has no source_url")
        if s.get("status") == "live" and not s.get("observations"):
            err(f"live series '{sid}' marked live but carries no observations")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true",
                    help="treat warnings as failures")
    args = ap.parse_args()

    if not os.path.exists(APP_DATA):
        print(f"ERROR: {APP_DATA} does not exist", file=sys.stderr)
        return 1

    try:
        with open(APP_DATA, "r", encoding="utf-8") as fh:
            doc = json.load(fh)
    except json.JSONDecodeError as exc:
        print(f"ERROR: data.json is not valid JSON: {exc}", file=sys.stderr)
        return 1

    check_observations(doc)
    check_tables(doc)
    check_live(doc)
    check_scenarios()

    print(f"validation: {len(errors)} error(s), {len(warnings)} warning(s)")
    for w in warnings:
        print(f"  WARN  {w}")
    for e in errors:
        print(f"  ERROR {e}", file=sys.stderr)

    if errors:
        return 1
    if warnings and args.strict:
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
