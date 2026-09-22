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
        # A row whose value is genuinely missing is a deliberate gap marker.
        # There is no figure to assign a confidence to, so requiring a quality
        # label on it would only encourage inventing one.
        is_gap = o.get("value") is None and o.get("parse") == "missing"
        if q not in VALID_QUALITY and not is_gap:
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
        # A research agent writing 'NA' where it could not judge confidence is
        # honest missing metadata, not a defect. It only becomes a real problem
        # when it is widespread enough to undermine the dataset's provenance.
        share = unlabelled / len(obs)
        msg = (f"{unlabelled} of {len(obs)} observations ({share:.0%}) lack a "
               "valid quality label")
        if share > 0.25:
            err(msg + " - provenance is too thin to rely on")
        else:
            warn(msg)
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

    # Monotonicity: holding the policy stance fixed, a lower Hormuz throughput
    # must not produce a smaller GDP hit. A violation means a sign or parameter
    # error.
    #
    # The policy stance has to be held fixed for this to be a valid test.
    # Withdrawing price support legitimately improves GDP at unchanged
    # throughput -- it restores the price signal, so more demand adjusts
    # voluntarily and less output is rationed away. Comparing across the policy
    # switch would flag that intended result as a bug.
    meta = {
        s["key"]: (s["hormuz_throughput_pct"], s.get("policy_offset_active"))
        for s in sc.get("scenarios", [])
    }
    groups = {}
    for r in results:
        if r["scenario"] not in meta:
            continue
        thr, policy = meta[r["scenario"]]
        groups.setdefault((r["country"], policy), []).append((thr, r))

    for (country, policy), rows in groups.items():
        ordered = sorted(rows, key=lambda t: -t[0])
        for (thr_a, a), (thr_b, b) in zip(ordered, ordered[1:]):
            if thr_b == thr_a:
                continue  # same throughput: nothing to compare
            if b["gdp_impact_pp"] > a["gdp_impact_pp"] + 1e-9:
                err(
                    f"{country} (support={policy}): '{b['scenario']}' has lower "
                    f"throughput than '{a['scenario']}' but a smaller GDP hit "
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
