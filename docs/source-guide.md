# Source guide — Gulf + Middle East

A reference for primary and authoritative sources used in Gulf, Iran, Iraq, and maritime-chokepoint analysis. Tier secondary sources explicitly. Do not rely on a single secondary report for legal, compliance, sanctions, or AML claims.

## Primary sources by domain

### Sanctions

- **US Treasury OFAC** — Recent Actions, SDN List, FAQ pages. Canonical for US sanctions designations and General Licenses.
  - https://ofac.treasury.gov/recent-actions
  - https://sanctionssearch.ofac.treasury.gov/
- **US BIS** — Federal Register notices, Entity List, Military End User List.
  - https://www.bis.doc.gov/index.php/policy-guidance/lists-of-parties-of-concern
- **EU Council** — sanctions decisions, Official Journal publications, EU consolidated sanctions list.
  - https://www.consilium.europa.eu/en/policies/sanctions/
- **UK OFSI** — UK Sanctions List, financial sanctions notices.
  - https://www.gov.uk/government/organisations/office-of-financial-sanctions-implementation
- **UN Security Council** — sanctions committees, resolutions.
  - https://www.un.org/securitycouncil/sanctions/information

For Iran specifically: OFAC's Iran sanctions program page is the consolidated index. Designation status changes; verify the current status of any specific entity via the SDN search before any operational claim.

### AML / FATF

- **FATF** — public statements, mutual evaluations, follow-up reports.
  - https://www.fatf-gafi.org/
- **MENAFATF** — regional FATF-style body for the Middle East and North Africa.
  - https://www.menafatf.org/

### Energy

- **IEA Oil Market Report** (monthly) — supply, demand, OECD inventories, OPEC production.
  - https://www.iea.org/reports/oil-market-report
- **OPEC Monthly Oil Market Report** — OPEC's view on the market and OPEC+ production data.
  - https://www.opec.org/opec_web/en/publications/202.htm
- **EIA STEO and Country Briefs** — US Energy Information Administration short-term outlook and country analyses.
  - https://www.eia.gov/outlooks/steo/
- **IEF** (International Energy Forum) — producer-consumer dialogue forum reports.

### Maritime

- **IMO** — maritime incident reports, IMO numbers, flag-state communications.
  - https://www.imo.org/
- **EMSA** (European Maritime Safety Agency) — incidents, vessel traffic in EU waters.
- **Classification societies** (ABS, DNV, Lloyd's Register, etc.) for vessel data.
- **Flag-state registries** for vessel registration and ownership history.

For dark-fleet and AIS-based analysis, paid commercial sources (Kpler, TankerTrackers, Lloyd's List Intelligence, Windward) are operative; do not fabricate AIS data or vessel positions if you do not have access.

### Banking

- **BIS Consolidated Banking Statistics** — cross-border banking exposure, including to Gulf states and Iran.
  - https://www.bis.org/statistics/consstats.htm
- **Central banks:**
  - SAMA (Saudi Central Bank): https://www.sama.gov.sa/
  - Central Bank of the UAE (CBUAE): https://www.centralbank.ae/
  - Qatar Central Bank (QCB): https://www.qcb.gov.qa/
  - Central Bank of Kuwait (CBK): https://www.cbk.gov.kw/
  - Central Bank of Bahrain (CBB): https://www.cbb.gov.bh/
  - Central Bank of Oman (CBO): https://cbo.gov.om/
  - Central Bank of Iran (CBI): https://www.cbi.ir/
  - Central Bank of Iraq (CBI Iraq): https://cbi.iq/
  - Banque du Liban (BDL): https://www.bdl.gov.lb/

### Macro

- **IMF Article IV consultations** and country reports for GCC, Iran, Iraq, Lebanon, Jordan.
  - https://www.imf.org/en/Countries
- **World Bank** — country diagnostics, MNA region updates.
  - https://www.worldbank.org/en/region/mena

### Court records and enforcement

- **US PACER** — federal court filings, including civil forfeiture and criminal cases involving sanctions evasion.
- **DOJ press releases** for enforcement actions.
- **OFAC enforcement actions and settlement releases.**
- **DOJ National Security Division** announcements.

## Tiered secondary sources

**Tier 1 — major financial press:**
- Reuters, Bloomberg, Financial Times, Wall Street Journal.

**Tier 2 — specialized industry and regional:**
- **Energy and shipping:** S&P Global Platts, Argus Media, Lloyd's List, TradeWinds, gCaptain, Splash 247.
- **Iran-focused:** Bourse & Bazaar, Iran International (use cautiously, opposition-affiliated), Tasnim/Mehr/IRNA (state-aligned), Radio Farda.
- **Gulf-focused:** Arab Gulf States Institute Washington (AGSIW), The National (UAE), Arab News, Asharq Al-Awsat.
- **Middle East think tanks:** Middle East Institute (MEI), Atlantic Council Rafik Hariri Center, Brookings Doha Center, Carnegie Middle East Center, Chatham House MENA Programme, IISS.
- **Sanctions and compliance:** ACAMS Today, Sanctions and Export Controls Update, Lawfare.

**Tier 3 — regional press, blogs, social media:**
- Use only for color and source-of-source. Do not cite as a sole basis for legal, compliance, or sanctions claims.

## Source-handling rules

1. **Tier sources explicitly** in any output. "Reuters reported X" is a tier-1 reference; "industry sources told X publication" is tier-2 or tier-3.
2. **Do not blend secondary commentary into a primary-source claim.** If you cite OFAC, link OFAC, not a Reuters article that paraphrases OFAC.
3. **State retrieval date** for any time-sensitive source (sanctions designations, vessel data, oil prices, OPEC decisions). Designations and prices change.
4. **For Iran-related sources, declare orientation.** State media (Tasnim, IRNA, Mehr), opposition media (Iran International), and Western government-funded (Radio Farda) all carry orientation.

## Source freshness — re-verification horizons

Operational decisions require live source verification regardless of these horizons. The horizons below describe when a previously verified claim is presumed stale and must be re-checked before reuse.

| Claim type | Re-verify by |
|---|---|
| OFAC SDN designation status | Same-day for any operational claim. Within 7 days for analytical reuse. |
| EU/UK sanctions designation status | Same-day for operational. Within 7 days for analytical reuse. |
| OPEC+ production decisions or quotas | Within 30 days; faster around scheduled meetings. |
| Oil price levels (spot Brent, WTI) | Same-day for any planning use. |
| Vessel ownership, flag, AIS-derived patterns | Same-day for any sanctions/AML claim; unreliable beyond 24 hours for operational use. |
| FATF/MENAFATF mutual evaluation status | Within 12 months. |
| IMF Article IV consultations | Within 12 months of publication. |
| Central bank policy rates and dollar-auction parameters | Within 30 days; faster around policy meetings. |

If a claim from a source older than the horizon is reused, label it explicitly: `last verified [date]; re-verification required for operational use`.
