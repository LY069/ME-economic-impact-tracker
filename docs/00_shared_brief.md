# Shared analyst brief — Iran/US conflict energy shock, Japan & China

**As-of date: 2026-09-14.** All research must be current to this date.

## Established baseline (verified by lead analyst, 2026-09-14)

- **2026-02-28**: US and Israel launch joint air strikes on Iran. Start of the "2026 Iran war".
- **2026-03-02**: Strait of Hormuz effectively closed. Brent peaks near $118/bbl
  (from ~$71/bbl on 2026-02-27; $94/bbl by 2026-03-09).
- Hormuz transit collapsed: ~5.36 vessels/day in late March 2026 vs 94.3/day in 2025.
  Tanker (oil+LNG) transits fell from 53.2/day to ~2/day.
- IEA has characterised this as the **largest supply disruption in the history of the
  global oil market**.
- **2026-03-16**: Japan begins largest-ever SPR release (~80mn bbl: 15 days of private
  mandatory reserves + 1 month of national reserves). Further releases 2026-04-15,
  2026-04-24 (~20 days from early May).
- **March 2026**: IEA coordinated emergency collective release.
- **2026-05**: China crude imports fall to multi-month lows, by some estimates near half
  pre-war pace; refiners draw down commercial stocks.
- **2026-08-10**: Brent October futures ~$84.11/bbl — prices had eased from the peak.
- **2026-09-11**: Saudi **East–West Crude Oil Pipeline** shut down, forcing all crude
  back through the strait. Reported total disruption of ~39% of global oil trade and
  31% of global shipments. Hormuz transit ~3% of pre-war levels.
- **2026-09-13**: Iranian commercial cargo vessel attacked in Hormuz, one crew member
  killed. Oman-brokered Iran–Gulf talks on shipping protection **postponed**, no accord.
- War-risk insurance premia: ~0.125% of hull value pre-crisis → 2.5–5% at peak →
  ~1% by late March/April. Re-check current level.
- Asia absorbs >80% of crude and LNG transiting Hormuz — the shock is asymmetrically Asian.
- Known reliance anchors to verify/refine: China ~30% of LNG imports from Qatar+UAE and
  ~40% of oil imports via Hormuz; Japan ~6% of LNG from Qatar+UAE but a much higher
  crude share via Hormuz.
- LPG and naphtha supply loss is already curbing petrochemical run rates.

## Country coverage
**Japan and China only.** Other economies appear only as comparators or alternative
supply sources.

## Evidence standards (mandatory)
1. Every number needs a **source URL** and an **observation date**.
2. Label each figure `hard` (published official/industry data), `est` (credible third-party
   estimate), or `calc` (your own calculation — show the formula).
3. **Never invent a number.** If you cannot source it, write `NA` and say what is missing.
4. Prefer primary sources: METI, ANRE, JODI, Japan Customs, MOF, Cabinet Office, BOJ,
   e-Stat, NBS China, GACC customs, NDRC, CNPC/ETRI, IEA, EIA, OIES, Kpler, ICIS, Platts.
5. Distinguish **pre-war baseline** (2025 or Jan–Feb 2026) from **current** readings —
   every impact claim needs both.
6. Flag contradictions between sources rather than silently picking one.
7. Note that some sources found via search may be low-quality aggregators; prefer
   official and established outlets, and mark anything shaky.

## Output contract
Write BOTH:
1. A markdown findings file at the path given in your task, with a
   `## Key figures` table, a `## Narrative` section, an `## Uncertainties and gaps`
   section, and a `## Sources` list of full URLs.
2. One or more tidy CSVs in `data/raw/` using **long format** with these columns:
   `series_id,country,product,metric,unit,date,value,quality,source_url,note`
   - `country`: `JP`, `CN`, `WORLD`, or a supplier ISO code
   - `quality`: `hard` | `est` | `calc`
   - `date`: ISO `YYYY-MM-DD` (use month-end for monthly data)
   - one observation per row, no merged cells, no thousands separators

Do not edit files outside your assigned paths — other agents are working in parallel.
