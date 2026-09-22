# Independent audit of the revision (6c4c506 → HEAD)

Scope: the changes made since the first review (`docs/REVIEW.md`), i.e. the diff
`6c4c506..HEAD`. I re-ran the model directly (`python3 analysis/scenario_model.py` and a custom
harness importing `run_country`), diffed `run_country` against `runCountry` in `app/index.html`,
recomputed every new `calc`/`est` figure from its stated formula, and cross-checked the new
`data/raw/ws6_followup.csv` rows against how they are used downstream. No WebSearch was used, per
instructions; all findings are internal-consistency and arithmetic checks against the repository's
own numbers.

## Verdict

This revision is a real improvement on the specific points the first review named — the pipeline
question is answered, the China import conflict has a resolving data point, the tracker now
renders provenance tags, and the double-charging and mis-tag bugs are fixed as claimed. But the two
new headline claims it is proudest of are weaker than presented, and the document has grown a new,
worse version of the exact failure the first reviewer diagnosed: **confidence that outruns the
audit trail**. The naphtha "not a cliff" conclusion rests on a Middle-East-dependence input (40%)
that the study's own cited source says is roughly half of Japan's true exposure once ME-sourced
domestic refining is counted — nobody in the report ever runs the numbers with the larger figure.
The LNG "112-day" runway is a hand calculation that the shipped model *never actually produces* in
any of its four scenarios (the assumed substitution cap happens to exceed the worst-case loss in
every one, so the tracker always reports "no gap to cover"). And the report's own
"Independent review" section — unchanged since v1 — still says the model is "crude-only" and that
LNG is merely "Disclosed... not modelled," flatly contradicting this same document's Section 5/6
and changelog, which are about nothing else. The single biggest remaining weakness is the same one
the first review named: the narrative is more confident than the evidence trail it discloses, and
this revision's marquee corrections have not been checked with the same rigor that was applied to
finding fault with the *previous* version.

## Material findings

### 1. The report contradicts itself about whether LNG is modelled at all

`docs/REPORT.md`'s "Independent review" table (lines 299–319) is **byte-identical** to the same
section in the v1 report (verified: `git show 6c4c506:docs/REPORT.md` vs HEAD, no diff in this
section). It still says: "LNG absent from the model's physical channels | **Disclosed** — stated
at the scenario table; not modelled" and "the model remains crude-only in its physical channels."
This directly contradicts the rest of the *same* document: Section 5 ("Modelling the balance
explicitly..."), Section 6 ("The engine now models both LNG and naphtha physically"), and the
changelog table itself (line 349, "**112+ days** against the Hormuz-attributable gap"). Whoever
wrote this revision's Sections 5, 6 and the changelog never went back to update the self-audit
table three sections later. A reader who reads the whole document gets two irreconcilable answers
to "does the model include LNG?" **Fix:** update the Independent-review table's LNG row to
"Fixed" (or explain why it's still listed as unmodelled) before publishing this revision.

### 2. The naphtha exposure figure the whole "not a cliff" conclusion rests on is likely roughly half the true exposure

`analysis/parameters.json` line 67: `"me_dependent_pct": 40.0`. Its own provenance (line 407)
says: "Japan imports about 40% of its naphtha from the Middle East. (Its exposure is larger
still: 95% of the crude used in domestic refining was ME-sourced, and that refining supplies
roughly another 40% of naphtha demand — so 40% is the directly-imported slice, not total
exposure.)" The underlying source row, `data/raw/ws6_followup.csv` (`jp_naphtha_me_import_share`),
says exactly this, tagged `hard`. Doing the arithmetic the source itself invites: total
ME/Hormuz-linked exposure ≈ 40% (direct import) + 40% × 95% (domestically refined naphtha made
from ME crude) ≈ **78%**, not 40%. `run_country`'s naphtha block (`scenario_model.py` lines
263–294) and `runCountry`'s (`app/index.html` lines 408–420) both use only the 40% figure as
`me_dependent_pct`. This is not a minor rounding issue: it is used as the multiplicative base for
`naphtha_supply_loss_pct = me_dependent_pct * (1 - throughput/100)`, so doubling the base roughly
doubles the modelled loss at any given throughput. Two consequences: (a) the calibration of
`max_substitution_pct = 24.7` (line 70), which is fitted so `40% loss − substitution = 11.3pp
cracker-rate decline` (line 419), would need `max_substitution_pct ≈ 59%` if the correct 78% base
were used to explain the *same* 11.3pp observed decline — i.e. either Japan re-sourced/replaced
almost 60% of its naphtha needs within weeks (implausible given `ws2_substitutability.csv` row 15
rates non-ME naphtha substitutability "low," citing a small base and a competing South Korean
export ban) or the 40% base itself is what's making the fit work, at the cost of understating the
true physical exposure by roughly 2×. (b) The "not an approaching cliff — continuous output loss"
framing (Section 5, `docs/REPORT.md` lines 252–260) is built entirely on this understated base; if
the true base is ~78%, a further drop in Hormuz throughput (e.g. under `full_closure`, 2%) would
produce a far larger, and much less "continuous/manageable," feedstock gap than the model shows.
**This caveat is disclosed only in `parameters.json`'s provenance text and the raw CSV note — it
never appears in `docs/REPORT.md`'s Section 5 or 6 narrative**, where the 40% figure is presented
flatly ("about 40% of naphtha is imported directly from the Gulf," line 249) with no signal to the
reader that the source it's drawn from says the real number is roughly double. **Fix:** either
build a `me_dependent_pct_total` that includes the indirect refining channel and show both cracker-
rate paths, or state the caveat prominently next to the naphtha conclusion, not only in the
parameter file.

### 3. The price-channel "cross-check" numbers in Section 6 don't reproduce from the model, and the China figure fails its own benchmark

`docs/REPORT.md` line 297–299: "The price channel needed no adjustment — at Brent $100 it yields
**−0.85pp for Japan and about −0.5pp for China**, both inside the published ranges." I ran
`run_country` for `current_grind` (Brent $100) and read `gdp_impact_breakdown['terms_of_trade']`
directly:
- Japan: **−0.76pp** (not −0.85; a control run confirms `total_tot_transfer_pct_gdp=1.529%` ×
  `tot_transfer_to_gdp_multiplier=0.5` = 0.7645, rounds to 0.76). The −0.85/−0.87 figure appears to
  come from applying GlobalData's raw "0.3pp per $10/bbl" proxy directly to the $29 Brent move
  (0.3×2.9=0.87) — a *different* calculation from what the code in `scenario_model.py` line 340
  (`gdp_from_tot = -total_tot_pct * tot_mult`) actually produces.
- China: **−0.29pp** (not −0.5; `total_tot_transfer_pct_gdp=0.831%` × `tot_transfer_to_gdp_multiplier=0.35`
  = 0.2907). The claimed benchmark range, from `parameters.json` line 311 itself
  ("GlobalData's −0.15 to −0.2pp per $10/bbl... at Brent $100 (+$29) that implies about −0.5pp"),
  computes to −0.435 to −0.58pp. The model's actual output, **−0.29pp, falls outside (below) the
  very range it is claimed to sit inside.**

Both discrepancies stem from the same design choice: `tot_mult` is applied to `total_tot_pct`,
which bundles the oil *and* LNG transfer together, while the calibration narrative and the
external Korea/GlobalData comparisons describe an oil-price-only relationship. The multiplier
therefore does not deliver the number the provenance text says it delivers. This is exactly the
kind of "calc that doesn't reproduce from its stated formula" the first review caught elsewhere
(Finding 6) — recurring here in the section added specifically to demonstrate that "the price
channel needed no adjustment." **Fix:** recompute `gdp_from_tot` isolating the oil-only component
before comparing to GlobalData/Korea, or restate the cross-check numbers to match what the code
actually outputs.

### 4. The LNG physical channel never binds in any of the four scenarios — the "112-day" figure is not a model output

Running all four scenarios for Japan: `lng_unserved_mt_yr` = 0.0 in **every one** (de-escalation,
current grind, full closure, closure-support-withdrawn), because `max_substitution_mt_yr = 8.0`
(an unsourced `assumption`, `parameters.json` line 63/383) exceeds the maximum possible loss even
at zero throughput (`66 × 11% = 7.26` mt/yr). Consequently `lng_runway_days` is `None` in all four
—confirmed against `app/scenarios.json`, which ships the same result. The tracker a reader is told
to "run yourself" (`docs/REPORT.md` line 282) will **never show an LNG runway number**; it always
reports "no gap to cover." The report's headline "112+ days" (Executive Summary, Section 5 table,
changelog) is a hand-computed hypothetical ("even with zero re-sourcing and zero fuel switching") —
a legitimate sensitivity check, but it is not a scenario the model runs or the interactive tool can
reproduce, and the report does not flag that the physical-balance addition it advertises leaves
this channel permanently slack. Separately, that hand calculation itself is slightly off: 2.19mt ÷
(7.26mt/365) = **110.1 days**, not 112 — a small (~1.8%) but real arithmetic slip in the flagship
number of the correction. **Fix:** either show the zero-substitution hypothetical as an explicit
sensitivity row in the model/tracker output (not just prose), or correct "112" to ~110, and note
in Section 6 that the LNG channel is slack in every scripted scenario.

### 5. Section 5/6's own reserve figures are stale relative to this revision's own parameter update

This revision updated `JP.reserves.usable_stock_mnbbl` from 247mn bbl to **270mn bbl**
(`parameters.json` line 219: "Supersedes the 247mn bbl figure derived from January data"), and
`app/scenarios.json` (the shipped tracker data, confirmed freshly matches a live model run)
correctly shows Japan's runway at **42.9 weeks**, not 39.2. But `docs/REPORT.md` still says, in two
places: Section 5's table (line 229) "Usable cushion | ~247mn bbl" and Section 6 (lines 320–321)
"Japan's 39.2 weeks is just 247mn bbl ÷ 900 kb/d ÷ 7." Both are the *old* v1 numbers, left
unreconciled with the parameter this very revision updated (and with the report's own changelog
row claiming the reserve figures were refreshed). A reader who runs the tracker gets 42.9 weeks;
the report's prose tells them 39.2. **Fix:** update both instances to 270mn bbl / 42.9 weeks, or
explain the discrepancy if it is intentional.

### 6. "Resolved" is an overstatement for the China import conflict — two of the three conflicting figures are still live and uncorrected

The changelog (line 352) claims: "China Aug imports | Three-way conflict (7.2 / 8.9 / 11.65 mb/d),
unresolved | **Resolved: 37.93 Mt = 8.93 mb/d**, official GACC customs." The new figure (GACC via
`ws6_followup.csv`) is real and well-sourced, and it correctly fixed
`CN.mitigation.max_substitution_kbd` (`parameters.json` line 303). But the other two conflicting,
`hard`-tagged figures the first review flagged are **still present, unflagged, and uncorrected**:
- `data/raw/ws3_macro.csv` line 67 and `data/raw/ws3_demand_destruction.csv` line 6 still carry
  49.49 Mt (≈11.65 mb/d) tagged `hard`, sourced to itiger.com, with no note that GACC customs data
  (a materially more authoritative primary source) puts the same month 24% lower.
- `docs/ws3_macro_impact.md` lines 84 and 167 still narrate "imports had recovered to ~11.65 mb/d
  (Aug, near-full recovery)" — the framing the first review specifically criticized — unchanged.
- `docs/ws5_reserves.md` lines 140/164 and `data/raw/ws5_runway.csv` line 9 still use a *third*,
  separate figure ("~7.2mb/d Sept prelim," Kpler) for China's current import rate, feeding a
  runway calculation that is never reconciled with the 8.93 mb/d GACC figure used everywhere else.
This is a real partial fix (one load-bearing model parameter now rests on the better source) mis-
described as a full resolution of "the conflict." The project's own evidence standard ("flag
contradictions between sources rather than silently picking one," per the first review's Finding
2) is still not honored for the two untouched files. **Fix:** either retag/annotate the 49.49 Mt
and 7.2 mb/d rows as superseded, or downgrade the changelog's claim from "Resolved" to "one
parameter re-derived; other cited figures not reconciled."

### 7. The tracker's parameter table still doesn't show most of this revision's new (and least-vetted) parameters, despite the report's repeated claim that it does

`app/index.html` line 1160: `const groups = ['macro','energy','reserves','elasticities','cpi',
'policy','mitigation'];` — this list was not updated to include the two groups this revision
added to `parameters.json`, `lng` and `naphtha`. Confirmed by grep: `lng`/`naphtha` never appear
anywhere in `app/index.html` outside `runCountry` itself. The result: none of the ~18 new
parameters — `imports_via_hormuz_pct`, `stock_mt`, `max_substitution_mt_yr`, `switchable_mt_yr`,
`me_dependent_pct`, `stock_days`, `cracker_rate_prewar_pct`, `max_substitution_pct`,
`downstream_buffer_days`, for both countries — appear in the "Model parameters and assumptions"
table, values or provenance tags alike. Yet `docs/REPORT.md`'s Limitations section states: "What
is still assumed and still matters: **the LNG substitution and fuel-switching capacities**...
**China's naphtha exposure**... All are listed under `assumptions` in `analysis/parameters.json`
and **tagged in the tracker's parameter table**." That last clause is false for exactly the
parameters it names. This is the same specific, checkable claim the first review's Finding 3
caught about the *previous* version of the table — now recurring for this revision's newest and
least-sourced additions, including the naphtha substitution capacity that Finding 2 above shows is
calibrated on a possibly-understated exposure base. **Fix:** add `lng` and `naphtha` to the
`groups` array in `renderParams()`.

## Minor findings

- **The rationing-coefficient "bracket" is a loose upper bound dressed as an anchor.** The
  electricity-curtailment literature (`ws6_followup.csv`, `lit_electricity_curtail_equilibrium`
  etc.) gives "0.2–0.4 per 1% curtailment" only as an *upper* bound (oil is asserted to be more
  substitutable, hence lower) — it does not itself argue for 0.12 over, say, 0.05 or 0.18; any
  value under 0.4 is "consistent" with it. The "lower bound" side of the argument
  (`parameters.json` lines 243/315) compares the model's **total, all-channel** GDP output against
  the IMF's ~1pp **total** regional figure, then attributes the entire gap to the rationing
  coefficient alone — but Finding 3 above shows the price/ToT channel's own calibration is not
  precise either, so the "fix" may be partly compensating for error elsewhere. After the change,
  `full_closure`'s Japan GDP hit is still −2.97pp, roughly 3× the IMF benchmark it is claimed to be
  checked against — the same order of overshoot the original 0.25 produced, just smaller. The
  coefficient went from "unanchored" to "loosely bounded," not to "anchored," and the report's
  language ("Bracketed," "no longer an unanchored guess") oversells the improvement.
- **Source quality: two of the newest "hard" tags rest on low-authority sites for load-bearing
  numbers.** `worldometers.info` (a data-aggregation site, not a primary statistical agency) is
  tagged `hard` for `jp_oil_demand_2025` (`ws6_followup.csv`), which directly sets
  `JP.energy.oil_demand_kbd = 3071`, used in every scenario's demand-destruction and CPI
  denominator. `plastic-pallet.co.jp` — a site with no evident standing as a petrochemical-industry
  data source — is tagged `hard` for **three** separate, decisive naphtha parameters
  (`jp_naphtha_stock_days`, `jp_naphtha_me_import_share`, `jp_pe_pp_downstream_buffer`), which is
  the entire evidentiary base for the naphtha channel this revision calls "the constraint the study
  concludes actually binds." Neither site is disqualifying on its own, but `hard` (per the
  project's own brief, "published official/industry data") oversells them; `est` would be the
  honest tag, and it would have been worth corroborating at least the ME-dependence split against
  the `ws2_dependency.csv`/`ws5_reserves.csv` rows already in the dataset (which give 60–74%
  import-ME-share figures that don't cleanly match the 40%/40% split this source is used for).
- **The "35 of 66" sourced-parameter count is arithmetically correct but blends categories.**
  Recount confirms: 66 provenance entries, 13 `hard` + 12 `est` + 10 `calc` = 35, 31 `assumption`.
  Accurate as stated. But `est` ("credible third-party estimate") is bundled into "sourced" on par
  with `hard`; a reader skimming "35 of 66 sourced" could reasonably think more of the 35 are
  primary data than the 13 that actually are.
- **`JP.cpi.gas_retail_passthrough` and `CN.cpi.gas_retail_passthrough` share a verbatim,
  Japan-specific justification.** `parameters.json` lines 397–404: the basis text for China's gas
  pass-through parameter is a copy-paste of Japan's ("Calibrated so the base scenario reproduces
  **Japan's** realised position: core CPI 1.8%...") — it does not actually describe how China's
  0.25 value was chosen, only restates Japan's calibration rationale under China's key.
- **Two rounding-linked ~2% drifts.** The naphtha runway/downstream-buffer figures reported in text
  (138–160 days, 620–720 days) reproduce exactly from the model; the LNG "112 days" figure does not
  (see Finding 4) — the inconsistency between how carefully one number was checked versus the other
  is itself notable.

## Assessment of the v1 fixes

Genuinely fixed, verified directly:
- Demand-destruction balance rescoped to Japan; China's evidentiary gap stated (`docs/REPORT.md`
  Section 3).
- `JP.mitigation.max_substitution_kbd` recomputed: 34.8% × 2,360 = 821.28 → 821 (was 826). Now
  reproduces exactly.
- `JP.policy.cpi_suppression_pp` retagged `est`, BOJ attribution removed
  (`parameters.json` line 257–259).
- Terms-of-trade/rationing double-charge fixed in both `scenario_model.py` (lines 296–304) and
  `app/index.html` (lines 436–439): import bill now struck on delivered volume, confirmed
  identical in both ports.
- Tokyo-vs-national CPI conflation flagged with an inline caveat (`docs/ws4_policy.md` diff).
- `scripts/validate_data.py` no longer counts genuine `NA`/missing rows as "unlabelled."

Partially fixed / weaker than claimed:
- **v1 Finding 2 (China import conflict):** one parameter re-derived on better data; the conflict
  itself (three figures, two files, one narrative paragraph) is not reconciled — see Material
  Finding 6.
- **v1 Finding 3 (tracker doesn't tag provenance):** fixed for the parameters that existed in v1,
  but the same failure mode now applies to every parameter this revision added — see Material
  Finding 7. This is the clearest case of a fix not generalizing past the specific instance a
  reviewer happened to name.
- **v1 Finding 4 ("pinned runway" oversold as a finding):** the prose framing genuinely softened
  ("treat this as an illustration, not a finding," `docs/REPORT.md` line 313), which is the right
  fix — but the specific numbers attached to it (247mn bbl, 39.2 weeks) are now stale relative to
  this revision's own parameter update (Material Finding 5), so the illustration itself no longer
  matches the model.
- **v1 Finding 8 (LNG not modelled):** substantively addressed by a genuine new physical-balance
  channel — but the report's own "Independent review" section was never updated to reflect this
  (Material Finding 1), and the channel never binds in any scripted scenario (Material Finding 4),
  so "modelled" is a stronger word than what the shipped tool actually demonstrates.

Not revisited (correctly disclosed as such): the GDP elasticity remains a cross-country proxy, the
CPI channel's energy weights and pass-through rates remain assumptions, and China's naphtha
exposure is correctly left unmodelled rather than invented.

## Checks performed

- Read `docs/REPORT.md` in full (current and, via `git show 6c4c506:docs/REPORT.md`, the prior
  version) and diffed the two directly for the "Independent review" and Section 5/6 text.
- Read `docs/REVIEW.md` in full to establish what v1 found and avoid re-litigating fixed items.
- Read `analysis/scenario_model.py` and `analysis/parameters.json` in full.
- Ran `python3 analysis/scenario_model.py` and a custom harness calling `run_country` directly for
  all four scenarios × both countries; extracted `gdp_impact_breakdown`, `cpi_impact_breakdown`,
  `lng_lost_mt_yr`/`substituted`/`switched`/`unserved`/`runway_days`, and
  `naphtha_supply_loss_pct`/`gap_pct`/`implied_cracker_rate_pct`/`stock_runway_days`/
  `downstream_runway_days` for every combination.
- Recomputed by hand: the naphtha calibration (36% − 24.7% = 11.3pp, and 78.6 − 11.3 = 67.3 —
  reproduces exactly); the naphtha stock/downstream runways (137.9–160.0 and 620.7–720.0 days —
  matches the report's "138–160" and "620–720"); the LNG zero-substitution hypothetical
  (2.19 ÷ (7.26/365) = 110.1 days, not the reported 112); the ToT/GDP cross-check for both
  countries against GlobalData's stated ranges (Finding 3); and the true naphtha ME-exposure
  implied by the source's own note (≈78% vs the 40% used, Finding 2).
- Confirmed `app/data.json`'s embedded parameters equal `analysis/parameters.json`
  (`d['parameters'] == p` → `True`) and that `app/scenarios.json`'s `runway_weeks` (42.9) reflects
  the *current* `usable_stock_mnbbl` (270), not the stale 247/39.2 figures still in `docs/REPORT.md`.
- Diffed `run_country` (`analysis/scenario_model.py` lines 169–429) against `runCountry`
  (`app/index.html` lines 369–496) term by term, including the new naphtha and LNG blocks and the
  fuel-split CPI (`oil_share_of_energy_basket`, `gas_retail_passthrough`); found no numerical
  divergence between the ports.
- Grepped `app/index.html` for `lng`/`naphtha`/`provenance` to check the parameter-table rendering
  path (`renderParams`, lines 1127–1173) and confirmed the `groups` array (line 1160) omits the two
  new parameter groups.
- Recounted `analysis/parameters.json`'s `provenance` dict by quality tag (66 total: 13 hard / 12
  est / 10 calc / 31 assumption; 35 sourced) — matches the report's "35 of 66" claim exactly.
- Cross-checked `data/raw/ws6_followup.csv`'s new rows (46 lines) against `parameters.json`'s
  provenance citations and against the pre-existing `ws2_dependency.csv`/`ws5_reserves.csv` naphtha
  rows for consistency; traced the `worldometers.info` and `plastic-pallet.co.jp` citations across
  `data/raw/`, `data/curated/master_observations.csv`, and `app/data.json`.
- Searched `data/raw/ws3_macro.csv`, `ws3_demand_destruction.csv`, `docs/ws3_macro_impact.md`,
  `docs/ws5_reserves.md`, and `data/raw/ws5_runway.csv` for the China crude-import figures the
  changelog claims to have resolved; confirmed two of the three conflicting figures are still
  present and uncorrected.
- Did not use WebSearch/WebFetch (per instructions); did not independently verify any external
  source's real-world accuracy — only internal consistency, arithmetic reproduction, and whether
  the report's claims about its own data/model/tracker are true.
