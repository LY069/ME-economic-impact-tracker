# The Hormuz shock and the Asian economies

### Economic impact of the 2026 Iran–US conflict energy disruption on Japan and China

**As of 2026-09-15 — day 199 of the conflict** (2026-02-28 start).

> **Second pass.** This revision closes the gaps the first version disclosed. The
> pipeline question is answered, the Chinese import conflict is resolved against official
> customs data, the model gained an LNG physical channel, and the GDP and CPI channels were
> recalibrated against published benchmarks. **Two headline claims changed materially —
> see `## What changed in this revision`.**

Supporting data: `data/curated/` · Model: `analysis/scenario_model.py` · Tracker: `app/index.html`
Workstream detail: `docs/ws1`–`ws5`.

---

## Executive summary

The largest oil supply disruption in market history has, so far, produced a **deceleration rather
than a recession** in both Japan and China — and that gap between the size of the physical shock
and the modesty of the macro damage is the single most important thing to understand about this
episode. It exists because three buffers absorbed the blow: **reserves**, **substitution**, and
**subsidy**. All three are depleting, and none of them can be topped up.

Six findings follow.

**1. The physical disruption is severe, partly bypassed, and currently re-tightening.** Hormuz
crude and petroleum-liquids transit fell from 21.6 mb/d (4Q25) to 4.9 mb/d (2Q26), a 77% collapse.
But Gulf crude *exports* — counting barrels that leave via bypass pipelines — held near 13–15.5
mb/d, a 33–50% loss. The distinction matters: the strait is closed, the Gulf is not sealed. That
cushion is now eroding. The Saudi East–West pipeline, which had been moving ~4–5 mb/d, **shut
on 2026-09-11** after drone strikes launched from Iraqi territory. Satellite imagery shows its
**pumping station completely destroyed**; industry estimates put repairs at **five to six
weeks**, though the US Energy Secretary said on 09-14 that the line would "come back on
shortly." Talks on shipping protection collapsed on 09-13. LNG is the harder hit on paper:
Qatar's H1 cargo count fell from 509 to 18 (−96%).

**2. Japan is more exposed structurally; China is more exposed in narrow chokepoints.** Japan
imports about 97% of its crude (a 2022-vintage figure, the most recent sourced) and drew
94–95% of it from the Gulf pre-war, with a supplier HHI near
3,600 — one of the most concentrated energy dependencies in the developed world, and it has no
pipeline alternative. China sourced 36% via Hormuz, produces ~4.3 mb/d domestically, and takes
Russian barrels overland. But China holds the most concentrated single dependency found anywhere
in this study: **Iran supplied 60.4% of its methanol imports**.

**3. Demand destruction has already happened, and in Japan most of it is supply-constrained
rather than price-induced.** Japanese refinery utilisation fell to 73.3%, naphtha crackers cut
runs, and force majeures were declared at named plants (Shell, CNOOC, Wanhua, Mitsubishi
Chemical). That is **feedstock unavailable at any price** — no subsidy fixes it. The
price-induced side is narrower, and in the data is essentially one phenomenon: Japan's
gas-to-coal switching in power.

This is a **Japan finding, and should not be read as a Japan-and-China one.** China has *no*
quantified, realised, price-induced observation in the dataset: its entries are a full-year
forecast and one low-confidence directional note. That is an absence of evidence, not evidence
of absence. China's import collapse is also classified in the data as a *hybrid* —
supply-constrained plus a price-induced buying strike — not purely supply-constrained. And one
widely-cited datapoint should *not* be attributed to the war at all: China's 2026 road-fuel
decline is majority-structural EV substitution.

**4. The macro damage so far is real but contained.** Japan's Q2 2026 GDP grew just **+1.1%**
annualised, with **private consumption contributing zero** — and the positive contribution came
from net trade, i.e. growth held up on a *shrinking import bill*, not domestic strength. China's
Q2 came in at **+4.3% YoY**, its weakest since Q4 2022 and below Beijing's own target floor.
Neither is a collapse.

**5. Inflation has been suppressed, not avoided — and the wedge shows where it is stored.**
Japan's core CPI was **1.8%** in July, still *below* the BOJ's 2% target seven months into the
largest oil shock on record. Meanwhile producer prices ran **+7.6%** and import prices **+24.8%**.
China shows the same shape: CPI +0.8% against PPI +3.8%. That producer–consumer wedge is the
shock sitting in corporate margins and on the government's balance sheet, waiting. Japan's energy
subsidies alone are holding roughly **1.0pp off headline CPI**.

**6. The reserves are draining fast, but not toward an LNG cliff.** Japan's total oil stocks fell
from 458mn bbl (248 days) in January to **390mn bbl (179 days) by 30 April** — a 70–100mn bbl
draw, the largest in the country's history, at roughly 0.75–1.1 mb/d. That is the real depletion
story, and it is a crude story.

**This revision corrects the previous version's LNG claim.** Japan's utility LNG stock is ~2.19mn
tonnes, which METI puts at **about 12 days of use** — but that is 12 days of *total* consumption,
not 12 days of cover against the shortfall. Only **~11% of Japan's LNG transits Hormuz**, so the
maximum volume at risk is ~7.3mt/yr. Modelling the balance explicitly, even with **zero**
re-sourcing and **zero** fuel switching, the stock covers that gap for **about 110 days** — and with
plausible re-sourcing and the gas-to-coal switching already observed, the volume gap closes
entirely. Japan's LNG stocks were in fact **12% above the five-year average and rising**, METI
reports **no requests for emergency supply**, and a new Strategic Buffer LNG programme began
buying a cargo a month in January. **The LNG shock is transmitting as price (JKM +118% y/y), not
as volume.** The binding *physical* constraint is naphtha and petrochemical feedstock, where
crackers were cutting runs from March.

**The policy trap.** Japan and China have both chosen to suppress the price signal — Japan through
a ¥26.2/L wholesaler subsidy burning ~¥600bn a month, China through the NDRC pass-through cap that
has forced refiners to absorb losses (Sinopec: ~¥9.2bn in Q1). This protects households and CPI.
It also **prevents demand from adjusting**, which keeps physical consumption high and drains the
reserves faster. Subsidy converts an inflation problem into an inventory problem — and inventory
is the thing that cannot be refinanced.

---

## 1 · How large is the supply disruption?

| Flow | Pre-war | Current | Change |
|---|---|---|---|
| Hormuz crude + liquids transit | 21.6 mb/d (4Q25) | 4.9 mb/d (2Q26) | **−77%** |
| Gulf crude exports (incl. bypass) | ~20–24 mb/d | 13–15.5 mb/d | −33% to −50% [^a] |
| Hormuz vessel transits | ~125/day | 7/day (09-09) | −94% |
| Qatar LNG cargoes (H1) | 509 | 18 | **−96%** |
| Qatar global LNG exports (Jan–Jul) | 48.2 Mt | 17.2 Mt | −64% |
| Qatar → China LNG (Jan–Jul) | 11.0 Mt | 4.7 Mt | −58% |
| Gulf diesel/gasoil net exports | — | 390 kb/d (Aug) | ~¼ of pre-war |

[^a]: This range is not the min/max of the two cells beside it — it blends the IEA's and
Kpler's own internally-paired baseline/current estimates. Subtracting the displayed endpoints
gives −23% to −46% instead.

**Bypass capacity is the swing factor, and it just got worse.** The Saudi East–West pipeline
(7 mb/d nameplate, ~4–5 mb/d actual) **shut on 2026-09-11** after drone strikes from Iraqi
territory. Satellite imagery confirms the pumping station was destroyed and the damaged section
must be dug up and replaced; the industry estimate is five to six weeks, with partial operation
possibly sooner. This was the previous revision's highest-value open question; it is now answered,
and the answer is worse than "precautionary shutdown" implied.
UAE's Habshan–Fujairah line is already maxed at 1.82 mb/d, carrying 80% of UAE loadings against
30% pre-war — there is no headroom left there. Iraq–Turkey moves 170–200 kb/d against 1.5 mb/d of
nameplate.

**Prices.** Brent $71 → $104.61 (09-11), having peaked at ~$118. JKM LNG roughly doubled to
$24.8/mmbtu. But the most violent moves are in the plumbing, not the commodity: **VLCC freight
reached $759,969/day**, and war-risk insurance went from 0.125% of hull value to **7.5–10%** — a
60-to-80-fold increase that is itself a tax on every delivered barrel.

**Direction of travel: tightening.** June–August brought a partial recovery; September reversed
it — pipeline shutdown (09-11), a tanker attack near Qeshm (09-13), and talks postponed with no
accord.

## 2 · How reliant are Japan and China?

| | Japan | China |
|---|---|---|
| Crude import dependence | 97% (2022 vintage, `est`) | ~64% (4.3 mb/d domestic) |
| Pre-war Gulf/Hormuz share of crude | 94–95% | 36.1% |
| Supplier concentration (HHI) | ~3,626 (UAE 44% + Saudi 40%) | no supplier >18% |
| Gulf share after substitution | 59.3% (Jul 2026) | — |
| Gas in power generation | 31–34% | 2.9% |
| Nuclear available | 15 of 32 reactors | — |
| Overland pipeline options | **none** | ESPO + Power of Siberia |

**The asymmetry is structural.** Japan's exposure is broad and physical: no pipelines, refineries
configured for Gulf medium-sour crude with a historical 10–20% non-ME blending ceiling (pushed to
an estimated 30–50% under duress, at a cost in yield and margin), and a power system where gas
carries a third of generation while half the nuclear fleet remains offline. Japan did substitute
hard and fast — cutting the Gulf share from 94% to 59% in four months — but April ME import
volumes hit their **lowest level since records began in 1979**.

China's exposure is narrow and sharp. Its power sector is barely touched (gas is 2.9% of
generation; coal self-sufficiency exceeds 84%). Its vulnerability is petrochemical feedstock:
**methanol, 60.4% Iranian-sourced**, and sulphur at 45–56% Middle East. These are small line items
that gate large downstream industries.

## 3 · What has the impact been, and is demand already destroyed?

### Realised — not forecast

| | Japan | China |
|---|---|---|
| GDP | Q1 +1.8%, **Q2 +1.1%** (QoQ ann.) | Q1 +5.0%, **Q2 +4.3%** YoY |
| Consumer prices | core CPI **1.8%** (Jul) | CPI **0.8%** (Aug) |
| Producer prices | CGPI **+7.6%** (Aug) | PPI **+3.8%** (Aug) |
| Import prices | **+24.8%** (Aug) | — |

Japan's Q2 print is the most informative single datapoint in the study: growth decelerated
sharply, private consumption contributed **zero**, and what positive contribution there was came
from net trade — exports up, imports down. Growth was flattered by the *collapse in the import
bill*, which is a symptom of the shock, not resilience to it. China's Q2 undershot its own target
band for the first time this cycle.

### Demand destruction: yes, and mostly involuntary

**Supply-constrained curtailment** (feedstock unavailable at any price — subsidy cannot fix this):
- Japanese refinery utilisation down to **73.3%**
- Naphtha crackers cutting runs from March–May, on stocks measured in weeks
- Force majeure at named plants: Shell, CNOOC, Wanhua, Mitsubishi Chemical

**Price-induced destruction** (available, but uneconomic — this is what subsidy suppresses):
- Japan's gas-to-coal switching in power generation

**Explicitly not war-related** — flagged because commentary routinely conflates it: China's
forecast 2026 road-fuel decline (Sinopec, −8.9%) is **majority-structural EV substitution**.
China's Jan–Feb steel and March cement falls pre-date or are unrelated to the war.

The balance matters enormously for policy. Most of the destroyed demand was destroyed by
*physical unavailability*. Subsidies do nothing about that; they only suppress the second,
smaller category — while accelerating the depletion of the reserves that are holding the first
category at bay.

## 4 · What have governments done, and will it last?

| Measure | Country | Scale | Continuation |
|---|---|---|---|
| Provisional fuel tax abolition | JP | ~¥1.5tn/yr revenue | **0.95** — enacted, permanent |
| Fuel Oil Price Stabilization Fund | JP | ~¥2tn fund, ~¥600bn/mo burn, ¥26.2/L | **0.85** |
| NDRC partial pass-through cap | CN | routine at every 10-day window | **0.90** |

Japan's subsidy is **fiscally load-bearing and escalating** — the benchmark went ¥5 → ¥25 →
¥26.2/L, and the fund has already required a ¥3.1tn replenishment against a ~¥600bn monthly burn.
The aggregate energy-subsidy effect is worth about **−1.0pp on headline CPI**. China's mechanism
differs in who pays: the NDRC cap (whose $130/bbl freeze clause has **not** been triggered) pushes
the cost onto refiner margins — Sinopec booked a ~¥9.2bn loss in Q1.

**The BOJ is tightening into a supply shock**, with markets pricing ~88% odds of a move to 1.25%
— explicitly to stop an energy shock un-anchoring wage-price expectations, rather than looking
through it as a one-off. That is a materially different reaction function from the 2022 episode
and raises the cost of the fiscal support running alongside it.

### Why continuation is the problem, not the solution

Both regimes suppress the retail price signal. The consequence is mechanical: demand does not
adjust, physical consumption stays high, and the shortfall is met from reserves instead of from
conservation. Japan's stockpile fell 254 → 214 days while CPI stayed below target; China's
refiners absorbed losses rather than passing prices through. **In both cases the shock was moved
off the price index and onto an inventory or a balance sheet.** Neither is inexhaustible, and
withdrawal gets harder the longer it runs — Japan's fuel-tax cut is now permanent law.

## 5 · The reserves and the runway

| | Japan | China |
|---|---|---|
| Total stocks | 248 days / ~458mn bbl (Jan 2026) | ~1,400mn bbl (360 govt + 1,000 commercial) |
| Usable cushion | ~270mn bbl (April basis) | ~750mn bbl (before SPR) |
| Already mobilised | 115–125mn bbl (Mar–May) | 7.14 mb/d gap bridged from stock (May) |
| Private obligation | cut **70 → 55 days** | — |
| Crude runway (full closure) | **28–118 weeks** | **15 weeks** at May draw; ~2 years at 1 mb/d |
| Total stocks, latest | **390mn bbl / 179 days** (30 Apr) | — |
| **LNG stock** | **2.19mn t = ~12 days of total use** | not published |
| LNG at risk via Hormuz | ~7.3mt/yr (11% of imports) | ~22mt/yr (30%) |
| **LNG cover against that gap** | **~110 days** even with no switching | n/a |

**Naphtha is the binding physical constraint, not LNG — and the previous revision got this
wrong.** LNG tanks are working inventory rather than a reserve, and 12 days sounds alarming. But
days-of-total-consumption is the wrong denominator: what matters is cover against the *lost*
volume, and only ~11% of Japan's LNG comes through Hormuz. Against a maximum ~7.3mt/yr loss, the
stock lasts about 110 days even assuming no re-sourcing and no fuel switching at all — and Japan
has demonstrably done both. In the model as parameterised the LNG gap is in fact **zero in all four
scenarios**, because the assumed re-sourcing capacity alone exceeds the worst-case loss; the
110-day figure is a bounding hand-calculation at zero substitution, not a scenario output. Consistent with that, stocks sat 12% above the five-year average, rose
10% into March, and METI has received no emergency-supply requests.

What genuinely binds is petrochemical feedstock, and this revision now models it. Japan's
**ethylene cracker rate hit a record-low 67.3% in April** (−11.3pp y/y, from a then-record 68.8%
in March), with **ethylene output down 38.8% y/y**. Private naphtha inventory is **20 days** —
far thinner than the crude stockpile — about 40% of naphtha is imported directly from the Gulf,
and unlike LNG there is no national reserve and no fuel-switching escape.

**But the same denominator discipline applies here too, and it changes the conclusion's shape.**
Twenty days is cover against total throughput; against the ~13–16% of supply actually unmet after
re-sourcing, the stock lasts **123–150 days**, and the polymer buffer behind it (PE and PP
inventories covering three-plus months of demand) stretches to **550–670 days**. So the
petrochemical damage is **not an approaching cliff — it is continuous output loss happening now**:
crackers running 12–15pp below normal, indefinitely, with the loss showing up as forgone
production and margin rather than as an exhaustion date. Japan is also importing **~30% more
Chinese chemicals**, at six-year highs, which relocates the value added rather than replacing it.

The LNG shock, by contrast, is a *price* shock (JKM +118% y/y) — a terms-of-trade problem, not a
rationing one.

Two caveats on the numbers above, both material. Japan's 28–118 week range is wide because **no
Japanese crude-import or refinery-run figure after 2026-05-09 could be sourced** — that single
gap drives the spread. And China publishes no reserve data at all, so every Chinese figure here
rests on commercial estimates.

The **IEA's 400mn bbl collective release** (2026-03-11, the largest ever) is a one-off buffer, not
a flow. No running total of what remains was locatable.

### When the runway ends

The rationing order is consistent across both economies and politically predictable: petrochemical
feedstock first, then industrial fuel, then power, then transport — with residential and
agricultural supply protected longest. Japan's legal trigger is the Petroleum Supply and Demand
Optimization Act; **no evidence was found that it has been invoked**, which is not the same as
confirmation that it has not.

## 6 · Scenarios

Model results, not forecasts: they state what the stated assumptions imply. Run them yourself in
the tracker.

| Scenario | Transit | Brent | Japan GDP / CPI | China GDP / CPI |
|---|---|---|---|---|
| De-escalation | 50% | $80 | +0.01pp / −0.02pp | +0.07pp / +0.02pp |
| **Current grind (base)** | 7% | $100 | **−1.81pp / +2.80pp** | **−0.25pp / +1.11pp** |
| Full closure | 2% | $145 | −2.97pp / +7.48pp | −0.62pp / +3.09pp |
| Full closure, support withdrawn | 2% | $145 | −2.82pp / +8.48pp | −0.70pp / +3.49pp |

**These are materially smaller than the previous revision's GDP figures, and that is a
correction, not a change of view.** The rationing coefficient was cut from 0.25 to 0.12pp of GDP
per 1% forced cut in oil use after checking against published benchmarks: the IMF's April 2026
adverse scenario puts the GDP loss for the region's major economies at **almost 1pp**, and
GlobalData puts China at **−0.15 to −0.2pp per sustained $10/bbl**. At 0.25 the model produced a
Japan hit three to four times the IMF figure. The price channel now yields **−0.76pp for Japan** (inside the −0.29 to −1.45pp implied by
GlobalData's importer range) and **−0.46pp for China** (inside the −0.44 to −0.58pp implied by its
China-specific figure). An earlier draft quoted −0.85 and −0.5 and claimed both passed; the second
audit found China's actual output was −0.29pp, *outside* its range, so China's multiplier was
raised to deliver the calibration the parameter file claimed. Econbrowser/IMF compute Korea's
transfer by the identical method. The CPI channel was also split
by fuel, because gas reaches households through regulated, lagged tariffs: Japan's base case now
prints **+2.80pp**, matching the realised position (core CPI 1.8% with subsidies holding ~1.0pp
off, so ~2.8% ex-subsidy).

Two results are worth dwelling on.

**Withdrawing price support improves GDP while worsening CPI.** For Japan under full closure,
GDP goes from −2.97pp to −2.82pp while CPI rises from +7.48 to +8.48. Restoring the price signal
roughly doubles voluntary conservation and cuts rationed demand from 392 to 296 kb/d.
Because rationing destroys *output* while higher prices merely *transfer income*, trading
inflation for availability is GDP-positive in this model. That result is a direct consequence of
the assumed rationing cost and should be stress-tested, not taken as settled.

**For Japan, subsidy withdrawal does not extend the runway — but treat this as an illustration,
not a finding.** China's runway lengthens (71 → 90 weeks) when support lapses, while Japan's
stays pinned at 42.9 weeks in every variant, because Japan's draw is capped by **deliverability**
rather than by stock size or policy.

The mechanism is worth understanding: once the rate at which reserves can physically be moved
is what binds, conservation changes *who bears* the shortfall, not how long the reserves last.
But the number is close to tautological. Japan's 42.9 weeks is just
270mn bbl ÷ 900 kb/d ÷ 7, and while the 900 kb/d ceiling is now calibrated on the observed
0.75–1.1 mb/d draw rather than assumed outright, no engineering maximum is published. Whenever the physical gap exceeds that cap the
runway stops varying with scenario severity *by construction*. Change the assumed cap and this
result changes with it. It belongs in a sensitivity discussion, and it is reported here as one.

**The engine now models both LNG and naphtha physically.** The first revision's physical channels
ran on crude alone. Both product balances now exist: LNG (loss, re-sourcing, fuel switching, stock
draw, runway) and naphtha (loss, re-sourcing, then straight into the cracker operating rate, with
stock and downstream-polymer cover). Building them is what exposed both denominator errors
corrected above.

**Two caveats on the naphtha channel, both raised by the second audit.**

First, exposure is larger than the directly-imported share alone. Japan imports ~40% of its naphtha
from the Gulf *and* domestic refining supplies roughly another 40% from crude that was 95%
ME-sourced — a structural exposure near **78%**, not 40%. The model now carries both parts, but the
refinery-derived slice is scaled by the *realised* refinery run reduction rather than by Hormuz
throughput, because the crude channel already determines how much crude arrives; applying
throughput to both would double-count the same missing barrels. Correcting this raises gross
naphtha loss from 36% to **41–44% of supply**, not to 78% — the difference being precisely the
crude Japan successfully re-sourced.

Second, the channel is **under-identified**. One observation (April's 67.3% cracker rate) cannot
separate substitution capacity from how strongly an unmet gap passes into the operating rate. The
pass-through is therefore fixed at 1.0 — the Leontief bound, since a cracker cannot process
feedstock it does not have — and substitution calibrated to 28% of supply. The level fits April by
construction; treat the scenario *variation* as illustrative. China's naphtha exposure could not be
sourced, so no Chinese naphtha result is produced rather than an invented one.

**A caution on the CPI column.** These are sustained-shock scenarios measured against a no-shock
baseline, not nowcasts. The base case shows Japanese CPI +2.49pp while realised core CPI is 1.8%
and below target. There is no contradiction — the subsidy is currently holding ~1.0pp off, and the
scenario prices a shock sustained for longer than the realised data covers — but the two numbers
answer different questions and should not be read side by side without that caveat.

---

## What changed in this revision

| Item | Previous version | Now |
|---|---|---|
| **Japan's LNG cover** | "~2–3 weeks, roughly a fortnight of buffer" | **~110 days against the Hormuz-attributable gap.** 12 days is total-consumption cover; only 11% of LNG transits Hormuz |
| **The binding physical constraint** | LNG and naphtha | **Naphtha.** LNG is transmitting as price, not volume |
| **East–West pipeline** | Open question | **Answered:** pumping station destroyed, 5–6 week repair estimate |
| **China Aug imports** | Three-way conflict (7.2 / 8.9 / 11.65 mb/d), unresolved | **Resolved: 37.93 Mt = 8.93 mb/d**, official GACC customs |
| **Japan reserves** | 458mn bbl / 248 days (Jan) | **390mn bbl / 179 days (30 Apr)**; 70–100mn bbl drawn, largest ever |
| **Japan GDP, base case** | −3.01pp | **−1.81pp**, after recalibrating against IMF and GlobalData |
| **Japan CPI, base case** | +2.49pp (Brent-driven only) | **+2.80pp**, split by fuel and matched to the realised print |
| **Deliverability ceiling** | Pure assumption | **Calibrated** on the observed 0.75–1.1 mb/d draw |
| **Naphtha** | Not modelled at all | **Modelled:** cracker rate 67.3% (record low), 20-day stock = 123–150 days against the actual gap |
| **Rationing coefficient** | Unanchored assumption | **Bracketed** by the electricity-curtailment literature above and the IMF benchmark below |
| **Sourced parameters** | 15 of 43 | **37 of 72** |

Two of those are corrections to claims this report previously made with more confidence than the
evidence supported. The LNG one is the more serious: it inverted the report's central judgement
about which constraint binds, and it was a denominator error of exactly the kind the project's own
evidence standards warn about — quoting days of cover without stating what they are days *of*.

## What the second audit found

The revision was itself independently audited (`docs/REVIEW2.md`). It found seven material
problems, all verified and all now fixed:

| Finding | Status |
|---|---|
| The v1 review table still said "LNG not modelled", contradicting this same document | **Fixed** — it had not been updated when the channel was added |
| Naphtha exposure used the directly-imported share only, omitting refinery-derived naphtha | **Fixed** — both parts now modelled; gross loss 36% → 41–44% |
| The price-channel cross-check did not reproduce; China's output was *outside* its cited range | **Fixed** — China's multiplier raised so the calibration is real, not claimed |
| The LNG gap is zero in all four scenarios; "112 days" was a hand calc, and recomputes to ~110 | **Fixed** — restated as a bounding calculation, and the zero result disclosed |
| Sections 5–6 still cited 247mn bbl / 39.2 weeks after the parameter was updated to 270mn | **Fixed** — now 270mn bbl / 42.9 weeks |
| `renderParams()` never learned the new parameter groups, so ~18 new tags were invisible | **Fixed** — a repeat of the v1 finding; tags rendered went 47 → 73 |
| "China conflict resolved" overstated: the contradicting rows remained in the repo | **Fixed** — superseded rows now annotated in place |

Two of the audit's points I could only **disclose**, not resolve:

- **Weak sources on load-bearing figures.** Japan's naphtha stock (20 days) and polymer buffer
  (3 months) come from a trade site, and Japan's oil demand from an aggregator rather than METI or
  the IEA. All three now carry `est` rather than `hard`, but they still drive results and deserve a
  primary-source check.
- **The rationing coefficient's anchor is loose, not tight.** Japan's base case (−1.81pp) is about
  1.8× the IMF's ~1pp regional benchmark and full closure roughly 3×. Some divergence is expected —
  the IMF's adverse case is a price scenario with no rationing regime, and full closure is more
  severe than it — but the benchmark constrains the order of magnitude, not the level. Treat these
  GDP figures as bounded above by that comparison rather than validated by it.

Independently confirmed as genuinely fixed from the first audit: the crude substitution arithmetic,
the CPI-suppression mistag, the terms-of-trade double-charge, the Tokyo/national CPI conflation, and
Python/JS port parity — the last verified line by line, including every new channel.

## What would change the picture

In rough order of value:

1. **Whether the East–West pipeline restart holds.** The repair estimate is 5–6 weeks from 09-11,
   so mid-to-late October is the test. A confirmed restart is the single most bullish thing that
   could happen to Asian supply.
2. **Japanese crude imports and refinery runs after 2026-05-09.** Still missing, and still the
   reason the crude runway carries a wide range.
3. **Cracker rates after April 2026.** The naphtha channel is calibrated on one month; a second
   observation would turn a fit into a test.
4. **Any hard read on Chinese reserve levels**, and China's naphtha exposure — both still absent.
5. **A Japan-specific GDP elasticity per $10/bbl.** The model borrows a major-importer midpoint
   because no Japan figure could be sourced.

## Independent review

This study was audited by an independent reviewer with no stake in its conclusions
(`docs/REVIEW.md`). The review's verdict was that the study is **not sound enough to act on as
originally presented**, and it was right on every checkable point. Its findings have been
applied rather than filed:

| Finding | Status |
|---|---|
| Demand-destruction balance overstated as a Japan+China finding | **Fixed** — now scoped to Japan; China's absence of evidence stated |
| Three irreconcilable figures for Chinese Aug-2026 imports, all tagged `hard` | **Fixed** — conflict disclosed; the derived parameter downgraded to `est` |
| Report claimed the tracker tags assumptions; it did not | **Fixed** — the tracker's parameter table now renders every provenance tag |
| "Pinned runway" presented as a finding, not an artifact of one assumption | **Fixed** — reframed as a sensitivity illustration at the point of claim |
| `JP.policy.cpi_suppression_pp` mistagged `hard` | **Fixed** — retagged `est`; the incorrect BOJ attribution removed |
| A `calc` parameter that did not reproduce from its formula | **Fixed** — 826 → 821 kb/d |
| Terms-of-trade and rationing double-charged the same missing barrels | **Fixed** — the import bill is now struck on delivered volume only |
| LNG absent from the model's physical channels | **Fixed in the second pass** — full LNG balance now modelled |

Two findings were disclosed rather than repaired at the time, because repairing them would have
meant inventing parameters the study lacked. **Both were subsequently fixed in the second pass:**
the model is no longer crude-only (LNG and naphtha balances were added) and the CPI channel is no
longer Brent-driven (it is split by fuel). That revision was then independently audited in turn —
see `docs/REVIEW2.md` and `## What the second audit found`.

## Limitations

This study was assembled under two binding constraints, and its conclusions should be weighted
accordingly.

- **Coverage is uneven across time.** The first pass ran out of search budget mid-research; this
  revision closed the highest-value gaps (the pipeline, Chinese customs data, Japanese reserve and
  LNG levels, published GDP elasticities) but several series still stop in May–July 2026. Every
  remaining gap is marked `NA` in the data rather than filled by inference.
- **37 of 72 model parameters are now sourced; 35 remain assumptions.** The GDP and CPI channels
  are calibrated against published benchmarks (IMF, GlobalData) and, for Japanese CPI, against the
  realised print. The deliverability ceiling is calibrated on the observed draw rate. What is still
  assumed and still matters: the LNG substitution and fuel-switching capacities, CPI energy
  weights, China's naphtha exposure, and a Japan-specific GDP elasticity. The rationing
  coefficient is no longer unanchored — the electricity-curtailment literature bounds it from
  above (0.2–0.4 per 1% for a *less* substitutable input) and the IMF scenario from below — but it
  is still a calibration rather than a measurement. All are listed under `assumptions` in
  `analysis/parameters.json` and tagged in the tracker's parameter table.
- **Sourcing quality is mixed.** 389 observations carry a source URL and a quality label
  (`hard` / `est` / `calc`); 2% are unlabelled. Some figures come from aggregators rather than
  primary statistical agencies and are flagged as such in the workstream notes. Where sources
  conflict — current Hormuz throughput most of all, where estimates range from 3% to 7.4% of
  pre-war — the range is reported rather than a false point estimate.

The reviewer's overall verdict deserves to stand alongside the conclusions rather than be
buried: the narrative's confidence repeatedly outran its evidentiary base. The corrections above
address the specific instances, but a reader should treat the *direction* of these findings as
well established and the *magnitudes* as illustrative throughout.

A dissenting note worth recording: one analyst view holds that Chinese stocks are already
depleting toward operational minimums, with Q3 2026 — now — as the base case. This report can
neither confirm nor refute that with the available data, and it sits in tension with China's own
partial easing of fuel-export curbs in July 2026.
