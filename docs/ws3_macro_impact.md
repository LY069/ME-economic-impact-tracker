# WS3 — Realised macro impact on Japan and China, and demand destruction

**As-of: 2026-09-14.** Prepared per `docs/00_shared_brief.md`. Core discipline of this
workstream: keep **realised, published data** strictly separate from **forecasts and
scenario numbers**, and for every demand-destruction observation state explicitly
whether it is **supply-constrained curtailment** (feedstock/product physically
unavailable) or **price-induced demand destruction** (available but uneconomic).
Full sourced data underlying this note are in:
- `data/raw/ws3_macro.csv` (97 rows, long format)
- `data/raw/ws3_demand_destruction.csv` (24 rows)
- `data/raw/ws3_elasticities.csv` (14 rows)

Search was WebSearch-only (WebFetch blocked); several BOJ/Cabinet Office/IMF primary
PDFs could only be characterised via secondary reporting of their headline numbers,
not read directly. This is flagged wherever it matters.

## Key figures

### Growth — realised prints (the priority datapoints)

| Country | Metric | Period | Value | vs. prior | Quality | Source date |
|---|---|---|---|---|---|---|
| JP | Real GDP, QoQ annualized | Q1 2026 (2nd release) | **+1.8%** | revised down from +2.1% flash | hard | 2026-06-08 |
| JP | Real GDP, QoQ annualized | **Q2 2026 (flash)** | **+1.1%** | down from Q1's (revised) 1.9%; missed +2.0% consensus | hard | 2026-08-17 |
| CN | Real GDP, YoY | Q1 2026 | **+5.0%** | up from +4.5% Q4 2025 | hard | 2026-04-16 |
| CN | Real GDP, YoY | **Q2 2026** | **+4.3%** | down from Q1's 5.0%; weakest since Q4 2022; below the 4.5–5.0% annual target floor | hard | 2026-07-17 |

Japan's Q2 print is the single most important realised datapoint in this workstream:
growth decelerated sharply from Q1, **private consumption made zero contribution**,
and the positive contribution came from net trade (exports up, imports down) — i.e.
growth held up on the back of a shrinking import bill, not domestic demand strength.
China's Q2 print shows a parallel deceleration, undershooting Beijing's own target
range for the first time this cycle.

### Prices — realised prints

| Country | Series | Baseline (pre-war, Jan/Feb 2026) | Latest realised print | Quality |
|---|---|---|---|---|
| JP | Core CPI YoY (ex fresh food) | 2.0% (Jan) / 1.6% (Feb) | **1.8%** (Jul 2026) | hard |
| JP | Core-core CPI YoY (ex food & energy) | 2.5% (Feb) | **1.9%** (Jul 2026, fastest in 3 months) | hard |
| JP | CGPI (producer prices) YoY | NA (gap, see below) | **7.6%** (Aug 2026) | hard |
| JP | Import price index YoY | NA (gap) | **24.8%** (Aug 2026) | hard |
| CN | CPI YoY | NA precise Jan/Feb (gap) | **0.8%** (Aug 2026), up from 0.5% Jul | hard |
| CN | PPI YoY | NA precise Jan/Feb (gap) | **3.8%** (Aug 2026) | hard |

Japan's core CPI is *still below the BOJ's 2% target* seven straight months into
the shock — government fuel subsidies are visibly offsetting pass-through — while
wholesale/producer prices (CGPI +7.6% YoY, import prices +24.8% YoY) show the
shock hitting far harder upstream than downstream. China shows the same pattern in
sharper relief: PPI accelerated to +3.8% YoY in August (partly energy, partly a
separate memory-chip shortage) while CPI is still only 0.8% — a large and widening
wedge between producer and consumer inflation in both economies, consistent with
firms absorbing margin rather than passing costs through.

### Trade, industrial activity, sentiment — realised prints

| Country | Metric | Latest value | Period | Quality |
|---|---|---|---|---|
| JP | Industrial production YoY | +4.1% | Jul 2026 | hard |
| CN | Industrial production YoY | +4.5% (missed 5% forecast) | Jul 2026 | hard |
| JP | Trade balance | -¥634.5bn | Jul 2026 | hard |
| CN | Trade surplus | $119.0bn | Aug 2026 | hard |
| CN | Exports YoY (USD) | +25.0% | Aug 2026 | hard |
| CN | Imports YoY (USD) | +28.0% (value; volume unclear) | Aug 2026 | hard |
| JP | Manufacturing PMI (au Jibun/S&P) | 54.5 | Jul 2026 | hard |
| CN | Manufacturing PMI (NBS, official) | 49.8 (still contraction) | Aug 2026 | hard |
| CN | Manufacturing PMI (Caixin) | 51.5 | Aug 2026 | hard |
| CN | Retail sales YoY | +0.6% (missed 1.5% forecast) | Jul 2026 | hard |
| JP | Retail sales YoY | +2.5% | Apr 2026 (gap thereafter) | hard |
| JP | Real wages YoY | +1.6% (Jun) → +1.0% (Jul) | Jun/Jul 2026 | hard/est |

### FX

| Pair | Pre-war baseline | Latest | Change |
|---|---|---|---|
| USD/CNY | 6.91 (Feb 2026 avg) | 6.71 (2026-09-14) | Yuan **appreciated** ~2.9% — counterintuitive, flagged below |
| USD/JPY | NA — gap, Feb 2026 baseline not located | 153.49 (2026-09-11) | Yen +3.7% over the prior month but -4.0% weaker YoY |

### Demand destruction — headline volume evidence

| Observation | Baseline → current | Type |
|---|---|---|
| Japan PAJ refinery utilization | >80% → 67.7% (early Apr), recovering to 73.3% (early May) | **Supply-constrained** |
| China crude oil imports | 7.8 mb/d (May) → 6.4 mb/d (Jun, 8-yr low) → ~11.65 mb/d (Aug, near-full recovery) | **Supply-constrained**, now largely resolved (pre-dates 2026-09-11 pipeline shutdown) |
| Shandong "teapot" refinery utilization | 53.1% → 50.76% (Jun) | **Supply-constrained** |
| Japan/China ethylene crackers (named force majeures: Shell/CNOOC Huizhou, Wanhua Chemical, Mitsubishi Chemical) | Cracker utilization 80%→60% (Japan, Mar) | **Supply-constrained** |
| Qatar LNG exports | ~77Mt normal → 38.7Mt (2026 forecast) | **Supply-constrained** |
| Japan LNG imports | -7% YoY (Q2) | **Price-induced substitution** |
| Japan gas-fired power generation | -16% YoY (Jun); coal +4.6% YoY | **Price-induced substitution** |
| China 2026 gasoline/diesel demand (Sinopec forecast, NOT yet realized) | -8.7% / -11.4% (full-year forecast) | **Mixed — majority structural (EV shift), minority price-induced** |

## Narrative

### 1. Growth: a real, moderate, but not catastrophic deceleration — confirmed in hard data

**Japan.** Q1 2026 GDP grew a strong +2.1% QoQ annualized on the flash release
(2026-05-19), beating consensus, before being revised down to +1.8% on 2026-06-08
(capex was the swing factor, revised from +0.3% to -0.7% QoQ). This strength was
**pre-shock momentum** carrying through — the war started 2026-02-28, right at the
Q1 quarter boundary, so Q1 barely captures the shock. **Q2 2026 (flash, released
2026-08-17) is the first quarter to fully reflect the war**, and it shows
deceleration: +1.1% QoQ annualized, missing the +2.0% consensus, with **private
consumption contributing zero** and the entire positive contribution coming from
net trade (exports rising while imports fell — itself a symptom of the energy
shock reducing import volumes/values, not of demand strength). One secondary
aggregator source (fxstreet/tmgm) muddies the QoQ figure between 0.3% and 0.4% in
mutually inconsistent text; treat the 0.3% flash as more reliable pending a primary
Cabinet Office check.

**China.** Q1 2026 (+5.0% YoY) actually *accelerated* from Q4 2025 (+4.5%), on
strong Jan-Feb exports and fiscal support — again, largely pre-shock strength
(the war started at the very end of February). **Q2 2026 (+4.3% YoY) is the first
quarter to show the shock**, decelerating sharply, missing the 4.5% consensus, and
landing **below the bottom of Beijing's own 4.5–5.0% growth target band** — the
weakest quarter since Q4 2022. QoQ momentum also eased (0.9% vs 1.3% in Q1).

**Bottom line: both economies show a clear, dateable inflection at Q2 2026 — the
first full quarter of the war — but neither shows a collapse.** Growth decelerated,
it did not go negative. This matters for calibrating any scenario model: the
realised data through Q2 argue for a moderate drag, not a recession, as of the
last confirmed GDP print. Q3 2026 data (not yet released as of 2026-09-14) will be
the first to capture the September escalation (pipeline shutdown, vessel attack).

### 2. Prices: upstream pain, downstream restraint — the wedge is the story

In both countries, **producer/wholesale prices have moved far more than consumer
prices**, and this wedge has *widened* through the summer rather than closing:

- Japan's CGPI (corporate goods/producer prices) is running at +7.6% YoY (Aug 2026,
  near 3.5-year highs) and import prices at +24.8% YoY (compounding yen weakness with
  the energy shock), while core CPI is only +1.8% YoY and still *below* the BOJ's 2%
  target seven months into the shock. Government electricity/gas subsidies
  (¥3.50–4.50/kWh, July–September 2026, ~¥5,000/household/month) are a documented,
  quantified reason core CPI understates the underlying cost shock.
- China's PPI accelerated to +3.8% YoY in August (NBS explicitly cites Middle East
  energy costs, alongside an unrelated memory-chip shortage) while CPI is only
  +0.8% YoY. The one CPI sub-index that clearly shows the oil shock — transport
  costs — jumped from +0.4% YoY (Jul) to +2.5% YoY (Aug), a six-fold acceleration
  in one month and the cleanest single piece of realised evidence that the energy
  shock is now visibly reaching Chinese consumers via travel/fuel costs specifically,
  even as broader CPI stays subdued.

This producer-consumer wedge is consistent with firms in both countries absorbing
margin compression rather than fully passing costs through — a pattern that shows
up independently in the PMI data: China's Caixin manufacturing PMI for August 2026
shows input price inflation *accelerating* while output prices *fell* for the first
time in 2026 (the clearest hard evidence of margin squeeze in the whole dataset).

### 3. Demand destruction — the priority section

**This is the analytically central distinction the brief asks for, and the
evidence supports separating three distinct phenomena that are often conflated in
commentary:**

**(A) Genuine supply-constrained curtailment — cannot get feedstock, full stop.**
This is the dominant story in refining and petrochemicals through March–June 2026:
- Japan PAJ refinery utilization fell from >80% pre-war to 67.7% (week of 2026-04-04,
  lowest since June 2025), recovering only to 73.3% by 2026-05-09 as SPR releases
  (from 2026-03-16) and alternative crude sourcing came online. This is a textbook
  physical constraint: Japan sourced ~94% of crude from Arab Gulf nations in
  February 2026, falling to 73.9% by May as it substituted toward the US (22.4%),
  Russia, Azerbaijan and Brunei — a forced substitution, not a demand choice.
- China's crude imports collapsed from 7.8 mb/d (May) to 6.4 mb/d (June, an 8-year
  low) as Hormuz transit cratered and refiners drew down stocks rather than
  physically obtain replacement barrels fast enough — though this also had a
  price-induced buying-strike component (refiners waiting out the price spike).
  By August, imports had recovered to ~11.65 mb/d (+0.8% YoY, +4.9% MoM) — evidence
  that the supply constraint was substantially resolved by late summer, **before**
  the 2026-09-11 Saudi pipeline attack reintroduced risk.
- Petrochemicals show the clearest, most specific supply-constrained evidence with
  named entities: the Shell/CNOOC Huizhou ethylene cracker JV shut down and
  suspended polyethylene shipments indefinitely from 2026-03-05; Wanhua Chemical
  declared force majeure on TDI and MDI (key polyurethane intermediates) on
  2026-03-06; Mitsubishi Chemical cut steam-cracker output in Japan around the same
  time. Industry-wide, Japanese cracker utilization fell from ~80% to ~60% in March
  2026 as ~74% of Japan's naphtha imports normally originate in the Middle East.
  These are unambiguous force-majeure supply events, not demand choices.
- Qatar's LNG export capacity is still constrained at the source: force majeure was
  *extended into November 2026* (per a 2026-08-31 update), with 2026 export guidance
  at 38.7Mt vs a ~77Mt normal run-rate — roughly half of capacity, six months into
  the war, with no clean restart date. This is the most durable supply constraint
  identified in this workstream.

**(B) Price-induced demand destruction — available, but uneconomic, and consumers/
utilities are visibly switching away.**
This is the dominant story in Japanese power generation and, on the current
(imperfect) evidence, a meaningful share of the Chinese road-fuel story:
- Japan's LNG imports fell 7% YoY in Q2 2026 **not** because LNG was unavailable to
  Japan specifically, but because spot Asian LNG prices ran ~70% above pre-war
  levels and utilities had a substitute (coal) available. This shows up cleanly in
  the generation mix: gas-fired generation -16% YoY, coal-fired +4.6% YoY in June
  2026. A draft METI proposal to remove the 50% coal-utilization cap (not yet
  enacted as of this report) would extend this substitution further, potentially
  cutting LNG use by another 0.5 Mt/year — a **forecast**, not realised.
- China's Sinopec forecasts full-year 2026 oil demand down 8.9% YoY (gasoline -8.7%,
  diesel -11.4%) — but Sinopec's own framing is important and should not be
  flattened into a single "war caused this" number: the company explicitly states
  the high oil/fuel prices from the war **"compounded rather than created"** an
  already-underway structural shift to EVs and alternative-powertrain trucks (1.3
  Mbd of displacement attributed to technology in 2026 alone). This is a forecast
  for the full year, not a realised print, and the majority driver is structural,
  not the war. Treat any scenario-model attribution of Chinese road-fuel demand
  destruction to the oil shock as needing a haircut for this structural overlap.

**(C) Not war-related — flagged explicitly to prevent misattribution.**
Two widely-circulated Chinese heavy-industry data points predate or are largely
unrelated to the war and should not be counted as war-driven demand destruction by
other workstreams:
- China crude steel production fell 3.6% YoY in Jan-Feb 2026 — this period is
  **before** the war started (2026-02-28); the driver is the government's
  capacity-control/anti-involution industrial policy.
- China cement output fell 21% YoY in March 2026, the lowest for the period since
  2020 — the source attributes this primarily to the ongoing property-sector
  downturn, with energy-cost pass-through only a secondary, unquantified factor.

**(D) Too recent to show up in demand data yet.** The Saudi East-West pipeline
shutdown (2026-09-11, after a drone attack from Iraq) reroutes all crude back
through Hormuz and is the most severe supply escalation since March, but as of
this report's as-of date (2026-09-14) there is no realised demand-side data
covering it — only the logistics response (Saudi refiners report >90% of Sept-Oct
crude needs already secured, suggesting limited near-term shortfall) and the price
reaction. The 2026-09-13 attack on an Iranian commercial vessel and the collapse of
Oman-brokered shipping-protection talks add further near-term risk not yet
reflected in any hard macro print.

### 4. Forecast revisions — kept separate from the above

None of the following are realised outcomes; all are point forecasts, shown with
their revision direction and the reason given:

- **BOJ Outlook Report**: real GDP FY2026 raised slightly, 0.5% (April) → 0.6%
  (July), while core CPI FY2026 was *cut*, 2.8% (April) → 2.5% (July) — the BOJ's
  stated reasoning is that AI-related demand offset the growth hit while oil prices
  eased from their March peak by the time of the July report (helped by June
  ceasefire talk). This is a forecast **improvement** on both fronts, moving in the
  opposite direction from the Cabinet Office (below) over the same window —
  flagged as a genuine cross-institution discrepancy, not resolved in this note.
- **Cabinet Office**: real GDP FY2026 *cut* sharply, 1.3% (January, pre-war) → 0.9%
  (2026-07-30), explicitly citing elevated oil prices; the oil price assumption used
  in the forecast was raised from $68/bbl to $92.5/bbl over the same period.
- **IMF**: global growth 2026 cut from 3.1% (April WEO) to 3.0% (July WEO Update),
  explicitly citing "lingering effects" of the Iran-war energy shock. Secondary
  reporting on IMF China/Japan 2026 forecasts is internally inconsistent between a
  4.4% and a 4.6% China figure attributed to different WEO vintages within the same
  article — flagged as unresolved, needs a primary WEO table check.
- **OECD**: global growth cut to 2.8% for 2026 (from 3.4% in 2025), with an explicit
  warning of the "deepest slowdown in 40 years outside COVID/GFC" if the conflict
  persists. No China/Japan-specific OECD figures were located (gap).
- **Goldman Sachs (China)**: an apparent large forecast *upgrade*, from 4.3%
  (original ~Dec 2025/Jan 2026, pre-war outlook) to 4.8% (a later revision, exact
  date unconfirmed) — attributed to AI/tech export resilience outweighing the
  energy drag. This should be treated cautiously: the exact date and vintage of the
  4.8% figure could not be confirmed, and a GS commodities outlook found in the same
  search (Brent/WTI averaging $56/52 for 2026) is clearly a stale pre-war forecast
  now overtaken by realised prices of $84–91/bbl — a caution against using any GS
  2026 outlook number without checking its publish date against the war timeline.

### 5. Elasticities for scenario modelling — mostly a gap, reported honestly

Per the brief's instruction to write NA rather than invent, most of the specific
elasticities requested (GDP impact per $10/bbl for Japan and China; terms-of-trade
transfer as % of GDP for either country; CPI pass-through per 10% naphtha or
electricity move) **could not be sourced to a specific, citable primary study** in
this WebSearch-only pass — WebFetch being blocked meant BOJ/Cabinet Office/RIETI
PDFs and discussion papers could be found by title but not read for their actual
coefficients. Where a number appeared, it is included in
`ws3_elasticities.csv` with an honest quality flag:
- A **calc**-quality Japan CPI-per-$10/bbl estimate (~0.05pp) was derived from a
  secondary (Deloitte) citation of a Cabinet Office six-month, $30/bbl scenario —
  shown with its formula, but low confidence given the linear-scaling assumption.
- A commonly repeated **0.3–0.4pp per $10/bbl** Japan CPI figure surfaced in
  search-synthesized commentary but its primary source (possibly RIETI) could not
  be confirmed — included but explicitly flagged low-confidence, source_url NA.
- Short-run oil demand price elasticities are global/US benchmarks only
  (~-0.05 to -0.25 depending on product; a 23-country range of -0.05 to -0.77
  short-run), **not** Japan/China-specific — used as proxies only, flagged as such.
- The one solid regional calibration metric found: Asia's energy (oil+gas) use is
  ~4% of GDP (IMF, via ICIS reporting), roughly double Europe's — useful as a
  structural-exposure input to a model even though it is not itself a shock
  elasticity.

## Uncertainties and gaps

1. **Japan Q2 GDP QoQ figure is internally inconsistent across secondary sources**
   (0.3% vs 0.4%) — recommend confirming against the Cabinet Office ESRI primary
   release before using in any downstream model.
2. **IMF China 2026 growth forecast is inconsistently reported** (4.4% vs 4.6%)
   across what may be different WEO vintages, both attributed via the same
   secondary article — needs a primary WEO database check.
3. **USD/JPY pre-war (Feb 2026) baseline was not located** in this search pass —
   only the current (Sept 2026) level and its 1-month/12-month changes were found.
   A primary MOF/BOJ FX series check is needed to compute a clean war-window change.
4. **USD/CNY shows the yuan appreciating** ~2.9% from the Feb/Mar 2026 baseline to
   September, which is counterintuitive for an economy absorbing a negative
   terms-of-trade shock via a large, oil-exposed current account. This could reflect
   broad dollar weakness, PBOC fixing management, or a data quality issue in the
   aggregator source used (tradingeconomics.com) — flagged for cross-check against
   PBOC/SAFE primary data, not resolved here.
5. **China LNG import volumes for 2026 were not located** as hard monthly figures —
   only a qualitative claim that China "managed" the loss of Qatari cargo share.
   This is a real gap given LNG's centrality to the brief's Hormuz narrative.
6. **Japan retail sales after April 2026, and Japan manufacturing PMI after July
   2026, were not located** — both series have a 4+ month reporting gap in this
   dataset that should be closed with a targeted follow-up search.
7. **China August 2026 industrial production was not located** — the series in this
   note stops at July (+4.5% YoY).
8. **War-risk insurance premiums**: the brief's baseline (~1% by late March/April)
   is now clearly stale — late-July 2026 reporting puts premiums back up at
   7.5–10% of hull value, a renewed surge not captured in the shared baseline.
   No reading was found covering the 2026-09-11 pipeline attack or 2026-09-13
   vessel attack specifically — likely higher still, unconfirmed.
9. **Elasticities requested by the brief (GDP per $10/bbl for JP and CN;
   terms-of-trade transfer as % GDP for either country; naphtha/electricity CPI
   pass-through per 10% move) could not be sourced** to citable primary research in
   this pass. This is the single biggest gap for the quantitative model this
   workstream is meant to feed, and is explicitly marked NA (not estimated) in
   `ws3_elasticities.csv`. Closing it requires direct retrieval of BOJ Outlook
   Report background boxes, Cabinet Office WEO short-run model documentation, or
   RIETI/IMF working papers — none of which could be read as PDFs given the
   WebFetch restriction on this task.
10. All PMI/CGPI/CPI/PPI "August 2026" prints in this note are the **latest
    available as of 2026-09-14**; September prints for most series will not exist
    yet and are not expected in this dataset.

## Sources

- https://www.cnbc.com/2026/05/19/japan-first-quarter-gdp-economy-inflation-energy.html
- http://www.china.org.cn/world/Off_the_Wire/2026-06/08/content_118536904.shtml
- https://www.cnbc.com/2026/08/17/japan-gdp-misses-estimates-trade-exports-yen-nikkei.html
- https://www.tmgm.com/en/analysis/market-news/article/japans-gdp-grows-03-qoq-in-q2-2026-vs-05-expected-202608162353
- https://www.fxstreet.com/news/japans-gdp-grows-03-qoq-in-q2-2026-vs-05-expected-202608162353
- https://www.stats.gov.cn/english/PressRelease/202604/t20260416_1963326.html
- https://www.focus-economics.com/countries/china/news/gdp/china-national-accounts-17-07-2026-economic-growth-decelerates-in-the-second-quarter-of-2026/
- https://aninews.in/news/business/japans-industrial-output-rises-for-fourth-consecutive-quarter-up-01-mom20260831105722/
- https://global.chinadaily.com.cn/a/202604/16/WS69e042f4a310d6866eb43c35.html
- https://wmbdradio.com/2026/08/17/chinas-july-industrial-output-grew-4-5-y-y-retail-sales-up-0-6/
- https://www.cnbc.com/2026/08/17/china-economy-sales-investment-july-.html
- https://www.cnbc.com/2026/03/24/japan-cpi-inflation-february-.html
- https://www.cnbc.com/2026/08/21/japan-inflation-iran-war-energy.html
- https://www.cnbc.com/2026/09/09/china-cpi-ppi-august-oil-prices-tech-manufacturing-.html
- https://investinglive.com/news/japan-wholesale-inflation-stays-hot-in-august-cements-case-for-boj-hike/
- https://www.tradingview.com/news/seekingalpha:56b36b5ae094b:0-japan-s-august-ppi-rises-7-6-y-y-exceeding-expectations-manufacturer-sentiment-rebounds-to-highest-level-since-2021/
- https://www.japantimes.co.jp/business/2026/07/22/economy/japan-trade-deficit-june/
- https://www.investing.com/economic-calendar/trade-balance-1005
- https://www.cnbc.com/2026/09/08/china-exports-imports-august-trade-rebalance-demand-surplus-.html
- https://tradingeconomics.com/japan/manufacturing-pmi/news/527190
- https://news.metal.com/newscontent/104087023-national-bureau-of-statistics-nbs-august-manufacturing-pmi-at-498-up-06-percentage-points-from-previous-month-prosperity-level-rebounded
- https://www.stats.gov.cn/english/PressRelease/202609/t20260901_1965170.html
- https://investinglive.com/news/china-data-ratingdog-manufacturing-pmi-august-2026-vs-expected-50-9-prior-50-9/
- https://www.indexbox.io/blog/china-manufacturing-pmi-rises-to-515-in-august-beating-expectations/
- https://tradingeconomics.com/japan/retail-sales-annual/news/537585
- https://english.www.gov.cn/archive/statistics/202608/17/content_WS6a82b953c6d00ca5f9a0ca39.html
- https://tradingeconomics.com/japan/wage-growth/news/461251
- https://www.xe.com/en-us/currencycharts/?from=USD&to=JPY
- https://tradingeconomics.com/china/currency
- https://www.valutafx.com/history/usd-cny-2026
- https://www.eia.gov/todayinenergy/detail.php?id=67905
- https://www.bloomberg.com/news/articles/2026-06-09/china-s-oil-imports-plunge-to-eight-year-low-on-war-disruptions
- https://www.itiger.com/hans/news/2565328572
- https://www.arabnews.jp/en/business/article_167167/
- https://www.arabnews.jp/en/business/article_173200/
- https://www.sahmcapital.com/news/content/japanese-refinery-runs-down-to-725-on-a-weekly-basis-2026-04-01
- https://www.hydrocarbonprocessing.com/news/2026/04/japanese-refinery-runs-at-lowest-since-june-2025-on-middle-east-supply-crisis/
- https://www.spglobal.com/commodity-insights/en/news-research/latest-news/crude-oil/051320-japan-data-may-3-9-crude-runs-fall-to-229-mil-bd-65-of-capacity-paj
- https://oilprice.com/Latest-Energy-News/World-News/Japans-Refinery-Utilization-Hits-73-as-Strategic-Oil-Stocks-Flow-In.html
- https://www.indexbox.io/blog/chinese-independent-refiners-shift-from-iranian-to-gulf-crude-amid-widening-discounts/
- https://finance.yahoo.com/energy/articles/japans-lng-imports-fall-7-080000079.html
- https://www.energyconnects.com/news/utilities/2026/july/japan-cuts-gas-in-favor-of-coal-as-hormuz-disruption-chokes-lng/
- https://www.euronews.com/business/2026/08/31/qatarenergy-extends-lng-cancellations-into-november-as-hormuz-disruption-drags-on
- https://www.hydrocarbonprocessing.com/news/2026/03/asia-refineries-petchem-firms-cut-runs-as-middle-east-conflict-disrupts-feedstock-supplies/
- https://cen.acs.org/business/petrochemicals/Hormuz-Strait-pinch-worsens-Asian/104/web/2026/03
- https://www.agbi.com/petrochemicals/2026/03/premiums-surge-as-iran-war-disrupts-asias-naphtha-supply/
- https://www.bloomberg.com/news/articles/2026-03-16/shortage-of-naphtha-threatens-supply-chain-chaos-in-japan
- https://oilprice.com/Latest-Energy-News/World-News/Sinopec-Sees-China-Oil-Demand-Falling-89-in-2026.html
- https://www.kpler.com/blog/china-s-road-fuel-demand-displacement-reaches-1-3-mbd-in-2026-as-high-prices-accelerates-technology-shift
- https://gmk.center/en/news/china-has-committed-to-reducing-its-steel-production-capacity-by-2026/
- https://energyandcleanair.org/china-energy-and-emissions-trends-march-2026-snapshot/
- https://www.procurementresource.com/resource-center/kerosene-price-trends
- https://www.spglobal.com/commodity-insights/en/news-research/latest-news/crude-oil/071924-japan-exempts-refiners-from-raising-refinery-capacity-to-meet-jet-fuel-shortage
- https://www.cnbc.com/2026/09/11/saudi-arabia-shut-down-east-west-crude-oil-pipeline.html
- https://www.socialnews.xyz/2026/09/13/saudi-pipeline-shutdown-to-have-limited-impact-on-supply-in-short-term/
- https://www.thenationalnews.com/business/2026/07/17/war-risk-shipping-premium-surges-again-as-tensions-escalate-at-strait-of-hormuz/
- https://www.boj.or.jp/en/mopo/outlook/gor2604b.pdf
- https://www.boj.or.jp/en/mopo/outlook/gor2607b.pdf
- https://www.japantimes.co.jp/business/2026/07/30/economy/economic-outlook-trim/
- https://www.imf.org/-/media/files/publications/weo/2026/april/english/ch1.pdf
- https://www.imf.org/-/media/files/publications/weo/2026/update/july/english/text.pdf
- https://www.aljazeera.com/economy/2026/7/9/imf-cuts-2026-world-growth-forecast-citing-iran-war-fallout
- https://qz.com/oecd-global-growth-forecast-middle-east-conflict-energy-060326
- https://www.gspublishing.com/content/research/en/reports/2026/01/04/3c617d10-bb6d-42a9-8e10-478a67e476af.html
- https://x.com/GoldmanSachs/status/2011075763387142266
- https://www.deloitte.com/us/en/insights/topics/economy/asia-pacific/japan-economic-outlook/04-2026.html
- https://www.eia.gov/workingpapers/pdf/key_international_demand_elasticities.pdf
- https://www.reed.edu/economics/parker/f10/201/cases/oil_demand.html
- https://www.researchgate.net/publication/4916443_Price_elasticity_of_demand_for_crude_oil_estimates_for_23_countries
- https://www.icis.com/explore/resources/news/2026/04/17/11198970/asia-economic-resilience-being-tested-by-energy-shock-imf/
- https://www.jcer.or.jp/english/japanese-economy-update_march-2026
- https://www.rieti.go.jp/en/columns/a01_0510.html
- https://www.smileswallet.com/japan/japan-summer-electricity-gas-subsidies-2026/
- https://www.timeout.com/tokyo/news/electricity-and-gas-bill-subsidies-around-5-000-are-coming-to-tokyo-this-summer-052626
