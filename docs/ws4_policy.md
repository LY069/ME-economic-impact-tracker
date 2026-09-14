# WS4 — Government Policy Offsets: Japan & China (Iran/US 2026 Shock)

**As-of date: 2026-09-14.** Covers fiscal, price-control, reserve-release and monetary
policy responses in Japan and China to the 2026 Iran war energy shock, and the
outlook for continuation vs. withdrawal of each measure.

**Denominator assumptions used for `pct_gdp`/USD conversions** (not independently
verified via search this session — flagged as an assumption, not a sourced figure):
Japan nominal GDP ≈ JPY609tn (~$4.1tn); China nominal GDP ≈ CNY135tn (~$18.9tn);
FX: USD/JPY ≈ 150 (within the sourced 150–160 2026 trading range), USD/CNY ≈ 7.15.
Any `pct_gdp` or `size_usd_bn` figure derived this way is labeled `calc` in spirit
even where the CSV quality column inherits the underlying fact's label — treat these
conversions as approximate.

## Key figures

| Measure | Country | Size | Status (2026-09-14) | Continuation probability |
|---|---|---|---|---|
| Provisional gasoline/diesel tax abolition | JP | ¥1.5tn/yr revenue loss (est) | Permanent, enacted | 0.95 |
| Fuel Oil Price Stabilization Fund (wholesaler subsidy) | JP | ~¥2tn fund; ~¥600bn/mo burn | Active, benchmark now ¥26.2/L (Sept) | 0.85 |
| FY2026 supplementary budget (fuel/utility relief) | JP | ¥3.1tn ($19.4bn) | Enacted (~June 2026) | one-off, spent |
| Electricity/gas bill subsidy (summer tranche) | JP | ¥500bn ($3.15bn) | Expired 2026-09-30; winter renewal unconfirmed | 0.6 (renewal) |
| SPR releases (3 tranches) | JP | ~80mn bbl / 45 days; cumulative reserve fell 254→214 days | Completed; no confirmed new tranche since 09-11 pipeline shutdown | gap — see Uncertainties |
| Coal capacity-market rule suspension | JP | ~500,000t LNG/yr saved | Active through FY2026-27 (to 2027-03) | 0.9 |
| BOJ policy rate | JP | 0.75%→1%→(expected 1.25% on 09-18) | Active tightening cycle | 0.88 (Sept hike) |
| MOF FX intervention | JP | ~¥9.5–10tn (~$65bn) | Episodic; last confirmed late April/May | 0.5 (recurrence) |
| NDRC refined-price partial pass-through (>$80/bbl) | CN | ~40–53% of "natural" increase absorbed per adjustment | Active, reapplied 2026-09-11 | 0.9 |
| NDRC formal $130/bbl freeze | CN | N/A | Not yet triggered (Brent peak ~$119.5) | 0.38 (trigger by YE2026) |
| Refined-oil export quotas (2 batches) | CN | 32 Mt cumulative, +0.6% y/y | Maintained, not cut | 0.75 |
| Teapot crude import quotas | CN | 257 Mt, unchanged y/y | Maintained | 0.8 |
| Urea export quota | CN | 3.3 Mt (–34% y/y) | Quota effectively exhausted in Jun–Aug window | 0.9 (stays tight) |
| PBOC easing (RRR/rate cuts, May) | CN | RRR –50bp; 7-day repo –10bp | Implemented | 0.55 (further cuts) |
| Special treasury bonds — consumer trade-in | CN | ¥250bn of a ¥1.3tn renewal | Active through 2026 | 0.85 |

## Narrative

### 1. Japan policy inventory

**Provisional gasoline/diesel tax abolition.** In November 2025, six ruling and
opposition parties agreed to scrap the decades-old "provisional" tax add-ons:
¥25.1/L on gasoline (effective 2025-12-31) and ¥17.1/L on diesel (effective
2026-04-01). The Diet passed the bill unanimously on 2025-11-28. This is a
**permanent, structural** tax cut, not an emergency measure — it landed as full
abolition, not a partial cut or a debate that stalled. It leaves an estimated
¥1.5tn/yr revenue shortfall that the law's supplementary clause requires the
government to address within about a year; how that gap gets closed (spending
cuts vs. another tax) is an open fiscal question. [Japan Times; RIETI]

**Fuel wholesaler subsidy ("¥170/L" price-stabilization program).** The subsidy
(paid to oil wholesalers via the Fuel Oil Price Stabilization Fund) had actually
just been wound down alongside the tax cut, then was urgently **restarted** on
2026-03-19 as Brent spiked to ~$118/bbl and pump gasoline hit a record ¥190.8/L.
The subsidy rate escalated from ¥5/L (January, pre-war baseline) to ¥25/L (March
restart) to a benchmark of ¥26.2/L by 2026-09-03 (with a parallel domestic-airline
jet-fuel subsidy raised to 80% of that benchmark, ¥20.9/L, even as the
international-flight subsidy was allowed to lapse the same day — an early sign of
selective tapering at the margin). The benchmark was also switched from Brent to
Dubai crude on 2026-06-04 as the Dubai–Brent spread narrowed, a cost-optimization
tweak rather than a policy reversal. [Japan Times; METI; S&P Global; Travel And
Tour World; IndexBox]

**Fiscal cost and replenishment.** By April–May 2026 the program was burning
roughly ¥600bn/month against a combined fund-plus-reserve balance of just over
¥2tn — Nomura Research Institute estimated exhaustion around 2026-06-26 absent a
top-up. Japan responded with a ¥3.1tn (~$19.4bn) supplementary budget (finalized
around June 2026) explicitly to replenish contingency reserves used for gasoline
and utility subsidies. A separate ¥5tn (~$32bn) package with ¥2.2tn earmarked for
petrol stabilization was reportedly approved just before the war started
(February 2026) — treat this as pre-war/early-war baseline funding rather than a
war-response measure proper. [NRI; Nikkei Asia; Investing.com]

**Electricity and city-gas subsidies.** Winter tranche (Jan–Mar 2026): ¥4.5/kWh
electricity + ¥18/m³ gas, estimated ¥7,300 saving per household. Summer tranche
(Jul–Sep 2026, ~¥500bn/$3.15bn): ¥3.50/kWh (Jul, Sep) / ¥4.50/kWh (Aug)
electricity; ¥14/m³ (Jul, Sep) / ¥18/m³ (Aug) gas. This tranche expired
2026-09-30; **no winter 2026-27 renewal has been confirmed** in available
sources — a live open question given the precedent of intermittent renewal since
2023. [Smiles Wallet; Voice of Emirates; Time Out Tokyo]

**SPR releases.** Three confirmed tranches: 2026-03-16 (largest-ever release,
~80mn bbl / 45 days — private mandatory stockpile cut from 70 to 55 days plus one
month of national reserves transferred), 2026-04-15, and 2026-04-24 (cumulative
~20 days released by early May). By April 2026 Japan's total reserve coverage had
fallen from a pre-war ~254 days (146 national + 101 private + 7 joint, per
2025-12-31 data) to ~214 days (131 national + 81 private). This was part of a
broader March 2026 IEA coordinated release (32 member countries; the US alone
authorized 172mn bbl). **No dated, volumed SPR release announcement for the period
after the 2026-09-11 East–West pipeline shutdown or the 2026-09-13 Hormuz attack
was found in this session's searches** — flagged as a gap; Japan's stated posture
is instead to *rebuild* toward the IEA 90-day standard during FY2026–27 while
diversifying supply (backing pipelines that bypass Hormuz). [Japan Times;
Nippon.com; CIJToday; Asia Times; Al Jazeera]

**Petrochemicals/naphtha.** Japan sources ~40% of naphtha from the Middle East
(one estimate: 40% domestic, 40% Middle East, 20% other; a separate estimate:
~60% imported, of which "over 70%" from the Gulf — roughly consistent at ~40–42%
of total supply). Only about three weeks of naphtha stock is typically held. In
response, Japan is (a) importing more intermediate chemicals, including from
China, (b) building national naphtha reserves in crude-oil form, and (c) running
a **levy-funded cost-sharing subsidy** to offset the higher cost of substitute
(non-Middle-East) crude/naphtha. No yen figure for the size of this subsidy was
found — gap. [Hydrocarbon Processing; Nippon.com; Nikkei Asia]

**LPG.** The general fuel subsidy explicitly covers gasoline, diesel, kerosene and
heavy oil; no LPG/propane-specific subsidy rate or budget line was found in
available sources — gap.

**Nuclear, coal and setsuden.** Kashiwazaki-Kariwa Unit 6 (1,356 MW) restarted
2026-02-09, taking Japan to 15 operating reactors (33 GW); estimated to displace
~1.3mn t LNG/yr. METI on 2026-03-27 suspended, for FY2026–27, the capacity-market
rule requiring coal plants under 42% design efficiency to cap annual capacity
factor at 50% — estimated to save ~500,000t/yr of LNG (~10% of the ~4mn t/yr
previously transiting Hormuz). PM Takaichi has stated that expanded coal plus
restarted nuclear together offset roughly 40% of the LNG Japan previously imported
via Hormuz. No formal 2011-style voluntary "setsuden" conservation campaign was
found for 2026 — the government's approach has been supply-side (more coal, more
nuclear) rather than demand-restraint messaging. [Argus Media; EIA; Foreign
Policy; E&E News]

**BOJ policy rate.** The BOJ has been explicitly treating this as a shock that
*requires more tightening*, not one to look through: on 2026-04-28 it held at
0.75% (6–3 split, dissenters wanted a hike) while raising its FY2026 core CPI
forecast to 2.8% from 1.9%, citing crude oil, yen depreciation and wage pass-through.
By 2026-07-31 the rate stood at 1% (8–1, with board member Takata pushing for
1.25%). Ahead of the 2026-09-17/18 meeting, Governor Ueda and board member Masu
(2026-09-10 speech) signalled continued hikes are likely "at every meeting,"
with markets pricing ~88% probability of a 25bp move to 1.25%. The explicit
rationale is to prevent underlying inflation from significantly overshooting the
2% target as an energy-cost shock threatens to un-anchor wage-price expectations —
the opposite of a central bank absorbing a one-off supply shock passively.
[CNBC; Bloomberg; Japan Times; BOJ]

**MOF FX intervention.** Combined operations around 2026-04-30/05 estimated at
~¥9.5–10tn, moving USD/JPY from ~164 back to ~155, apparently defending a
~¥160 line rather than a fixed target. USD/JPY has traded 150–160 through
2025–2026, sustained by a 350–450bp US–Japan 2-year yield spread. MOF has stated
there is no binding legal cap on intervention frequency. [OMFIF]

**PM and coalition.** PM Sanae Takaichi (LDP) leads a coalition with the Japan
Innovation Party (Ishin) after Komeito exited; the February 2026 snap election
gave the LDP alone 316 seats (a two-thirds supermajority with Ishin). This
insulates the government from a near-term general election test (no House of
Representatives election is due until the current term expires, absent another
snap dissolution). However, cabinet approval fell from the 58–72% range in
March 2026 to below 50% by mid-July, with further slippage reported through
August, and by August 64% of respondents disapproved of the government's
inflation response specifically — despite the subsidies already in place. This
creates a political incentive to **keep** subsidies (rather than withdraw them)
even without an imminent election, since the subsidies are the government's
primary visible inflation-relief tool and are already seen as insufficient.
[Japan Times; NPR; ABC News; Al Jazeera]

### 2. China policy inventory

**NDRC refined-product pricing mechanism and the $130/bbl clause.** China's
mechanism (in place since 2016) tracks a crude-basket price every 10 working
days: it narrows retail adjustments once the basket exceeds $80/bbl and is
designed to **freeze retail prices entirely** if the basket exceeds $130/bbl.
On 2026-03-23, China invoked **discretionary "temporary control measures"** —
the first such intervention since the mechanism's 2013 predecessor — capping the
gasoline/diesel increase at ¥1,160/¥1,115 per mt versus a mechanism-implied
¥2,205/¥2,120 per mt (~53% pass-through). This pattern recurred: 2026-04-07
(actual ¥420/¥400 vs. implied ¥800/¥770, ~53%) and 2026-09-11, after the East–West
pipeline shutdown and Hormuz escalation (actual ¥260/¥250 vs. implied ¥435/¥420,
~60% pass-through; NDRC said this saved private drivers ~¥7 and truckers ~¥75 per
fill-up versus the uncapped mechanism outcome). **Brent has not sustained above
$130/bbl in 2026** (peak observed in this session's sources: ~$118–119.5, both
in late March and again around 2026-09-09) — so the formal full-freeze clause
has **not** been triggered to date; China has instead used the softer,
discretionary partial-pass-through tool repeatedly, now effectively
institutionalized as a standing practice at every 10-day pricing window rather
than a one-off. **Refiner-margin effect:** under the mechanism, retail-ceiling
margins turn "narrow or negative" once crude exceeds $80/bbl; Sinopec's refining
division reportedly posted a ¥9.2bn loss in Q1 2026, with one bank (Credit
Suisse) projecting a full-year loss of ¥56bn assuming Brent averages $125 —
i.e., the state is transferring the cost of price suppression onto SOE refiner
balance sheets rather than onto the CPI. [NDRC; China Daily; Global Times;
Xinhua/china.org.cn; S&P Global]

**SPR.** China entered the war with an estimated 1.1–1.4bn bbl in strategic
reserves (110–140 days of net imports), having added ~1.1mn bpd to inventories
through 2025, partly using discounted/sanctioned crude. **Unlike Japan or the
IEA-coordinated release, no official, sourced announcement of a Chinese SPR
release volume or date was found this session** — China does not publish SPR
levels or release decisions with Japan/US-style transparency. The May 2026 fall
in Chinese crude imports and refiner destocking documented in the shared
baseline refers to **commercial** stock drawdowns, not a confirmed SPR release —
this distinction should not be collapsed. Flagged as a significant data gap
requiring dedicated (Kpler/Vortexa-type) tracking rather than public statements.
[RAND; EIA; SCMP; National Security Journal — background only, no 2026 release
figure sourced]

**Refined-product export quotas.** Rather than cutting exports to conserve
domestic supply, China **maintained or slightly raised** quotas: 2026 batch 1
(≈Nov 2025) = 19 Mt clean products (steady y/y) + 8 Mt low-sulfur bunker fuel;
batch 2 (mid-2026) = 13 Mt, bringing the cumulative 2026 total to 32 Mt, +0.6%
y/y. Over 70% goes to Sinopec/CNPC. This suggests Beijing prioritized
export-market share/foreign-exchange revenue over aggressive domestic hoarding,
at least through mid-2026. [OilPrice.com; OPIS]

**Crude import quotas for independent ("teapot") refiners.** Total non-SOE
quota for 2026 held at 257 Mt, **unchanged year-on-year**; major individual
allocations include Hengli (2 Mt / 40 kbd), Rongsheng (0.75 Mt), Shenghong
(0.12 Mt) and Hongrun (0.53 Mt). No evidence of a crisis-driven quota cut.
[Baird Maritime; Tekedia; China-Global South Project]

**Fuel oil/bitumen-blend consumption tax.** Available sources only document the
pre-existing regime (CNY1.2/L, ~$189/mt, equalized with fuel-oil tax since 2021);
**no 2026-specific tariff or consumption-tax change was found** — flagged as a
gap, not confirmed as "no change."

**Coal, dual control and industrial power rationing.** China did **not**
visibly ramp up coal-fired generation because of the oil shock: coal power
generation actually **fell** 2.5% y/y in the period reported (after six
consecutive months of growth), and analysts (China-Global South Project, Carbon
Brief) argue the structure of China's coal-dominated, largely oil-insulated
power system makes an oil-price-driven coal surge unlikely. More importantly,
under the 15th Five-Year Plan (2026–2030) China has explicitly **shifted policy
away from the 2021-style "dual control" total-energy-consumption cap** toward an
emissions-intensity framework — the mechanism that caused 2021's industrial
power rationing. No evidence of a 2026 reimposition of industrial power
rationing tied to this shock was found. This is an inference from general
policy commentary rather than a direct statement that rationing was avoided, so
confidence is moderate, not high. [Carbon Brief; China-Global South Project;
Global Energy Monitor]

**Electricity pricing.** Industrial tariffs (36-city avg, ≥35kV) rose modestly
from ¥0.610/kWh (June) to ¥0.620/kWh (July 2026), +1.6% m/m — no emergency
pricing action found. Residential tariffs (~¥0.532/kWh, Dec 2025 reading) show
no discrete 2026 change in available sources, and **no household electricity
relief scheme comparable to Japan's was found for China** — gap/asymmetry worth
noting.

**Discounted Russian/Iranian barrels.** Russian crude to China surged in
Jan–Feb 2026 (+40.9% y/y to 21.8 Mt; deliveries ~2.09mn bpd, a record) — but the
ESPO grade **flipped from a $7–8/bbl discount (late 2025) to a premium in 2026**
as Chinese state refiners and teapots competed for scarce prompt barrels, i.e.
sanctioned-barrel discounts **compressed** sharply during the war rather than
widening. Iranian sales to China fell ~12% year-to-date 2026 versus a year
earlier despite (or because of) the conflict — plausibly because shipping and
insurance risk inside the Strait itself constrained Iran's own export logistics;
July-arrival Iranian Light was offered at only just over $1/bbl below ICE Brent,
a much narrower discount than historical norms. A widely cited "$28.8mn/day"
savings figure from discounted barrels is a **2025** baseline estimate and should
not be read as a current 2026 run-rate given the compression described above.
[SCMP; Bloomberg]

**Fiscal/monetary stimulus.** PBOC held benchmark lending rates unchanged in
April 2026 amid resilient growth and Middle East risk, then drained ~¥890bn via
open-market operations in March 2026 (first net liquidity drain in a year) — a
cautious, inflation-watching signal. As growth concerns (Q2 GDP slowing to 4.3%
y/y from 5.0%, missing the 4.5–5% target band) began to dominate, the PBOC
pivoted to easing: 2026-05-07, 7-day reverse repo cut 10bp to 1.4% and RRR cut
50bp. On the fiscal side, China renewed ¥1.3tn in ultra-long special treasury
bonds for 2026, of which ¥250bn is earmarked for the consumer-goods trade-in
program (an additional ¥62.5bn/~$9.1bn top-up was announced 2025-12-30 for the
same purpose) — this is general countercyclical support rather than an
oil-shock-specific instrument, but it offsets some of the real-income drag from
higher energy CPI. [CNBC; FXStreet; Central Banking; gov.cn; Bloomberg;
IBTimes UK]

**Fertilizer/urea export restrictions.** China's 2026 urea export quota was cut
to 3.3 Mt from ~5 Mt in 2025 (~34% reduction). New export inspections were
suspended entirely in March–April 2026 during spring planting ("supply
assurance, strict control of outflows"), and most of the reduced quota was
compressed into a June–August shipping window (with a brief guidance-price
whipsaw in June — lifted, then reinstated within days, signalling policy
uncertainty). Global urea prices reportedly rose 25% over a two-week span amid
the restriction and broader Middle East-linked gas-feedstock cost pressure.
[China-Global South Project; DiscoveryAlert]

### 3. Continuation vs. discontinuation outlook

**Japan — high-probability continuation:**
- *Gasoline wholesaler subsidy* (0.85): active and escalating (¥5→¥25→¥26.2/L)
  through Sept 2026; burn rate (~¥600bn/mo) against a fund that has already
  needed one ¥3.1tn replenishment shows the mechanism is fiscally
  finite but politically indispensable — Takaichi has explicitly used it as her
  primary inflation-relief tool while approval ratings slide on the inflation
  issue, raising the political cost of withdrawal.
- *Coal capacity-market suspension* (0.9): formally time-bound through
  FY2026–27 (March 2027); a rule change, not a discretionary daily subsidy, so
  high likelihood of running its full legislated course.
- *Nuclear restarts* (0.9): structurally one-directional — once restarted,
  reactors are not typically re-mothballed absent a new safety incident, and
  the trend reinforces a pre-existing 2040 target.
- *BOJ tightening cycle* (0.88 for the September hike specifically): the Bank
  is moving in the opposite direction from a "look-through" response, hiking
  precisely because the energy shock threatens to de-anchor inflation
  expectations above 2%; guidance points to further hikes "at every meeting."
- *Provisional tax abolition* (0.95): a permanent legislative fact, not
  contingent on the war's trajectory — the open question is only how the
  ¥1.5tn/yr revenue hole gets filled, not whether the cut itself reverses.

**Japan — genuinely uncertain / lower confidence:**
- *Winter 2026–27 electricity/gas subsidy renewal* (0.6): the summer tranche
  expired 2026-09-30 with no confirmed follow-on found; precedent (intermittent
  since 2023) argues for renewal, but it is not yet decided.
- *A fourth SPR release* post-2026-09-11: no confirmed announcement found; the
  government's stated medium-term posture (rebuild to IEA's 90-day standard)
  points toward restraint on further releases unless the September escalation
  forces another emergency tranche — treated as a genuine gap, not scored.
- *MOF FX intervention recurrence* (0.5): contingent on USD/JPY direction,
  which itself depends on the BOJ-Fed spread trajectory now that BOJ is hiking.

**China — high-probability continuation:**
- *NDRC partial pass-through above $80/bbl* (0.9): now applied routinely at
  essentially every 10-day pricing window since March 2026, most recently
  2026-09-11 — effectively institutionalized rather than a one-off crisis
  measure.
- *Export quotas maintained* (0.75) and *teapot import quotas unchanged*
  (0.8): both show no sign of crisis-driven tightening; Beijing has so far
  preferred to let refiners (SOEs) absorb margin pain over restricting trade
  flows.
- *Urea export restriction* (0.9): the 2026 quota is calendar-bound and
  concentrated in a Jun–Aug window that has already closed by the as-of date,
  so a de facto tightening for the balance of 2026 is already locked in
  regardless of any new policy decision.
- *Consumer trade-in fiscal support* (0.85): explicitly designed to run
  through end-2026.

**China — genuinely uncertain / lower confidence:**
- *Formal $130/bbl freeze trigger* (0.38 by year-end 2026): requires a
  sustained break above the highest level actually observed this year
  (~$119.5); plausible given repeated escalations (pipeline shutdown, Hormuz
  attack, postponed Iran–Gulf shipping talks) but not yet realized.
- *Further PBOC easing* (0.55): balances a growth undershoot against
  inflation caution from oil pass-through; March's liquidity drain shows the
  central bank is not on a purely dovish autopilot.
- *Reimposition of industrial "dual control" rationing* (0.15, i.e. low):
  the policy framework has structurally moved away from this tool, but this is
  inferred from general 15th-FYP commentary rather than a direct statement
  ruling it out for this specific shock.

### 4. Implications

**(a) GDP and CPI.**
Japan's FY2026 growth forecast has been cut to +0.5% (from +0.8% pre-war),
Q2 2026 GDP grew only 0.3% q/q (annualized ~1.1%, missing the 0.5% q/q
consensus), with domestic demand subtracting 0.2pp even as exports added 0.5pp —
consistent with energy-cost drag on households and firms despite the subsidy
cushion. Tokyo core CPI reached 1.8% y/y in August 2026 (core-core 2.0%),
pushing the case for the BOJ's September hike; one third-party estimate (not
government-confirmed) puts the combined effect of Japan's energy subsidies at
**suppressing headline CPI by roughly 1.0 percentage point** versus an
estimated ~3% "underlying" (ex-subsidy) rate — i.e., without the subsidy
package, reported inflation would likely be running noticeably hotter. Separately,
one scenario estimate (not a realized outturn) suggested a prolonged Hormuz
closure could cut Japan's GDP by up to 3% this year via the LNG/electricity-price
channel; the actual FY2026 forecast (+0.5%, a 0.3pp downgrade) is far smaller,
suggesting either that this scenario estimate is a stress-case upper bound or
that policy offsets (SPR releases, coal/nuclear switching, subsidies) have
materially blunted the realized hit — both readings are plausible and the
session's evidence cannot fully discriminate between them.

China's Q2 2026 GDP growth slowed to 4.3% y/y (from 5.0% in Q1), missing
consensus (4.5–4.6%) and falling below the government's 4.5–5% annual target
band, attributed partly to rising resource/material costs from the Iran
tensions and fading consumption-subsidy effects. August 2026 CPI re-accelerated
to 0.8% y/y (from 0.5% in July) with PPI at 3.8% y/y, both flagged by NBS as
partly energy/transport-cost driven — coinciding with Brent's climb back above
$100 around the September pipeline-shutdown/Hormuz-attack escalation. The NDRC
mechanism is explicitly designed to shave points off this CPI trajectory: the
September 11 adjustment alone absorbed roughly 40% of the "natural"
mechanism-implied retail increase, at the direct cost of SOE refiner margins
(Sinopec Q1 refining loss ~¥9.2bn) rather than consumer prices.

**(b) Supply/demand balance — the price-signal-suppression mechanism.**
Both governments' central policy choice has been to **absorb the international
price shock rather than pass it through to consumers**, and the evidence in
this workstream traces the resulting mechanism clearly:

- *Japan*: capping retail gasoline near ¥170/L (later effectively controlled
  via a rising per-litre wholesaler subsidy reaching ¥26.2/L by September)
  despite Brent trading well above $100 and a weak yen (150–160/USD) meant
  retail demand was **not** rationed by price to the extent an unsubsidized
  pass-through would have caused. The adjustment instead showed up as **the
  largest-ever SPR drawdown in Japanese history** (reserve coverage falling
  from ~254 to ~214 days by April 2026) — inventories absorbed the shock that
  price would otherwise have allocated via reduced consumption. This is a
  direct, evidenced illustration of the requested mechanism: subsidies keep
  physical demand higher than a free-price counterfactual, which drains
  reserves faster.
- *China*: the NDRC's partial pass-through (consistently ~40–53% of the
  mechanism-implied increase absorbed by the state/refiners since March 2026)
  similarly cushions the price signal for gasoline/diesel consumers. Chinese
  crude imports, which had fallen to multi-month lows around May 2026, were
  reported recovering toward ~7.2mn bpd by September even as Brent approached
  its September peak — consistent with demand not being strongly rationed by
  price, aided by the capped retail price. The cost of this demand-support is
  borne by refiner margins (documented SOE refining losses) rather than by
  consumers or by a visible surge in the CPI print.
- *The flip side — withdrawal*: neither country has yet been forced to fully
  withdraw its price suppression. Japan's fund-burn-rate arithmetic
  (~¥600bn/month against periodic ¥1–3tn top-ups) shows the mechanism has
  a real, finite fiscal ceiling that has already required one emergency
  replenishment; a further escalation without a matching new supplementary
  budget would force either fund exhaustion (letting pump prices rise, which
  would shift the burden onto CPI/real incomes and start to genuinely ration
  demand — rebalancing the physical market but at a political and
  distributional cost) or a fresh appropriation. China's mechanism has no
  announced hard funding ceiling in the same way, but relies on continued SOE
  willingness/capacity to absorb refining losses, which is itself bounded by
  corporate balance sheets and central-government tolerance for reporting
  large state-firm losses. Should either government be forced toward fuller
  pass-through — e.g., by a sustained crude breakout above the formal
  $130/bbl China ceiling, or by exhaustion of Japan's subsidy funding without
  replenishment — the analytical expectation (not yet observed in the data
  gathered this session) is a shift of the burden onto CPI and real incomes,
  which should in turn start to physically ration demand and slow the drain
  on reserves/refiner margins, rebalancing supply and demand at the cost of a
  sharper measured inflation and consumption hit.

## Uncertainties and gaps

- **No confirmed Japan SPR release dated after 2026-04-24**, despite the
  2026-09-11 pipeline shutdown and 2026-09-13 Hormuz attack. Sources describe a
  general posture of "releasing reserves to offset lack of supply" and a
  medium-term *rebuild* goal (IEA 90-day standard, FY2026–27) but no specific
  new tranche with a date/volume was found. This is exactly the kind of "stale
  read" risk flagged in the task — a fresh, targeted search for any
  September/October 2026 Japanese SPR announcement is recommended before this
  finding is finalized in a downstream report.
- **No sourced Chinese SPR release data at all.** China's strategic reserve
  policy in 2026 is described only in terms of pre-war accumulation
  (1.1–1.4bn bbl); whether/how much was released or drawn during the crisis is
  not transparently published and was not found via search this session.
  Estimates from specialist trackers (Kpler, Vortexa) would likely be needed
  to fill this gap.
- **China's fuel-oil/bitumen-blend consumption tax**: only 2021-vintage
  sourcing was found; no 2026-specific rate change confirmed either way.
- **Japan's LPG-specific subsidy rate/budget** was not isolated from the
  general fuel subsidy program in available sources.
- **Japan's naphtha/petrochemical levy-subsidy size** (yen amount) was not
  found; only the existence and mechanism (levy-funded cost-sharing) is
  confirmed.
- **Whether China's formal $130/bbl freeze has ever bound** is an inference
  from price data (Brent peak ~$118–119.5 observed), not a direct government
  statement that the clause remains untriggered — treat this as `est`/`calc`
  rather than `hard`.
- **China dual-control/rationing avoidance** is inferred from general policy
  commentary (Carbon Brief, China-Global South Project) about the 15th FYP's
  framework shift, not from a direct statement that no war-related rationing
  occurred anywhere in China in 2026 — moderate, not high, confidence.
- **GDP denominators** used for `pct_gdp` calculations (Japan ¥609tn, China
  ¥135tn) and the FX assumptions (USD/JPY 150, USD/CNY 7.15) were not directly
  sourced via search this session; they are standard, widely cited macro
  figures but should be re-verified against Cabinet Office/NBS primary data
  before being relied on for precision below one decimal place.
- **The web search budget for this session was exhausted** before a final
  pass specifically targeting policy responses in the 72 hours after the
  2026-09-11 pipeline shutdown and 2026-09-13 Hormuz vessel attack could be
  completed. Everything dated on or before 2026-09-12 in this document should
  be considered reasonably current; anything after that date is a genuine
  blind spot and should be re-checked before this file is treated as
  fully current to the 2026-09-14 as-of date.
- **Possible double-count risk**: China's ¥62.5bn (Dec 2025) and a separately
  reported ~$8.9bn (April 2026) trade-in top-up may refer to the same or
  overlapping allocations rather than fully additive amounts — only the
  clearer ¥1.3tn/¥250bn figure was used in the CSV to avoid overstating size.

## Sources

- https://www.rieti.go.jp/en/papers/contribution/sato-motohiro/40.html
- https://www.japantimes.co.jp/news/2025/11/28/japan/politics/gasoline-bill-pass/
- https://japan.kantei.go.jp/104/statement/202512/17kaiken.html
- https://japantoday.com/category/business/japan's-provisional-gasoline-tax-ends-after-50-yrs-amid-inflation
- https://www.meti.go.jp/english/speeches/press_conferences/2026/0317001.html
- https://eng.rim-intelligence.co.jp/news/features/1817356.html
- https://www.indexbox.io/blog/japan-reverts-to-dubai-crude-for-gasoline-subsidy-benchmarking-from-june-4/
- https://newsinfo.inquirer.net/1582634/japan-to-keep-gasoline-subsidy-program-after-may/amp
- https://www.timeout.com/tokyo/news/electricity-and-gas-bill-subsidies-around-5-000-are-coming-to-tokyo-this-summer-052626
- https://www.japantimes.co.jp/business/2026/03/16/economy/oil-release-japan/
- https://opengov.jp/en/economy/energy/petroleum-reserves/
- https://cijtoday.com/japan-oil-reserves-release-2026/
- https://harici.com.tr/en/japan-plans-19-billion-energy-relief-package-for-fiscal-2026-amid-middle-east-supply-strains/
- https://asia.nikkei.com/economy/japan-approves-19bn-extra-budget-to-curb-fuel-costs-amid-iran-tensions
- https://japan.kantei.go.jp/105/speech/202604/07kaiken.html
- https://www.voiceofemirates.com/en/business/2026/05/26/japan-allocates-3-billion-to-help-families-pay-their-energy-bills/
- https://en.wikipedia.org/wiki/Premiership_of_Sanae_Takaichi
- https://www.abc.net.au/news/2026-02-09/japan-election-sanae-takaichi-landslide-victory/106320228
- https://www.aljazeera.com/news/2026/2/8/pm-sanae-takaichis-party-set-for-majority-in-japan-parliamentary-elections
- https://www.japantimes.co.jp/news/2026/07/16/japan/politics/japan-pm-approval-rating-below-50/
- https://www.japantimes.co.jp/news/2026/07/30/japan/politics/takaichi-popularity-governing-challenges/
- http://www.hydrocarbonprocessing.com/news/2026/04/japan-to-boost-intermediate-chemical-imports-amid-tighter-naphtha-supply/
- https://asia.nikkei.com/economy/trade/japan-turns-to-chinese-petrochemicals-amid-naphtha-crunch
- https://foreignpolicy.com/2026/06/02/gulf-energy-iran-oil-crisis-japan-strategy-nuclear/
- https://www.eia.gov/todayinenergy/detail.php?id=67244
- https://www.eenews.net/articles/no-such-thing-as-absolute-safety-japan-embraces-nuclear-post-fukushima/
- https://www.cnbc.com/2026/07/31/boj-rates-yen-intervention-inflation-japan.html
- https://www.cnbc.com/2026/04/28/bank-of-japan-keeps-policy-rate-steady-cpi-iran-war-gdp.html
- https://www.bloomberg.com/news/articles/2026-06-04/boj-is-said-to-mull-june-rate-hike-with-another-possible-in-2026
- https://www.japantimes.co.jp/business/2026/09/02/economy/boj-ueda-katayama-rate/
- https://www.japantimes.co.jp/business/2026/09/10/economy/boj-board-member-masu-speech-rate-hike/
- https://www.boj.or.jp/en/about/press/koen_2026/data/ko260910a1.pdf
- https://www.fxstreet.com/news/boj-to-hold-key-interest-rate-at-050-in-september-meeting-reuters-poll-202509110437
- https://www.omfif.org/2026/08/japans-yen-intervention-and-the-us-unusual-support/
- https://www.argusmedia.com/en/news-and-insights/latest-market-news/2806874-japan-plans-temporary-ease-of-coal-power-restriction
- https://gulfnews.com/business/energy/japan-to-boost-coal-fired-power-as-mideast-war-triggers-energy-turmoil-media-1.500487703
- https://www.nri.com/en/media/column/nri_finsights/20260513.html
- https://www.tradingkey.com/analysis/politics/asia/261756505-japan-fuel-subsidies-depleting-reserves-oil-crisis-bite-global-liquidity-risks-loom-tradingkey
- https://www.travelandtourworld.com/news/article/rzlitqhv6vqi/
- https://asiatimes.com/2026/09/hormuz-crisis-forcing-japan-to-domesticate-its-energy-security/
- https://www.hydrocarbonprocessing.com/news/2026/08/japan-to-diversify-crude-supplies-back-pipelines-that-bypass-hormuz/
- https://turnleafinsights.substack.com/p/macroeconomic-insights-japan-cpi
- https://www.bloomberg.com/news/articles/2026-05-21/japan-s-inflation-eases-as-takaichi-eyes-more-cost-relief-steps
- https://en.ndrc.gov.cn/news/mediarusources/202506/t20250626_1404387.html
- http://www.china.org.cn/2026-05/09/content_118484326.shtml
- https://www.chinadaily.com.cn/a/202604/08/WS69d5fe1ca310d6866eb423b4.html
- https://www.chinadaily.com.cn/a/202604/09/WS69d70402a310d6866eb42678.html
- https://www.globaltimes.cn/page/202604/1358357.shtml
- https://www.spglobal.com/commodity-insights/en/news-research/latest-news/crude-oil/062922-beijing-offers-subsidy-for-refineries-if-benchmark-crude-price-exceeds-130b
- https://www.spglobal.com/energy/en/news-research/latest-news/energy-transition/032326-china-caps-fuel-price-surge-to-shield-consumers-amid-middle-east-conflict
- https://triviumchina.com/2026/03/24/beijing-intervenes-to-limit-fuel-price-increases-in-unprecedented-move/
- https://en.people.cn/n3/2026/0408/c90000-20444217.html
- https://english.news.cn/20260911/68146d707a89414a8b23412d42e2c6e6/c.html
- https://english.news.cn/20260731/b4d80788e8764de5afcfa3c9ef5dd98f/c.html
- https://www.rand.org/pubs/research_reports/RRA5069-1.html
- https://www.eia.gov/todayinenergy/detail.php?id=67504
- https://finance.yahoo.com/sectors/energy/article/new-data-shows-china-came-into-the-iran-war-with-over-3x-the-strategic-oil-reserves-of-the-us-151438578.html
- https://oilprice.com/Latest-Energy-News/World-News/China-Issues-First-2026-Fuel-Export-Quotas.html
- https://www.opis.com/resources/energy-market-news-from-opis/china-issues-second-batch-of-refined-product-export-quotas-totaling-13-mn-mt-sources/
- https://www.spglobal.com/energy/en/news-research/latest-news/shipping/062326-china-to-keep-clean-oil-product-export-curbs-in-july-policy-may-shift-in-aug
- https://www.bairdmaritime.com/offshore/refining-processing/chinas-teapot-refiners-get-first-2026-oil-quota-boosting-imports
- https://chinaglobalsouth.com/2026/04/09/china-teapot-refiners-crude-import-quotas/
- https://www.tekedia.com/china-begins-issuing-second-batch-of-2026-crude-import-quotas-to-independent-refiners/
- https://chinaglobalsouth.com/analysis/china-coal-consumption-oil-prices-energy-markets/
- https://www.carbonbrief.org/china-briefing-20-august-2026-oil-and-gas-plan-xi-on-climate-change-coal-five-year-plan
- https://globalenergymonitor.org/article/china-wasted-enough-wind-and-solar-cover-all-new-power-demand-h1-2026
- https://www.scmp.com/economy/china-economy/article/3347329/chinas-russian-oil-imports-spike-early-2026-iran-war-changes-outlook
- https://www.bloomberg.com/news/articles/2026-02-25/russia-and-iran-slashing-prices-to-china-as-oil-piles-up-at-sea
- https://www.bloomberg.com/news/articles/2026-06-08/iranian-crude-offered-to-china-at-discount-as-demand-softens
- https://www.cnbc.com/2026/04/20/china-keeps-benchmark-lending-rates-unchanged-as-economic-growth-revs-up-amid-mounting-middle-east-risk-mount-.html
- https://english.www.gov.cn/news/202601/22/content_WS69720cd8c6d00ca5f9a08b8c.html
- https://www.fxstreet.com/news/pboc-governor-pan-announces-lpr-10-bps-cut-rrr-50-bps-cut-and-7-day-rr-cut-to-14-202505070139
- https://investing.com/analysis/markets-embrace-pbocs-bold-stimulus-rate-cuts-as-oil-prices-surge-200652199
- https://x.com/chinascio/status/2042528864010932496
- https://www.bloomberg.com/news/articles/2025-12-30/china-unveils-initial-9-billion-in-consumer-subsidies-for-2026
- https://english.www.gov.cn/news/202604/10/content_WS69d8b355c6d00ca5f9a0a566.html
- https://chinaglobalsouth.com/2026/03/18/china-fertilizer-export-halt-urea-global-food-risk/
- https://discoveryalert.com/analysis/china-urea-exports-quota-global-nitrogen-september-2026/
- https://www.spglobal.com/energy/en/news-research/latest-news/crude-oil/051421-beijing-to-levy-consumption-tax-on-imported-mixed-aromatics-light-cycle-oil-bitumen-blend-from-june-12
- https://www.ibtimes.co.uk/china-economic-growth-slows-2026-1808887
- https://money.usnews.com/investing/news/articles/2026-04-13/china-poised-for-q1-gdp-growth-rebound-but-iran-war-dims-2026-outlook-reuters-poll
- https://www.vantagemarkets.com/market-news/china-cpi-ppi-august-energy-prices-september-9-2026/
- https://www.cnbc.com/2026/08/17/japan-gdp-misses-estimates-trade-exports-yen-nikkei.html
- https://www.japantimes.co.jp/business/2026/05/14/japan-economy-first-quarter-growth/
- https://www.dlri.co.jp/english/report_en/202605YS.html
- https://investinglive.com/news/japan-august-2026-tokyo-headline-cpi/
- https://www.cnbc.com/2026/08/21/japan-inflation-iran-war-energy.html
