# Hormuz Shock Tracker — Japan & China

Quantitative assessment of how the 2026 Iran–US conflict's energy supply disruption is
affecting **Japan** and **China**: growth, activity, trade and inflation.

**As-of date: 2026-09-14.**

The study answers five questions:

1. **How large is the supply disruption**, in physical volumes, product by product?
2. **How reliant** are Japan and China on the disrupted products, and how substitutable are they?
3. **What has the impact been so far** — and has demand actually been destroyed, or only forecast to be?
4. **What have governments done** to offset it, will those measures continue, and what follows for
   the economy and for the supply and demand of the affected products?
5. **How large are the reserves**, strategic and private, and **how long do they last** before
   demand destruction becomes unavoidable?

## What is here

```
docs/          research findings, one file per workstream, plus the final report
data/raw/      the research CSVs each workstream produced, with per-row sourcing
data/curated/  the consolidated dataset built from them
analysis/      the scenario model and its parameter file
app/           the interactive tracker (index.html + data.json)
scripts/       dataset build, live-data refresh, validation, standalone build
```

## The dashboard

`app/index.html` is a dependency-free single page: vanilla JS, inline SVG charts, no CDN.
It renders the research dataset, the live market series, and an interactive scenario model.

Run it locally:

```bash
python3 -m http.server 8000 --directory app
# then open http://localhost:8000
```

Or build a portable single file with the data inlined:

```bash
python3 scripts/build_standalone.py -o dist/tracker.html
```

The page holds no numbers of its own. Everything comes from `app/data.json`, so the dashboard
and the Python model cannot drift apart.

## Live data

`scripts/update_data.py` refreshes the market series (Brent, WTI, Henry Hub, USD/JPY, USD/CNY,
and — with free API keys — official EIA and FRED series) and writes them into `app/data.json`
under `live`, each stamped with its source and retrieval time.

```bash
python3 scripts/update_data.py            # refresh
python3 scripts/update_data.py --dry-run  # fetch and report, write nothing
```

`.github/workflows/update-data.yml` runs it every weekday at 06:10 UTC, rebuilds the scenario
outputs, validates, and commits any change. Add `EIA_API_KEY` and `FRED_API_KEY` as repository
secrets to enable those two series; the key-free ones work without any setup.

> **Note on the environment this was built in.** The development sandbox restricts outbound
> network access to an allowlist that excludes every market-data host, so the updater could not
> be executed live here. It is written to degrade gracefully: unreachable series are marked
> `stale` or `unavailable` with the error recorded, the analytical dataset is left untouched, and
> the run still exits 0 so a scheduled job never fails the build. Run it locally or let the
> GitHub Action run it — both have open egress — for genuine live tracking.

## The scenario model

`analysis/scenario_model.py` models four channels, each an explicit arithmetic step rather than a
fitted black box, so the assumptions can be argued with:

1. **Terms-of-trade transfer** — a price rise on net energy imports is real income transferred
   abroad. The dominant channel for Japan.
2. **Price-induced demand response** — voluntary demand destruction via a short-run elasticity.
3. **Physical supply constraint** — when imports plus substitution plus reserve draw fall short,
   the residual is rationed regardless of price. This is *involuntary* destruction and costs far
   more per barrel, because it destroys output instead of transferring income.
4. **Reserve runway** — usable stock over the shortfall rate, bounded by maximum deliverability.

```bash
python3 analysis/scenario_model.py                      # print a summary
python3 analysis/scenario_model.py --out app/scenarios.json
```

Every parameter lives in `analysis/parameters.json` with its source, and the dashboard's
JavaScript port reads the same file.

**The policy switch is the point.** Each scenario can be run with price support on or off.
Support lowers CPI and cushions GDP now, but by suppressing the retail price signal it prevents
demand from adjusting — so physical demand stays high and reserves drain faster, making the
eventual involuntary cut larger. That trade-off is the central policy finding of the study.

## Building the dataset

```bash
python3 scripts/build_dataset.py    # data/raw/*.csv -> data/curated/ + app/data.json
python3 scripts/validate_data.py    # provenance, consistency, scenario coherence
```

The validator fails the build on unsourced or unlabelled observations, on values that break
their own units, and on scenario results that move the wrong way (a worse throughput scenario
showing a smaller GDP hit means a sign error in the parameters).

## Evidence standards

Every figure carries a source URL, an observation date, and a quality label:

| Label | Meaning |
|-------|---------|
| `hard` | published official or industry data |
| `est`  | credible third-party estimate |
| `calc` | derived here — the formula is stated |

Pre-war baselines and current readings are always distinguished, because an impact claim needs
both. Where sources conflict — they do, particularly on current Hormuz throughput and on China's
opaque strategic reserve — the range is reported rather than a false point estimate.

Scenario outputs are **model results, not forecasts**: they state what the assumptions imply.
