# Independent review of the Hormuz shock / Japan-China impact study

Reviewer scope: internal consistency, methodology, and honesty, using only repository
contents (no web access). Every finding below was verified directly against the cited
file(s); where I ran code, the commands and outputs are described in "Checks performed."

## Verdict

The study is usable as a structured survey of a fast-moving, genuinely under-documented
event, and its discipline at the level of individual observations (quality tags, "NA"
instead of invented numbers, realised-vs-forecast separation) is real, not cosmetic. But it
is not sound enough to act on as presented, for one overriding reason: the report's central,
most-repeated claim — that Japan's reserve runway is "pinned" regardless of scenario severity
because physical **deliverability**, not stock size or policy, is the binding constraint —
is not a discovered fact about the world. It is a mechanical artifact of a single unsourced
number (`max_deliverable_draw_kbd = 900 kb/d`, tagged `assumption`, "not published" in
`analysis/parameters.json`). I ran the model directly: whenever the physical gap exceeds that
cap, the reserve draw is pinned at exactly 900 kb/d in every scenario, which makes
`runway_weeks = usable/draw/7 = 39.2` a near-tautology, not an economic finding. Change the
assumed cap and the "most operationally important" result in the report (Section 6) evaporates.
That the report says so explicitly in its Limitations section, while its own Section 6 prose
calls the same result "the most counter-intuitive output of the model and the most
operationally important," is the study's single biggest weakness: the confidence of the
narrative repeatedly outruns the evidentiary base it discloses, and in at least one place
(the claim that the tracker's parameter table tags every assumption — it doesn't; see Finding
3) the report makes a specific, checkable claim about its own deliverable that is false.

## Material findings

### 1. The headline "supply-constrained, not price-induced" balance is asserted more confidently than the data supports, and is really a Japan-only finding dressed as a Japan+China one

REPORT.md Executive Summary point 3 and Section 3 present "most of it is supply-constrained,
not price-induced" as "the analytical core of the report." I counted and categorized every
one of the 24 rows in `data/raw/ws3_demand_destruction.csv` by its own
`type_supply_or_price_induced` field:

- 6 of the 24 rows are not demand-destruction observations at all: one is explicitly "supply
  recovery (not destruction)" (row: CN crude imports recovered, Aug), one is a capacity
  *addition* (JP aviation jet-fuel trucking, +15,000 kl/month), one is the mirror-image *rise*
  in coal generation (not a destruction event), one is a Qatar-country row (out of the JP/CN
  scope the brief mandates), one is a WORLD-scope pipeline-status update that says outright "no
  realized demand-side macro data yet," and one is a magnitude-`NA` gap (China LNG).
- Of the rows that remain, the "price-induced" bucket has essentially **one** underlying
  phenomenon for the whole study — Japan's gas-to-coal power-sector switch — reported across
  2-3 near-duplicate rows (LNG imports -7%, gas generation -16%, coal generation +4.6%, all the
  same substitution event viewed from different angles, same source).
- **China has zero quantified, realised, price-induced demand-destruction observations in the
  dataset.** Its only "price-induced" entries are (a) the Sinopec 2026 road-fuel forecast,
  which the CSV itself labels "FULL-YEAR 2026 FORECAST (not realized hard data)" and "majority
  structural EV displacement," and (b) a steel-mills row explicitly flagged
  "directional only, low confidence, no volumes."
- One of the two largest-magnitude entries (China's crude-import collapse, -17.9%) is labelled
  a **hybrid** ("supply-constrained plus a price-induced buying-strike component") in the CSV,
  but the report's Section 3 bullet list assigns China's demand destruction only to the
  supply-constrained bucket and never mentions the price-induced component the data itself
  flags.

The directional claim ("more supply-constrained than price-induced") is defensible for Japan.
Presenting it as the report does — as a finding about "demand destruction" generally, resting
on 24 rows a quarter of which aren't demand-destruction observations, with essentially no
China-side price-induced evidence at all — overstates how much the data actually shows.
**Fix:** either scope the claim explicitly to Japan, or note plainly that China's side of the
comparison rests on an absence of evidence rather than evidence of absence.

### 2. Three mutually contradictory "hard" figures for the same metric are never reconciled, violating the study's own evidence standard

`docs/00_shared_brief.md` rule 6: "Flag contradictions between sources rather than silently
picking one." This is not done for one of the more consequential numbers in the dataset —
**China's crude oil import rate in the Aug/Sept 2026 window**:

- `data/raw/ws1_flows.csv` (`china_crude_imports_aug26`, quality `hard`, Bloomberg): **37.9 Mt**
  for August 2026 → ≈**8.9-9.0 mb/d**. Echoed in `docs/ws1_supply_disruption.md` line 23.
- `data/raw/ws3_macro.csv` (`CN_CRUDEIMPORTS`, quality `hard`, itiger.com): **49.49 Mt** for
  August 2026, noted "≈11.65 mb/d, near-full recovery." Echoed in
  `data/raw/ws3_demand_destruction.csv` and `docs/ws3_macro_impact.md` lines 167-169 ("By
  August, imports had recovered to ~11.65 mb/d").
- `docs/ws5_reserves.md` line 139-140: "By September 2026, Kpler's preliminary tracking put
  imports at **~7.2mb/d**, roughly flat versus August."

These three figures — 7.2, ~8.9, and ~11.65 mb/d — describe essentially the same country,
product, and month, span a **~60% range**, and are all tagged `hard` or `est` in different
places without a single cross-reference between them. The 37.9 Mt figure comes from a primary
wire source (Bloomberg); the 49.49 Mt figure comes from a comparatively low-quality secondary
site (itiger.com, a retail-brokerage news portal), yet it is the one that produced the
"near-full recovery" framing that flows into `docs/ws3_macro_impact.md`'s narrative. Separately,
`analysis/parameters.json`'s provenance for `CN.mitigation.max_substitution_kbd` (line 189)
silently uses the lowest of the three (8.93 mb/d, "11,000 - 8,930 = 2,070 kb/d") to derive
China's substitution-capacity parameter (1,901 kb/d) — a number that directly sets China's
substitution ceiling in every scenario the model runs — without disclosing that two other
"hard" figures in the study's own files put the same month 30-60% higher. **Fix:** reconcile
or explicitly flag the conflict, and re-derive the substitution parameter once it's resolved.

### 3. The report makes a specific, checkable claim about the tracker that is false

`docs/REPORT.md` lines 282-284 (Limitations): "Reserve deliverability ceilings — which bind
the Japanese runway in most scenarios — are unpublished and assumed. All such parameters are
listed in `analysis/parameters.json` under `assumptions` and are **tagged in the tracker's
parameter table**."

I read `app/index.html`'s `renderParams()` function (lines 1057-1078), which builds the
"Model parameters and assumptions" table (`<div id="paramTable">`, declared line 207). It
walks `PARAMS.countries.{JP,CN}` and for each parameter renders only its numeric value and,
for the 3 of roughly 40 parameters that have an entry in `PARAMS.sources` (`sources` dict,
`parameters.json` lines 201-205), a link. **It never reads `PARAMS.provenance` at all** — the
hard/calc/est/assumption tag and the textual basis for every parameter, meticulously maintained
in `parameters.json` lines 156-198, simply does not reach the UI. `grep -n "provenance"
app/index.html` returns zero matches. A user of the tracker looking at Japan's
`reserves.max_deliverable_draw_kbd = 900` — the single number the report itself says drives the
"most operationally important" result — sees only "900," with no indication it is an
unsourced guess. (The *observations* table elsewhere in the app, `renderDataTable`, does show
quality tags — that's a different table, covering the 389 sourced observations, not the ~40
scenario-model parameters this Limitations bullet is specifically about.) **Fix:** either wire
`renderParams()` to `PARAMS.provenance`, or correct the claim in the report.

### 4. The model's showcase result is a near-tautological consequence of one unsourced assumption, not a discovered dynamic

Section 6 of the report: "For Japan, subsidy withdrawal does not extend the runway... Japan's
stays pinned at 39 weeks in every variant — because Japan's draw is capped by
**deliverability**, not by stock size or by policy. This is the most counter-intuitive output
of the model and the most operationally important."

I ran `analysis/scenario_model.py` directly and inspected the intermediate values
(`run_country`, lines 144-300). For `current_grind`, `full_closure`, and
`closure_support_withdrawn`, Japan's `reserve_draw_kbd` is capped at exactly
`max_deliverable_draw_kbd = 900` in all three (confirmed `binding = "deliverability"` in each),
so `runway_weeks = usable_stock_mnbbl * 1000 / draw / 7 = 247,000 / 900 / 7 = 39.2` **by
construction** — the moment the physical gap (`lost - substitution - voluntary`) exceeds 900
kb/d in any scenario, the draw and therefore the runway stop depending on how severe the
scenario is at all. This is a property of having a fixed cap, not a finding about the shock.
And the cap's provenance entry (`parameters.json` line 168) says plainly: "Physical
draw-and-deliver ceiling; not published. This binds before stock size does and is the single
most important assumption in the Japan runway." The report's own Limitations section repeats
this candidly — but Section 6's prose oversells the result's robustness by calling it "the most
... operationally important" output without also noting there, where the reader is being asked
to act on it, that it is essentially the direct output of one invented number. **Fix:** either
source the deliverability ceiling, or present the "pinned runway" result as a sensitivity
illustration rather than a headline finding, and say so next to the claim, not only in the
Limitations section three pages later.

### 5. A load-bearing parameter is mistagged `hard` when its own cited source calls it an unconfirmed third-party estimate

`analysis/parameters.json` line 177: `"JP.policy.cpi_suppression_pp": {"quality": "hard",
"basis": "Aggregate Japanese energy-subsidy effect on headline CPI estimated at -1.0 pp
(ws4_policy)."}`. This parameter is subtracted directly from Japan's CPI in every
`policy_offset_active` scenario (`scenario_model.py` line 264-266,
`app/index.html` line 426).

Its own cited source, `docs/ws4_policy.md` lines 343-346, says: "**one third-party estimate
(not government-confirmed)** puts the combined effect of Japan's energy subsidies at
suppressing headline CPI by roughly 1.0 percentage point versus an **estimated** ~3%
'underlying' (ex-subsidy) rate." By the brief's own definitions (`docs/00_shared_brief.md`
item 2: `hard` = "published official/industry data," `est` = "credible third-party estimate"),
this is squarely `est`, not `hard`. The `parameters.json` "sources" dict (line 204) compounds
the problem by pointing to a BOJ Outlook Report PDF as the source — but ws4's own narrative
attributes the 1.0pp figure to an unnamed third party, not to the BOJ. **Fix:** retag as `est`
and correct the source citation, or find the primary BOJ figure if one exists.

### 6. A `calc`-tagged parameter doesn't reproduce from its own stated formula

`parameters.json` line 170: `"JP.mitigation.max_substitution_kbd": {"quality": "calc", "basis":
"Hormuz share fell 94.1% -> 59.3% by Jul 2026 (both sourced); 34.8% x 2,360 kb/d = 826 kb/d of
demonstrated substitution."}`. Recomputing: 34.8% × 2,360 = **821.28**, not 826. Reproducing
826 requires exactly 35.0 percentage points of share change, not the 34.8 stated in the basis
text. The discrepancy is small (≈0.6%) but it means the audit trail the `calc` tag exists to
provide — "show the formula" per the brief's evidence standard 2 — does not actually check out
on inspection. This parameter sets Japan's substitution ceiling in every scenario the model
runs. **Fix:** recompute and correct either the stated percentages or the resulting figure.

### 7. Channel 1 (terms of trade) and Channel 3 (rationing) partially double-charge the same missing barrels

`scenario_model.py`'s Channel 1 (lines 152-166) bills the country for its **full baseline**
`net_oil_import_mbd` at the new scenario price, in every scenario, regardless of how much of
that import volume the model's own Channel 3 subsequently determines is **physically
unavailable and rationed away** (`involuntary_dd_kbd`). Under `full_closure`, Japan's
`involuntary_demand_destruction_kbd` is 382 kb/d — about 16% of `net_oil_import_mbd` (2,360
kb/d) — oil Japan never actually obtains. Yet Channel 1's `oil_transfer_bn` still charges Japan
for importing its full 2.36 mb/d baseline volume at $145/bbl (you don't pay import prices on a
barrel you never received), and Channel 3 then applies a **separate, larger** GDP penalty
(`gdp_pp_per_pct_involuntary_demand_cut = 0.25`) to the same missing barrels. This is not a
divergence between the Python and JS implementations (both share the flaw identically — see
Finding 8 below), but a genuine internal-consistency issue in the model design that neither
the code's docstring nor the report's model discussion mentions. **Fix:** net the ToT-relevant
import volume down by the rationed shortfall before pricing it, or document why the current
treatment is intentional.

### 8. The model's LNG channel is price-only; the report's own emphasized binding constraint (LNG) never enters the physical/runway channels at all

The report is emphatic that "**crude is not the binding constraint. LNG and naphtha are**"
(Section 5) and that Japan has "**roughly a fortnight of buffer**" on LNG (Executive Summary
point 6). But `run_country`'s Channels 2-4 (voluntary/involuntary demand destruction and
`runway_weeks`) operate exclusively on `c["energy"]["oil_demand_kbd"]` and
`oil_imports_via_hormuz_kbd` (`scenario_model.py` lines 168-231); LNG (`lng_import_mt`,
`jkm_usd_mmbtu`) appears **only** in Channel 1 as a pure income-transfer term (lines 159-164).
There is no LNG substitution cap, no LNG reserve, no LNG runway anywhere in the model or in
the scenario table the report presents (Section 6 shows GDP and CPI only, no runway column at
all, and the only `runway_weeks` output the model produces is crude-only). So the number the
report treats as the analytically central vulnerability of the whole study is not represented
in the quantitative model at all — a real gap between the qualitative narrative and the
quantitative deliverable. **Fix:** either add a minimal LNG physical-balance channel, or state
explicitly in Section 6 that the scenario engine does not model the LNG constraint the rest of
the report identifies as binding.

## Minor findings

- **CPI channel ignores the LNG/gas price shock.** `cpi_direct` (`scenario_model.py` line 258)
  is driven solely by `pct_price_change`, which is defined from Brent (`d_oil / base_brent`,
  line 187). JKM moved roughly 3x more in percentage terms than Brent in the base scenario
  (24.7/11.3 vs 100/71), and gas is 31-34% of Japan's power generation per the report's own
  Section 2 table — yet none of that shows up in the CPI formula, even though the GDP
  terms-of-trade channel (Channel 1) does include LNG. The asymmetry is unexplained.
- **Executive summary reads more settled than the underlying evidence.** REPORT.md's
  Executive Summary point 1 states the East-West pipeline "shut on 2026-09-11" and "that
  cushion is now eroding" without the hedge that appears later, in the same section's body:
  "its status as of this writing is unconfirmed and is **the highest-value open question in
  the dataset**" (Section 1, and `docs/ws1_supply_disruption.md` lines 131-142, which also
  notes Yanbu loadings data hard to reconcile with a fully-shut pipeline). A reader who stops
  at the Executive Summary gets a more settled picture than the workstream evidence supports.
- **A range doesn't reproduce from its own displayed table cells.** REPORT.md's Section 1
  table gives "Gulf crude exports (incl. bypass): ~20-24 mb/d → 13-15.5 mb/d, −33% to −50%."
  Naive subtraction from the displayed endpoints gives a 22.5%-45.8% range, not 33%-50%; the
  33-50% figure is actually a blend of two different sources' own internally-paired
  baseline/current estimates (Kpler's vs. IEA's own respective pairs — see
  `docs/ws1_supply_disruption.md` lines 54-64), not the min/max of the two displayed ranges. A
  reader sanity-checking the table with its own numbers won't reproduce it.
- **Untagged conversion factors.** `parameters.json`'s `conversions.mmbtu_per_tonne_lng` (52.0)
  and `conversions.bcm_per_mt_lng` (1.36) are load-bearing in the LNG terms-of-trade calculation
  and in deriving China's `lng_import_mt_yr`, but appear in neither the `provenance` dict nor
  the `assumptions` list, despite the file's stated discipline that "every parameter carries a
  quality tag in provenance" (line 5).
- **A ">value" silently treated as "=value."** `CN.energy.lng_import_mt_yr` (73.5 mt, `calc`)
  divides a pre-war LNG-import figure that `docs/ws2_reliance.md` states as "**>100 bcm**"
  ("2025 consumption ~456 bcm... LNG imports >100 bcm") by exactly 100, treating a stated floor
  as a point value.
- **Two different CPI series conflated under one number.** `docs/ws4_policy.md` line 342 cites
  "Tokyo core CPI reached 1.8% y/y in **August** 2026," while REPORT.md and
  `docs/ws3_macro_impact.md` use national core CPI "1.8% (**Jul** 2026)." Tokyo CPI is a
  distinct, narrower index that leads the national print by about three weeks; ws4 doesn't
  flag that it's a different series for a different month, even though it happens to share the
  same headline figure.
- **An undated baseline presented as current.** Japan's "97% crude import dependence"
  (Executive Summary point 2, Section 2 table) traces in `docs/ws2_reliance.md`'s Uncertainties
  section to a 2022-vintage EIA/IEA figure "used... as a floor... marked `est`, not `hard`" —
  the report presents it without a date, in mild tension with the brief's own evidence standard
  5 ("every impact claim needs both" a dated pre-war baseline and a dated current reading).
- **A rounding chain that's circular but immaterial.** Japan's
  `oil_imports_via_hormuz_kbd` (2,221 kb/d) is `2,360 × 94.1%`, where 94.1% is itself a rounded
  `calc` (2,220/2,360×100, per `data/raw/ws2_dependency.csv` line 4) — reapplying a rounded
  percentage to its own source volume produces a ~1 kb/d drift. Trivial in size, but it shows
  the `calc` chain isn't always internally exact, consistent with Finding 6.

## What the study does well

- **The Python and JavaScript models are genuinely faithful ports of each other.** I diffed
  `run_country` (`analysis/scenario_model.py` lines 144-300) against `runCountry`
  (`app/index.html` lines 369-442) term by term: identical variable order, identical formulas,
  and — specifically checked, since the task flagged it as a likely divergence point — voluntary
  demand response is computed before the reserve draw in both, with matching comments
  explaining why. I ran both independently (Python via `python3 analysis/scenario_model.py`;
  the JS logic by inspection against the Python's actual numeric output) and found no
  divergence across all 8 scenario×country combinations.
- **The observation-level evidence tagging is real.** `data/curated/master_observations.csv`
  has 389 data rows; 227 `hard`, 148 `est`, 6 `calc`, 8 untagged (2.05%) — this matches
  REPORT.md's Limitations claim ("389 observations... 2% are unlabelled") exactly, and matches
  `app/data.json`'s own `analysis.counts` block. The dataset uses `NA` rather than invented
  numbers in many places where data genuinely wasn't found (China's September crude figure,
  several petrochemical prices, Japan urea/ammonia/sulphur dependency).
- **Scenario outputs are consistently disclaimed as not forecasts**, both in REPORT.md
  ("Model results, not forecasts: they state what the stated assumptions imply," Section 6
  header) and in the tracker's footer (`app/index.html` line 1138: "Scenario outputs are model
  results, not forecasts"). I did not find a single place where a scenario number is presented
  as a prediction.
- **Realised-vs-forecast discipline is maintained in the workstream that matters most for it.**
  `docs/ws3_macro_impact.md` explicitly separates "realised prints" from "forecast revisions"
  (its own Section 4 heading), and REPORT.md Section 3 is headed "Realised — not forecast."
- **Country scope is respected in the report's own claims.** Comparator/supplier data (Qatar,
  Saudi Arabia, world aggregates) is used only as context for Japan/China exposure, never
  folded into a JP/CN headline number.
- **The app handles missing data defensively.** `app/index.html`'s render functions
  consistently filter or coalesce `null`/`NaN`/`undefined` before charting (e.g. lines 326,
  503, 520, 736, 946, 982) rather than letting a gap crash a chart or silently render "NaN."

## Checks performed

- Read `docs/REPORT.md`, `docs/00_shared_brief.md`, and all five `docs/ws1`-`ws5` files in
  full.
- Read `analysis/scenario_model.py` and `analysis/parameters.json` in full.
- Ran `python3 analysis/scenario_model.py` directly and reproduced every figure in REPORT.md's
  Section 6 scenario table (GDP/CPI for all 4 scenarios × 2 countries) to the reported
  precision; also reran with a small script to extract intermediate values and confirmed the
  "69→172 kb/d" / "382→279 kb/d" voluntary/involuntary figures, the "71→90 week" and "pinned at
  39 week" runway claims, and the `binding` constraint (`deliverability`/`policy`/`shortfall`)
  for every scenario×country combination.
- Diffed `app/index.html`'s `runCountry` (JS, lines 369-442) against `run_country` (Python,
  lines 144-300) term by term for arithmetic and ordering; confirmed no divergence, including
  the specific order-of-operations question the task raised (voluntary demand response before
  reserve draw).
- Confirmed `app/data.json`'s embedded `parameters` object is byte-identical to
  `analysis/parameters.json` (`d.get('parameters') == p` → `True`), and that
  `app/scenarios.json`'s results match a fresh model run field-by-field — no staleness between
  the model, the parameter file, and the shipped app payload as of this review.
- Recomputed every `calc`-tagged parameter in `parameters.json`'s provenance dict against its
  stated formula and the CSV rows it cites; found one exact-reproduction failure (Finding 6)
  and one immaterial rounding circularity (minor findings).
- Cross-checked China's crude-import figures across `data/raw/ws1_flows.csv`,
  `data/raw/ws3_macro.csv`, `data/raw/ws3_demand_destruction.csv`, and `docs/ws5_reserves.md`
  for the Aug/Sept 2026 window; found the three-way contradiction in Finding 2.
- Read and categorized all 24 rows of `data/raw/ws3_demand_destruction.csv` by their
  `type_supply_or_price_induced` field and cross-checked the categorization against the wording
  of REPORT.md Section 3 (Finding 1).
- Read `app/index.html`'s rendering functions (`renderParams`, `renderDataTable`, `renderKPIs`,
  `renderSupply`, `renderReliance`, `renderMacro`, `renderPolicy`, `renderReserves`,
  `renderHeatmap`, `boot`) to check missing-data handling and to verify the specific claim in
  Finding 3 about the parameter table (`grep -n "provenance" app/index.html` → no matches).
- Verified `data/curated/master_observations.csv` row and quality counts (390 lines incl.
  header → 389 rows; 227 hard / 148 est / 6 calc / 8 NA) against REPORT.md's Limitations claim
  and against `app/data.json`'s `analysis.counts` block.
- Spot-read `scripts/build_dataset.py`'s CSV-parsing logic (`parse_number`, `read_csv`) to
  understand how `NA`/ranges/malformed rows are handled; confirmed via
  `data/curated/master_observations.csv` that zero rows in this dataset actually needed
  range-midpoint collapsing (all populated `value` cells parsed as `exact`).

**Not checked / out of scope for this review:**
- No WebSearch or WebFetch was available; I did not verify any external source cited in the
  workstream docs for accuracy, currency, or misquotation. All findings above are about
  internal consistency between the study's own files, not about whether the underlying
  real-world facts are correctly reported.
- I did not independently re-derive every `est`/`hard` figure in the five workstream docs
  against primary sources — only the ones load-bearing enough to affect a headline claim or a
  model parameter were traced back to their cited CSV rows and, where feasible, recomputed.
- I did not execute `scripts/validate_data.py`, `scripts/repair_csvs.py`, or
  `scripts/update_data.py`, and did not audit the GitHub Actions workflow
  (`.github/workflows/update-data.yml`) that presumably runs them.
- I did not test `app/index.html` in an actual browser; the "handles missing data without
  breaking" assessment in Finding/Section F is based on static code reading (null/NaN guards
  present at every render call site I checked), not runtime testing.
- I did not check whether `data/curated/*.csv` themselves are byte-consistent with
  `data/raw/*.csv` beyond the specific rows examined for the findings above (the curated files
  are a mechanical concatenation per `scripts/build_dataset.py`, and I did not diff them
  file-by-file).
