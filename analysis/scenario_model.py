"""
Scenario engine for the Iran/US conflict energy-shock impact on Japan and China.

Design notes
------------
The model is deliberately transparent rather than clever. Every channel is an
explicit, inspectable arithmetic step, because the point of the exercise is to
let an analyst argue with the assumptions, not to hide them behind a black box.

Four channels are modelled:

1. Terms-of-trade / income transfer.  A price rise on net energy imports is a
   transfer of real income abroad.  This is the dominant, most reliable channel
   for Japan, which is a near-total net importer.
       transfer_pct_gdp = (dPrice * net_import_volume * 365) / nominal_gdp

2. Price-induced demand response.  Higher prices destroy some demand
   voluntarily, via a short-run price elasticity.  Subsidies and price caps
   suppress this channel — which is the policy trap the report highlights.

3. Physical supply constraint.  If imports + reserve draw + substitution fall
   short of demand, the residual must be rationed away regardless of price.
   This is *involuntary* demand destruction and carries a much higher GDP cost
   per barrel than the price channel, because it hits output directly instead
   of transferring income.

4. Reserve runway.  Usable stocks divided by the shortfall rate, subject to a
   maximum physical deliverability constraint.

All elasticities and baselines are loaded from parameters.json so that the
provenance of every number is auditable and the web app can use the identical
figures.  No parameter is hard-coded in this file.

Units are stated in every field name.  Barrels are US barrels; mb/d is million
barrels per day; kb/d is thousand barrels per day.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional

HERE = os.path.dirname(os.path.abspath(__file__))
PARAM_PATH = os.path.join(HERE, "parameters.json")


# ---------------------------------------------------------------------------
# Parameter loading
# ---------------------------------------------------------------------------

def load_parameters(path: str = PARAM_PATH) -> dict:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


# ---------------------------------------------------------------------------
# Scenario definition
# ---------------------------------------------------------------------------

@dataclass
class Scenario:
    """A forward path for the shock.

    hormuz_throughput_pct: transit as % of pre-war normal (0-100).
    duration_months: how long this state persists from the as-of date.
    brent_usd_bbl: sustained Brent level under this scenario.
    jkm_usd_mmbtu: sustained JKM LNG level.
    naphtha_usd_t / lpg_usd_t: product prices, which drive the petrochemical
        and residential channels that crude alone misses.
    policy_offset_active: whether fuel subsidies / price caps remain in force.
        This is the key policy switch: when True the price-elasticity channel is
        damped by `subsidy_passthrough_block`, so less demand is destroyed
        voluntarily and reserves drain faster.
    """

    key: str
    label: str
    description: str
    hormuz_throughput_pct: float
    duration_months: float
    brent_usd_bbl: float
    jkm_usd_mmbtu: float
    naphtha_usd_t: float
    lpg_usd_t: float
    policy_offset_active: bool
    probability_pct: Optional[float] = None


@dataclass
class CountryResult:
    country: str
    scenario: str

    # channel 1
    net_oil_import_mbd: float
    oil_price_delta_usd: float
    oil_tot_transfer_pct_gdp: float
    lng_tot_transfer_pct_gdp: float
    total_tot_transfer_pct_gdp: float

    # channel 2 + 3
    supply_shortfall_kbd: float
    reserve_draw_kbd: float
    substitution_kbd: float
    voluntary_demand_destruction_kbd: float
    involuntary_demand_destruction_kbd: float
    total_demand_destruction_kbd: float
    demand_destruction_pct_of_demand: float

    # channel 4
    usable_reserve_mnbbl: float
    runway_weeks: Optional[float]
    runway_binding_constraint: str

    # macro outturn
    gdp_impact_pp: float
    gdp_impact_breakdown: Dict[str, float]
    cpi_impact_pp: float
    cpi_impact_breakdown: Dict[str, float]
    notes: List[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Core computation
# ---------------------------------------------------------------------------

def _safe(d: dict, *keys, default=0.0):
    """Fetch a nested key, returning `default` when absent or null.

    Missing data is treated as zero contribution rather than an exception, so a
    partially-populated parameter file still yields a usable (if conservative)
    result.  Every such fallback is recorded in the result notes.
    """
    cur = d
    for k in keys:
        if not isinstance(cur, dict) or k not in cur or cur[k] is None:
            return default
        cur = cur[k]
    return cur


def run_country(params: dict, country: str, sc: Scenario) -> CountryResult:
    c = params["countries"][country]
    notes: List[str] = []

    gdp_usd_bn = c["macro"]["nominal_gdp_usd_bn"]
    base_brent = params["baseline"]["brent_usd_bbl"]
    base_jkm = params["baseline"]["jkm_usd_mmbtu"]

    # ---- Channel 3 first: the physical balance -------------------------
    # The physical channels run before the terms-of-trade calculation because
    # a country does not pay the elevated import price on barrels it never
    # receives. Pricing the full pre-war import volume while Channel 3
    # separately charges a GDP penalty for the rationed share of that same
    # volume would bill the missing barrels twice.
    net_oil_import_mbd = c["energy"]["net_oil_import_mbd"]
    d_oil = sc.brent_usd_bbl - base_brent
    oil_demand_kbd = c["energy"]["oil_demand_kbd"]
    hormuz_dependent_kbd = c["energy"]["oil_imports_via_hormuz_kbd"]

    # Throughput loss applies only to the Hormuz-dependent slice.
    lost_kbd = hormuz_dependent_kbd * (1.0 - sc.hormuz_throughput_pct / 100.0)

    # Substitution: non-Hormuz sources that can realistically scale, capped by
    # the country's assessed incremental sourcing capacity.
    sub_cap = c["mitigation"]["max_substitution_kbd"]
    substitution_kbd = min(lost_kbd, sub_cap)

    # ---- Channel 2: voluntary (price-induced) demand response ----------
    # Computed BEFORE the reserve draw, because demand that is never exercised
    # never has to be supplied.  This ordering is what makes price support
    # costly in physical terms: by blocking the retail price signal it keeps
    # demand on the system, widening the gap that reserves must cover and so
    # shortening the runway.
    elas = c["elasticities"]["oil_demand_price_elasticity_short_run"]
    pct_price_change = (d_oil / base_brent) if base_brent else 0.0
    voluntary_pct = elas * pct_price_change  # elasticity is negative
    if sc.policy_offset_active:
        block = c["policy"]["subsidy_passthrough_block"]
        voluntary_pct *= (1.0 - block)
        notes.append(
            f"Subsidy/price-cap active: voluntary demand response damped by "
            f"{block*100:.0f}% (retail price signal suppressed), which widens "
            f"the physical gap and shortens the reserve runway."
        )
    voluntary_dd_kbd = min(
        oil_demand_kbd, max(0.0, -voluntary_pct * oil_demand_kbd)
    )

    # ---- Channel 3: what is left for reserves and rationing to cover ----
    gap_kbd = max(0.0, lost_kbd - substitution_kbd - voluntary_dd_kbd)

    # Reserve draw: bounded both by policy willingness and by physical
    # deliverability.  Deliverability is the constraint people forget.
    draw_cap = min(
        c["reserves"]["max_deliverable_draw_kbd"],
        c["reserves"]["policy_max_draw_kbd"],
    )
    reserve_draw_kbd = min(gap_kbd, draw_cap)

    shortfall_kbd = max(0.0, gap_kbd - reserve_draw_kbd)

    # Whatever reserves cannot cover must be rationed away.
    involuntary_dd_kbd = shortfall_kbd
    total_dd_kbd = voluntary_dd_kbd + involuntary_dd_kbd

    # ---- Channel 1: terms of trade, on delivered volume only ------------
    # Net the import bill down by the barrels that never arrive, so the
    # rationed shortfall is charged once (as lost output in the GDP
    # calculation below) rather than twice.
    delivered_import_mbd = max(
        0.0, net_oil_import_mbd - involuntary_dd_kbd / 1000.0
    )
    # mb/d * $/bbl * 365 days = $mn/yr  ->  /1000 = $bn/yr
    oil_transfer_bn = delivered_import_mbd * d_oil * 365 / 1000.0
    oil_tot_pct = oil_transfer_bn / gdp_usd_bn * 100.0

    lng_import_mt = c["energy"]["lng_import_mt_yr"]
    d_jkm = sc.jkm_usd_mmbtu - base_jkm
    # 1 tonne LNG ~ 52 mmbtu (industry convention, stated in parameters.json).
    # Note: LNG appears ONLY here. The model has no LNG physical balance, so
    # the LNG and naphtha constraints the report identifies as actually
    # binding are not represented in the runway or rationing channels.
    mmbtu_per_t = params["conversions"]["mmbtu_per_tonne_lng"]
    lng_transfer_bn = lng_import_mt * 1e6 * mmbtu_per_t * d_jkm / 1e9
    lng_tot_pct = lng_transfer_bn / gdp_usd_bn * 100.0

    total_tot_pct = oil_tot_pct + lng_tot_pct
    dd_pct = total_dd_kbd / oil_demand_kbd * 100.0 if oil_demand_kbd else 0.0

    # ---- Channel 4: runway ---------------------------------------------
    usable = c["reserves"]["usable_stock_mnbbl"]
    if reserve_draw_kbd > 0:
        runway_weeks = usable * 1000.0 / reserve_draw_kbd / 7.0
        if reserve_draw_kbd >= c["reserves"]["max_deliverable_draw_kbd"] - 1e-9:
            binding = "deliverability"
        elif reserve_draw_kbd >= c["reserves"]["policy_max_draw_kbd"] - 1e-9:
            binding = "policy"
        else:
            binding = "shortfall"
    else:
        runway_weeks = None
        binding = "no draw required"

    # ---- Macro outturn --------------------------------------------------
    # GDP: income-transfer channel scaled by a fiscal-style multiplier, plus a
    # much costlier involuntary-rationing channel.  Rationing destroys output
    # rather than merely transferring purchasing power, hence the separate and
    # larger coefficient.
    tot_mult = c["elasticities"]["tot_transfer_to_gdp_multiplier"]
    gdp_from_tot = -total_tot_pct * tot_mult

    ration_cost = c["elasticities"]["gdp_pp_per_pct_involuntary_demand_cut"]
    involuntary_pct_demand = (
        involuntary_dd_kbd / oil_demand_kbd * 100.0 if oil_demand_kbd else 0.0
    )
    gdp_from_rationing = -involuntary_pct_demand * ration_cost

    # Policy support partially offsets the GDP hit while it lasts.
    gdp_from_policy = (
        c["policy"]["gdp_support_pp"] if sc.policy_offset_active else 0.0
    )

    gdp_impact = gdp_from_tot + gdp_from_rationing + gdp_from_policy

    # CPI: direct energy basket effect plus indirect pass-through via naphtha
    # (packaging, plastics, processed goods) and utilities, net of subsidy.
    energy_weight = c["cpi"]["energy_weight_pct"] / 100.0
    retail_passthrough = c["cpi"]["retail_energy_passthrough"]
    cpi_direct = energy_weight * pct_price_change * 100.0 * retail_passthrough

    naph_base = params["baseline"]["naphtha_usd_t"]
    naph_change = (sc.naphtha_usd_t - naph_base) / naph_base if naph_base else 0.0
    cpi_indirect = naph_change * 100.0 * c["cpi"]["naphtha_to_cpi_beta"]

    cpi_subsidy = (
        -c["policy"]["cpi_suppression_pp"] if sc.policy_offset_active else 0.0
    )
    cpi_impact = cpi_direct + cpi_indirect + cpi_subsidy

    return CountryResult(
        country=country,
        scenario=sc.key,
        net_oil_import_mbd=net_oil_import_mbd,
        oil_price_delta_usd=d_oil,
        oil_tot_transfer_pct_gdp=round(oil_tot_pct, 3),
        lng_tot_transfer_pct_gdp=round(lng_tot_pct, 3),
        total_tot_transfer_pct_gdp=round(total_tot_pct, 3),
        supply_shortfall_kbd=round(shortfall_kbd, 1),
        reserve_draw_kbd=round(reserve_draw_kbd, 1),
        substitution_kbd=round(substitution_kbd, 1),
        voluntary_demand_destruction_kbd=round(voluntary_dd_kbd, 1),
        involuntary_demand_destruction_kbd=round(involuntary_dd_kbd, 1),
        total_demand_destruction_kbd=round(total_dd_kbd, 1),
        demand_destruction_pct_of_demand=round(dd_pct, 2),
        usable_reserve_mnbbl=usable,
        runway_weeks=round(runway_weeks, 1) if runway_weeks is not None else None,
        runway_binding_constraint=binding,
        gdp_impact_pp=round(gdp_impact, 2),
        gdp_impact_breakdown={
            "terms_of_trade": round(gdp_from_tot, 2),
            "involuntary_rationing": round(gdp_from_rationing, 2),
            "policy_support": round(gdp_from_policy, 2),
        },
        cpi_impact_pp=round(cpi_impact, 2),
        cpi_impact_breakdown={
            "direct_energy": round(cpi_direct, 2),
            "indirect_naphtha": round(cpi_indirect, 2),
            "subsidy_offset": round(cpi_subsidy, 2),
        },
        notes=notes,
    )


def load_scenarios(params: dict) -> List[Scenario]:
    return [Scenario(**s) for s in params["scenarios"]]


def run_all(params: Optional[dict] = None) -> dict:
    params = params or load_parameters()
    scenarios = load_scenarios(params)
    out = {
        "as_of": params["as_of"],
        "baseline": params["baseline"],
        "scenarios": [asdict(s) for s in scenarios],
        "results": [],
    }
    for sc in scenarios:
        for country in params["countries"]:
            out["results"].append(asdict(run_country(params, country, sc)))
    return out


def sensitivity(
    params: Optional[dict] = None,
    country: str = "JP",
    brent_grid: Optional[List[float]] = None,
    throughput_grid: Optional[List[float]] = None,
) -> List[dict]:
    """Two-way grid over Brent and Hormuz throughput.

    Produces the surface the web app renders as a heatmap: the interaction
    between price and physical availability is the whole story of this shock,
    and a one-way sensitivity would miss it.
    """
    params = params or load_parameters()
    brent_grid = brent_grid or [70, 85, 100, 115, 130, 150, 180]
    throughput_grid = throughput_grid or [0, 10, 25, 50, 75, 100]
    base_sc = load_scenarios(params)[1]  # the central/base scenario

    rows = []
    for b in brent_grid:
        for t in throughput_grid:
            sc = Scenario(
                key=f"grid_b{b}_t{t}",
                label=f"Brent {b} / throughput {t}%",
                description="sensitivity grid point",
                hormuz_throughput_pct=t,
                duration_months=base_sc.duration_months,
                brent_usd_bbl=b,
                # Scale gas and product prices off crude using the elasticities
                # in parameters.json rather than holding them fixed, since they
                # co-move strongly in a chokepoint event.
                jkm_usd_mmbtu=params["baseline"]["jkm_usd_mmbtu"]
                * (1 + (b / params["baseline"]["brent_usd_bbl"] - 1)
                   * params["cross_price"]["jkm_beta_to_brent"]),
                naphtha_usd_t=params["baseline"]["naphtha_usd_t"]
                * (1 + (b / params["baseline"]["brent_usd_bbl"] - 1)
                   * params["cross_price"]["naphtha_beta_to_brent"]),
                lpg_usd_t=params["baseline"]["lpg_usd_t"]
                * (1 + (b / params["baseline"]["brent_usd_bbl"] - 1)
                   * params["cross_price"]["lpg_beta_to_brent"]),
                policy_offset_active=base_sc.policy_offset_active,
            )
            r = run_country(params, country, sc)
            rows.append({
                "country": country,
                "brent": b,
                "throughput_pct": t,
                "gdp_impact_pp": r.gdp_impact_pp,
                "cpi_impact_pp": r.cpi_impact_pp,
                "runway_weeks": r.runway_weeks,
                "involuntary_dd_kbd": r.involuntary_demand_destruction_kbd,
            })
    return rows


def policy_switch_comparison(params: Optional[dict] = None) -> List[dict]:
    """Isolate the effect of keeping vs withdrawing price support.

    Run each scenario twice, flipping only `policy_offset_active`, to make the
    subsidy trade-off legible: support buys lower CPI and higher GDP today at
    the cost of faster reserve depletion and a larger involuntary cut later.
    """
    params = params or load_parameters()
    rows = []
    for sc in load_scenarios(params):
        for country in params["countries"]:
            for active in (True, False):
                variant = Scenario(**{**asdict(sc), "policy_offset_active": active})
                r = run_country(params, country, variant)
                rows.append({
                    "scenario": sc.key,
                    "country": country,
                    "policy_active": active,
                    "gdp_impact_pp": r.gdp_impact_pp,
                    "cpi_impact_pp": r.cpi_impact_pp,
                    "runway_weeks": r.runway_weeks,
                    "voluntary_dd_kbd": r.voluntary_demand_destruction_kbd,
                    "involuntary_dd_kbd": r.involuntary_demand_destruction_kbd,
                })
    return rows


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", help="write full results JSON here")
    args = ap.parse_args()

    params = load_parameters()
    res = run_all(params)
    res["sensitivity"] = {
        "JP": sensitivity(params, "JP"),
        "CN": sensitivity(params, "CN"),
    }
    res["policy_switch"] = policy_switch_comparison(params)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            json.dump(res, fh, indent=2)
        print(f"wrote {args.out}")
    else:
        for r in res["results"]:
            print(
                f"{r['scenario']:<28} {r['country']}  "
                f"GDP {r['gdp_impact_pp']:+.2f}pp  "
                f"CPI {r['cpi_impact_pp']:+.2f}pp  "
                f"runway {r['runway_weeks']}w  "
                f"involDD {r['involuntary_demand_destruction_kbd']:.0f}kb/d"
            )
