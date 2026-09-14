# The Hormuz shock and the Asian economies

### Economic impact of the 2026 Iran–US conflict energy disruption on Japan and China

**As of 2026-09-14 — day 198 of the conflict** (2026-02-28 start).

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
cushion is now eroding. The Saudi East–West pipeline, which had been rerouting ~5 mb/d, **shut on
2026-09-11**; talks on shipping protection collapsed on 09-13. LNG is the harder hit: Qatar's H1
cargo count fell from 509 to 18 (−96%).

**2. Japan is more exposed structurally; China is more exposed in narrow chokepoints.** Japan
imports 97% of its crude and drew 94–95% of it from the Gulf pre-war, with a supplier HHI near
3,600 — one of the most concentrated energy dependencies in the developed world, and it has no
pipeline alternative. China sourced 36% via Hormuz, produces ~4.3 mb/d domestically, and takes
Russian barrels overland. But China holds the most concentrated single dependency found anywhere
in this study: **Iran supplied 60.4% of its methanol imports**.

**3. Demand destruction has already happened — and most of it is supply-constrained, not
price-induced.** This distinction is the analytical core of the report. Japanese refinery
utilisation fell to 73.3%, naphtha crackers cut runs, and force majeures were declared at named
plants (Shell, CNOOC, Wanhua, Mitsubishi Chemical). That is **feedstock unavailable at any
price** — no subsidy fixes it. Genuinely price-induced destruction is narrower: Japan's
gas-to-coal switching in power is the clearest case. And one widely-cited datapoint should *not*
be attributed to the war: China's 2026 road-fuel decline is majority-structural EV substitution.

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

**6. The runway is long in crude and short in everything else.** Japan's usable crude cushion of
~247mn bbl buys 28–118 weeks under full closure. But crude is not what binds. **Japan's utility
LNG inventory is ~2.3mn tonnes — roughly two to three weeks of use, and LNG cannot be stockpiled
at scale.** Naphtha crackers were cutting output in March–May, long before crude reserves would
bind. China bridged a **7.14 mb/d gap** entirely from stocks in May 2026 — the largest national
stockpile deployment on record — which at that rate would exhaust its usable commercial cushion in
about 15 weeks.

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
| Gulf crude exports (incl. bypass) | ~20–24 mb/d | 13–15.5 mb/d | −33% to −50% |
| Hormuz vessel transits | ~125/day | 7/day (09-09) | −94% |
| Qatar LNG cargoes (H1) | 509 | 18 | **−96%** |
| Qatar global LNG exports (Jan–Jul) | 48.2 Mt | 17.2 Mt | −64% |
| Qatar → China LNG (Jan–Jul) | 11.0 Mt | 4.7 Mt | −58% |
| Gulf diesel/gasoil net exports | — | 390 kb/d (Aug) | ~¼ of pre-war |

**Bypass capacity is the swing factor, and it just got worse.** The Saudi East–West pipeline
(7 mb/d nameplate) was moving ~5 mb/d until it **shut on 2026-09-11** after drone strikes; its
status as of this writing is unconfirmed and is the highest-value open question in the dataset.
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
| Crude import dependence | 97% | ~64% (4.3 mb/d domestic) |
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
| Usable cushion | ~247mn bbl | ~750mn bbl (before SPR) |
| Already mobilised | 115–125mn bbl (Mar–May) | 7.14 mb/d gap bridged from stock (May) |
| Private obligation | cut **70 → 55 days** | — |
| Crude runway (full closure) | **28–118 weeks** | **15 weeks** at May draw; ~2 years at 1 mb/d |
| **LNG** | **~2.3mn t ≈ 2–3 weeks** | — |

**Crude is not the binding constraint. LNG and naphtha are.** Japan's crude cover is measured in
quarters; its LNG cover is measured in *weeks*, because LNG cannot be stockpiled at scale — the
tanks are working inventory, not a reserve. So far the LNG strain has shown up as **price**
(JKM +118% y/y) rather than volume, which is what a market clearing on willingness-to-pay looks
like. If it becomes a volume constraint, Japan has roughly a fortnight of buffer and no
equivalent of an SPR to open.

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
| De-escalation | 50% | $80 | −0.00pp / +0.04pp | +0.06pp / +0.03pp |
| **Current grind (base)** | 7% | $100 | **−3.01pp / +2.49pp** | **−0.38pp / +1.06pp** |
| Full closure | 2% | $145 | −4.54pp / +7.50pp | −0.74pp / +3.12pp |
| Full closure, support withdrawn | 2% | $145 | −3.96pp / +8.50pp | −0.74pp / +3.52pp |

Two results are worth dwelling on.

**Withdrawing price support improves GDP while worsening CPI.** For Japan under full closure,
GDP goes from −4.54pp to −3.96pp while CPI rises from +7.50 to +8.50. Restoring the price signal
roughly doubles voluntary conservation (69 → 172 kb/d) and cuts rationed demand (382 → 279 kb/d).
Because rationing destroys *output* while higher prices merely *transfer income*, trading
inflation for availability is GDP-positive in this model. That result is a direct consequence of
the assumed rationing cost and should be stress-tested, not taken as settled.

**For Japan, subsidy withdrawal does not extend the runway.** China's runway lengthens (71 → 90
weeks) when support lapses, but Japan's stays pinned at 39 weeks in every variant — because
Japan's draw is capped by **deliverability**, not by stock size or by policy. This is the most
counter-intuitive output of the model and the most operationally important: once the physical
rate at which reserves can be moved is the binding constraint, conservation changes who bears
the shortfall, not how long the reserves last.

**A caution on the CPI column.** These are sustained-shock scenarios measured against a no-shock
baseline, not nowcasts. The base case shows Japanese CPI +2.49pp while realised core CPI is 1.8%
and below target. There is no contradiction — the subsidy is currently holding ~1.0pp off, and the
scenario prices a shock sustained for longer than the realised data covers — but the two numbers
answer different questions and should not be read side by side without that caveat.

---

## What would change the picture

In rough order of value:

1. **The operating status of the Saudi East–West pipeline.** It moves ~5 mb/d and went down on
   09-11. Nothing else in the dataset has this leverage.
2. **Japanese crude imports and refinery runs after 2026-05-09.** One missing series is
   responsible for a 28–118 week spread in the runway.
3. **Japan's weekly utility LNG stock.** The genuinely binding constraint, and it is published.
4. **Any hard read on Chinese reserve levels**, which are currently estimated end to end.

## Limitations

This study was assembled under two binding constraints, and its conclusions should be weighted
accordingly.

- **The session's web-search budget was exhausted mid-research.** Coverage is therefore uneven:
  the last fortnight before the as-of date is thinner than the rest, and several series stop in
  May–July 2026. Every such gap is marked `NA` in the data rather than filled by inference.
- **Key model parameters could not be sourced.** Per-$10/bbl GDP elasticities were not locatable
  for either economy, so the GDP channel runs off a *measured* income transfer times an *assumed*
  multiplier. Reserve deliverability ceilings — which bind the Japanese runway in most scenarios —
  are unpublished and assumed. All such parameters are listed in `analysis/parameters.json` under
  `assumptions` and are tagged in the tracker's parameter table.
- **Sourcing quality is mixed.** 389 observations carry a source URL and a quality label
  (`hard` / `est` / `calc`); 2% are unlabelled. Some figures come from aggregators rather than
  primary statistical agencies and are flagged as such in the workstream notes. Where sources
  conflict — current Hormuz throughput most of all, where estimates range from 3% to 7.4% of
  pre-war — the range is reported rather than a false point estimate.

A dissenting note worth recording: one analyst view holds that Chinese stocks are already
depleting toward operational minimums, with Q3 2026 — now — as the base case. This report can
neither confirm nor refute that with the available data, and it sits in tension with China's own
partial easing of fuel-export curbs in July 2026.
