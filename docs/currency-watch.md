# Currency watch — Gulf + Middle East

An **active reminder** of fast-moving topics in the region that any source-backed memo should re-verify against current primary sources before relying on. This is **not** a database of current facts. The skill does not retrieve sources. Treat entries below as the list of *what to check now*, not as confirmed status.

**Last reviewed:** 2026-05-15
**Staleness rule:** any entry older than **90 days** must be re-verified before use. A stale watch list is worse than no watch list — it looks current while being wrong.

---

## How to use this file

1. Before writing a `live-source-backed` or `user-provided sources` memo, scan the topics below to see which ones touch the memo's scope.
2. For each touched topic, **re-verify against current primary sources** (per `docs/source-guide.md` source classes and freshness horizons).
3. If verification is not performed in the current session, label every claim derived from that topic with `[verify]` and downgrade the memo's evidence mode to `mixed` or `reasoning-only`.
4. When you update this file with a new finding, **update the Last reviewed date at the top** and the per-topic `Last reviewed` timestamp.

## How to maintain this file

- Add a topic when it becomes a recurring source of factual drift in memos.
- Remove a topic when it has stabilized (no material change for at least two horizons) or when it has resolved.
- Do **not** record specific designations, dates, vessel IMO numbers, prices, or numerical facts in this file. Those belong in memos with citation. This file records **what to watch**, not **what is currently true**.

---

## Iran sanctions and secondary-sanctions exposure

### Topic: OFAC Iran SDN evolution and General License changes
- **Why it matters:** Touches almost every Gulf banking, energy, shipping, and trade memo. Secondary-sanctions risk is the dominant exposure driver for Western counterparties with any Iran or Iran-adjacent activity.
- **What to re-verify:** Current SDN status of named counterparties; current vessel-list status of named ships; recent OFAC enforcement actions involving Iran; General Licenses and FAQs affecting Iran energy / financial sectors; Determinations under EO 13902 or successor authorities.
- **Where to verify:** OFAC SDN search; OFAC vessel list; OFAC recent actions; OFAC General Licenses and FAQs; State / Treasury joint statements.
- **Freshness horizon for derived claims:** 30 days, and always at point of operational decision.
- **Last reviewed:** [YYYY-MM-DD]

### Topic: EU and UK Iran sanctions divergence
- **Why it matters:** EU and UK regimes diverge from US on specific Iran designations and on the scope of sectoral measures. Memos for users with multi-jurisdictional exposure must not assume convergence.
- **What to re-verify:** Current EU consolidated list status; latest UK OFSI Iran designations; sectoral scope of EU Council decisions affecting Iran energy or finance.
- **Where to verify:** EU consolidated sanctions list; OFSI consolidated list and Iran-specific guidance.
- **Freshness horizon for derived claims:** 30 days.
- **Last reviewed:** [YYYY-MM-DD]

### Topic: IRGC and IRGC-affiliated entity scope
- **Why it matters:** IRGC FTO status, affiliated-entity designations, and front-company turnover create constant secondary-sanctions exposure. Memos must distinguish Iran-state, IRGC-affiliated, and Iran-private commercial actors throughout.
- **What to re-verify:** Recent IRGC-affiliated designations; recent enforcement actions naming IRGC fronts; State Department designations.
- **Where to verify:** OFAC recent actions filtered for IRGC; State Department designations; credible secondary reporting cross-checked against primaries.
- **Freshness horizon for derived claims:** 30 days for specific entity claims.
- **Last reviewed:** [YYYY-MM-DD]

### Topic: US-Iran negotiation status and nuclear file
- **Why it matters:** Affects sanctions-relief expectations, snapback risk, and Gulf-state political alignment. High volatility, low predictability. Overconfident forecasting on this file is explicitly listed as an anti-pattern in `AGENTS.md`.
- **What to re-verify:** Official statements (State, Treasury, EU, IAEA, Iran MFA); IAEA Board of Governors outputs; specific named-deal status.
- **Where to verify:** Official communiqué texts; IAEA reports; credible reporting cross-checked.
- **Freshness horizon for derived claims:** 1 month; treat any claim about negotiation status as **time-sensitive** and explicitly time-stamped.
- **Last reviewed:** [YYYY-MM-DD]

## Maritime chokepoints and shipping risk

### Topic: Houthi attacks and Bab-el-Mandeb / Red Sea security
- **Why it matters:** Attack frequency, target patterns (commercial vs naval; flag-state correlation), and convoy / re-routing posture affect shipping rates, insurance, and route choice. Snapshot claims age within weeks.
- **What to re-verify:** Recent UKMTO / IMSC advisories; Operation Prosperity Guardian or successor mission posture; insurance market premia patterns for Red Sea transits.
- **Where to verify:** UKMTO advisories; IMSC; flag-state advisories; credible shipping-trade press cross-checked.
- **Freshness horizon for derived claims:** 1 month for operational claims; 3 months for structural.
- **Last reviewed:** [YYYY-MM-DD]

### Topic: Hormuz incident pattern and Iranian seizure activity
- **Why it matters:** Iranian seizures of tankers, regional naval posture changes, and US-Iran maritime incidents affect insurance and routing for any Hormuz transit.
- **What to re-verify:** Recent named seizure incidents; CENTCOM and IRGC Navy posture statements; Hormuz transit advisories.
- **Where to verify:** UKMTO; CENTCOM releases; credible reporting cross-checked.
- **Freshness horizon for derived claims:** 3 months.
- **Last reviewed:** [YYYY-MM-DD]

### Topic: Dark-fleet and STS transfer patterns
- **Why it matters:** Sanctioned-crude flows, vessel-identity manipulation, and ship-to-ship transfer patterns shift continuously. Specific vessel claims age within weeks. Note: detection of dark-fleet activity is explicitly outside this skill's claimed capabilities (see `AGENTS.md`).
- **What to re-verify:** Specific vessel status in OFAC list; AIS gaps and re-flagging events from competent providers; sector enforcement actions naming vessels.
- **Where to verify:** OFAC vessel list; IMO GISIS; AIS providers (Kpler, Vortexa, Lloyd's List Intelligence, MarineTraffic); enforcement-action announcements.
- **Freshness horizon for derived claims:** 1 month; treat as time-sensitive for any vessel-level claim.
- **Last reviewed:** [YYYY-MM-DD]

## GCC banking, finance, and sovereign-wealth

### Topic: Correspondent banking posture toward GCC banks with Iran-adjacency exposure
- **Why it matters:** USD clearing access for GCC respondents with documented or suspected Iran-flow exposure shifts with each major US enforcement action and with shifts in correspondent appetite. Iraq banking sector is particularly volatile here.
- **What to re-verify:** Recent enforcement actions against correspondents serving the region; named-bank-level correspondent posture changes; CBI and CBI-adjacent central-bank statements.
- **Where to verify:** OFAC and DOJ enforcement actions; central bank communiqués (CBI, SAMA, CBUAE, QCB, CBK, CBB, CBO); credible secondary reporting cross-checked.
- **Freshness horizon for derived claims:** 6 months structural; immediately for any named-bank claim.
- **Last reviewed:** [YYYY-MM-DD]

### Topic: Iraq banking-sector reform and CBI dollar-auction structure
- **Why it matters:** CBI dollar-auction restrictions, named-bank suspensions, and FATF-driven AML reforms reshape Iraq financial-system risk. Volatile file.
- **What to re-verify:** Recent CBI statements on bank suspensions and auction structure; FATF / MENAFATF Iraq follow-ups; US Treasury actions affecting Iraqi banks.
- **Where to verify:** CBI press releases; FATF country page; OFAC; credible secondary cross-checked.
- **Freshness horizon for derived claims:** 3 months.
- **Last reviewed:** [YYYY-MM-DD]

### Topic: Sovereign-wealth deployment posture (PIF, ADIA, Mubadala, QIA, KIA)
- **Why it matters:** Mandates, leverage on portfolio companies, and political alignment with US/EU/China shift with regional priorities and ruling-family dynamics. Specific deal claims age fast.
- **What to re-verify:** Recent annual reports and disclosures where available; specific named-deal announcements; political-context shifts.
- **Where to verify:** SWF official disclosures; portfolio company announcements; credible financial reporting cross-checked.
- **Freshness horizon for derived claims:** 6 months structural; 1 month for specific deals.
- **Last reviewed:** [YYYY-MM-DD]

### Topic: MENAFATF country status and AML posture
- **Why it matters:** Mutual evaluation outcomes, follow-ups, and rating changes affect EDD requirements and correspondent posture toward in-scope jurisdictions.
- **What to re-verify:** Latest MENAFATF plenary statements; specific country MER / follow-up status; FATF public statements.
- **Where to verify:** MENAFATF reports and statements; FATF country pages.
- **Freshness horizon for derived claims:** 3 months follow-ups, 12 months MER findings.
- **Last reviewed:** [YYYY-MM-DD]

## Energy markets and OPEC+

### Topic: OPEC+ production posture and Saudi-led coordination
- **Why it matters:** Production decisions, quota changes, and KSA / UAE / Russia coordination affect price expectations and Gulf state fiscal balance. Volatile file.
- **What to re-verify:** Latest OPEC and OPEC+ communiqués; MOMR; specific country quota changes; sector reporting cross-checked.
- **Where to verify:** OPEC and OPEC+ statements; MOMR; IEA OMR; credible secondary cross-checked.
- **Freshness horizon for derived claims:** 1 month for production decisions; 3 months for structural framing.
- **Last reviewed:** [YYYY-MM-DD]

### Topic: Iran crude export volumes and destination patterns
- **Why it matters:** Sanctioned-crude flows, destination concentration (China dominance), and STS-laundering patterns affect enforcement and secondary-sanctions exposure analysis.
- **What to re-verify:** Specific volume estimates from competent providers (Kpler, Vortexa); IEA OMR mentions; US Treasury enforcement actions naming specific flow patterns.
- **Where to verify:** Paid AIS / flow-data providers; IEA OMR; OFAC enforcement actions.
- **Freshness horizon for derived claims:** 3 months for structural patterns; 1 month for volume claims.
- **Last reviewed:** [YYYY-MM-DD]

### Topic: LNG and gas export developments (Qatar, UAE, Israel-Mediterranean)
- **Why it matters:** Project sanctions, capacity expansions, and offtake structures affect medium-term energy procurement and counterparty-risk analysis.
- **What to re-verify:** Project-level announcements; specific offtake-deal disclosures; ministry-of-energy publications.
- **Where to verify:** Operator and ministry publications; IEA / IGU reports.
- **Freshness horizon for derived claims:** 6 months.
- **Last reviewed:** [YYYY-MM-DD]

## Regional security and political alignment

### Topic: Israel-Gulf normalization and Abraham Accords trajectory
- **Why it matters:** Normalization steps, deal pauses, and regional alignment affect business risk and reputational risk for Western counterparties with Gulf and Israeli relationships.
- **What to re-verify:** Latest official statements; specific named-deal status; sector developments in defense, tech, and energy crossings.
- **Where to verify:** Official communiqués; credible reporting cross-checked.
- **Freshness horizon for derived claims:** 3 months.
- **Last reviewed:** [YYYY-MM-DD]

### Topic: Iranian proxy network activity (Hezbollah, Iraqi militias, Houthis)
- **Why it matters:** Affects sanctions-screening scope, country-risk premia, and specific transit-route risk. Highly dynamic.
- **What to re-verify:** Recent OFAC and Treasury designations naming proxy-network entities; specific incident reporting; sector enforcement actions.
- **Where to verify:** OFAC recent actions; Treasury press releases; credible reporting cross-checked.
- **Freshness horizon for derived claims:** 3 months for structural; 1 month for specific incidents.
- **Last reviewed:** [YYYY-MM-DD]

---

## What this file is not

- Not a database of current sanctions designations, vessel IMO numbers, prices, throughput numbers, or designation dates. Those belong in memos with citation.
- Not a substitute for `docs/source-guide.md`, which classifies source tiers and lists freshness horizons by claim type.
- Not legal, sanctions, AML, vessel-screening, or operational advice. The skill does not perform sanctions screening, vessel screening, or live retrieval by itself.
