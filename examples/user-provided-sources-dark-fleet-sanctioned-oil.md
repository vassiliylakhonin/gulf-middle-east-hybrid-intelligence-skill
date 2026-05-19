# Dark-fleet / sanctioned-oil flow exposure for a refiner or trader (user-provided sources)

> **Evidence mode: `user-provided sources`.**
>
> **Skeleton-packet retrieval date (mandate-page URLs only): 2026-05-15.** Each U-tagged source below is a canonical regulator, IFI, or operational mandate page; the URLs were checked for accessibility on 2026-05-15 but no point-in-time content was extracted. The user is expected to perform their own retrieval of point-in-time content (current OFAC vessel designations, current EU/UK/Swiss listings, current price-cap attestation guidance, current OFAC maritime advisories) at the point of decision; those retrievals become the binding evidence.
>
> **This memo is delivered as a skeleton-packet structural framing.** The user (a refining company's commercial / compliance / trade-finance team, or an oil trader's risk and financing leadership) supplies the binding operational facts. The memo's structural analysis composes with whatever the user retrieves — it does **not** state current OFAC vessel designations, IMO numbers, AIS observations, price-cap attestation status, or named counterparties on its own authority.
>
> This memo is illustrative analysis. It is **not** legal, sanctions, AML, vessel-screening, maritime due-diligence, marine insurance, or investment advice. It does not screen any vessel, counterparty, or cargo against any list, and it does not assert specific vessel names, IMO numbers, ownership chains, or AIS-derived patterns.

**Question:** A refining company or an oil trader is reviewing its 2026–2027 framework for exposure to crude / fuel oil / condensate cargoes that may have dark-fleet or sanctioned-origin adjacency (Iran-, Russia-, or Venezuela-origin oil; sanctioned vessels in the voyage chain; STS-transfer or origin-obscuring patterns). What is the structural risk shape it should price into counterparty screening, voyage acceptance, attestation discipline, and policy — independent of any single vessel designation event?

**Decision:** Counterparty acceptance and tiering; voyage and cargo acceptance criteria; attestation and documentation discipline; insurance and trade-finance posture; board-level appetite for adjacency exposure.

**Audience:** Refining company's commercial, compliance, and trade-finance leadership; oil trader's risk, compliance, and financing leadership.

**Time horizon:** 12 months, with structural overlay through 2027.

**Limitation note:** See top. Structural reasoning only; not a vessel-screening framework, not a price-cap compliance tool, not legal advice.

## User-provided source packet (skeleton)

The user is expected to retrieve current content from these canonical mandate pages and supply the retrievals as the binding evidence base. Within this memo, only items the user has retrieved from these pages may be treated as factual at the point of decision.

- **[U1]** OFAC Sanctions List Search (vessel filter available) — https://sanctionssearch.ofac.treasury.gov/ — for current designations of any specific vessel by name or IMO number.
- **[U2]** OFAC Iran sanctions program — https://ofac.treasury.gov/sanctions-programs-and-country-information/iran-sanctions — for current Iran-program directives, including secondary-sanctions doctrine on Iran-origin petroleum.
- **[U3]** OFAC Russia-related sanctions (price-cap regime) — https://ofac.treasury.gov/sanctions-programs-and-country-information/russian-harmful-foreign-activities-sanctions — for current price-cap guidance, attestation requirements, and General Licenses.
- **[U4]** US Treasury Price Cap Coalition guidance — https://home.treasury.gov/policy-issues/financial-sanctions/sanctions-programs-and-country-information/russian-harmful-foreign-activities-sanctions — for current G7 / Coalition attestation framework and recordkeeping standards.
- **[U5]** OFAC Sanctions Compliance Guidance for the Maritime Industry — https://ofac.treasury.gov/recent-actions and OFAC compliance advisories archive — for current maritime advisories on deceptive shipping practices (AIS manipulation, STS-transfer red flags, flag-hopping, falsified documentation).
- **[U6]** EU consolidated financial sanctions list and EU oil-related guidance — https://www.sanctionsmap.eu/ — for current EU designations and price-cap guidance.
- **[U7]** UK OFSI consolidated list and UK Price Cap Coalition guidance — https://www.gov.uk/government/publications/financial-sanctions-consolidated-list-of-targets — for current UK designations and attestation requirements.
- **[U8]** Swiss SECO consolidated list — https://www.seco.admin.ch/seco/en/home/Aussenwirtschaftspolitik_Wirtschaftliche_Zusammenarbeit/Wirtschaftsbeziehungen/exportkontrollen-und-sanktionen/sanktionen-embargos.html — for current Swiss designations relevant to Swiss-based trading desks.
- **[U9]** IMO Global Integrated Shipping Information System (GISIS) — https://gisis.imo.org/ — for current vessel registry status (flag, ownership-of-record, IMO number lookup). Note: GISIS reflects what is filed; sanctioned actors often misrepresent.
- **[U10]** International Group of P&I Clubs — https://www.igpandi.org/ — for current P&I coverage posture on sanctioned-cargo voyages and attestation expectations.
- **[U11]** FATF and MENAFATF reports relevant to Gulf hub jurisdictions — https://www.fatf-gafi.org/ and https://www.menafatf.org/ — for current AML/CFT findings touching Iran-adjacency and Gulf trade-finance hubs.

Where the user has not yet retrieved a packet item, the corresponding claim category in this memo is `Unknown` and triggers `Stop and request` per the three-value response logic (see end of memo). The structural framing below is `[analyst-judgment]` / `[inference]` and does not depend on the packet contents.

## Bottom line

`[analyst-judgment]` For a refiner or oil trader, the binding 2026–2027 exposure on dark-fleet / sanctioned-oil flow is **not** any single vessel designation. It is the **distribution of secondary-sanctions, price-cap-breach, insurance-void, banking-rail, and cargo-seizure risk** across a small number of recurring **deceptive-practice patterns** that compound when they appear in the same voyage chain. A counterparty-screening framework built around per-vessel list checks under-prices the joint distribution. A framework built around the **deceptive-practice patterns** prices it correctly, and an **attestation discipline** built around the price-cap regime closes the documentation gap that enforcement actions exploit.

Six channels carry the exposure into the refiner / trader book: (1) OFAC SDN exposure on a vessel, owner, manager, charterer, or cargo-related counterparty; (2) secondary-sanctions exposure on the facilitator chain (lifting, freight, finance, insurance); (3) price-cap-regime breach with attestation failure as the proximate cause; (4) P&I and hull-insurance coverage void; (5) trade-finance and correspondent-bank rail loss; (6) cargo seizure or detention at port. The right response is a **pattern-aware tiered framework** with explicit Stop-and-request triggers on attestation gaps, not a per-name screen upgrade.

## Scope and evidence mode

`user-provided sources`. The packet skeleton above defines the boundary of factual authority. Structural patterns described below reflect publicly documented post-2022 sanctions and price-cap enforcement guidance and standard maritime-compliance frameworks `[secondary][verify against U1–U11 retrievals]`. Specific vessel designations, current enforcement posture, current AIS-pattern observations, current P&I posture, and named counterparties are **not stated** by this memo — they must come from the user's retrievals of [U1]–[U11] and from licensed maritime-intelligence providers operating outside the scope of an AI-skill repository.

Cross-region note: Central Asian / Caspian onshore routing exposure (Russia-bound or Russia-origin flow through the Caspian / Middle Corridor) is covered in the [`central-asia-caspian-hybrid-intelligence-skill`](https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill) repo; this memo references it for the upstream-routing dimension but does not duplicate it.

## Primary driver

`Primary driver [analyst-judgment]:` Post-2022 sanctions enforcement has produced three structurally durable patterns: (a) a **growing pool of dark-fleet vessels** operating outside mainstream P&I and flag-registry discipline to service Iran-, Russia-, and Venezuela-origin oil flows; (b) **deceptive-practice typologies** (AIS manipulation, STS transfers in opaque waters, flag-hopping, falsified bills of lading, blending and origin re-labeling) that have stabilized into recognizable patterns; (c) **price-cap regime enforcement** focused on attestation discipline more than on absolute price proof — making the **documentation chain** the load-bearing control.

The binding driver is not "more vessels are sanctioned" (an over-generic claim); it is **the maturation of deceptive-practice typologies into recurring patterns**, combined with **attestation-centric enforcement doctrine** that places the documentation burden squarely on the refiner / trader and their bank.

## Why now

`[analyst-judgment]` Three structural reasons make 2026–2027 the relevant horizon:

1. Deceptive-practice typologies are well-documented in OFAC maritime advisories `[secondary][verify against U5]` and in the IGP&I guidance ecosystem `[secondary][verify against U10]`; refiners and traders responding only to incidents and not to typologies are operating below the enforcement-doctrine state of the art.
2. The G7 / Price Cap Coalition attestation regime has shifted from a price-evidence regime to a **records-and-attestation regime** `[secondary][verify against U4, U7]`; the locus of breach is now the documentation chain, not the trade price.
3. P&I insurance markets and major flag registries have hardened their posture against dark-fleet vessels `[secondary][verify against U10]`; the **insurance-void** transmission channel has moved from a soft to a hard risk.

## Mechanism

### The three deceptive-practice patterns

1. **AIS manipulation and chokepoint dark behavior.** A vessel goes "dark" on AIS during loading, STS transfer, or transit in zones where dark behavior is operationally plausible (Persian Gulf, Strait of Hormuz approaches, eastern Mediterranean, west Africa, north Indian Ocean). AIS gaps are not in themselves proof; they are a *flag for source verification*. Refiners and traders need a pattern-aware reading of AIS gaps, not a binary "AIS-on = safe" model `[analyst-judgment]`.
2. **STS transfers in opaque waters.** Ship-to-ship transfers off non-cooperative coasts or in waters with low enforcement density are a typology used to break the chain of custody. The lifted cargo enters the legitimate fleet via a clean-looking voyage from the receiving vessel; the originating cargo's chain of custody is lost. Pre-cleared STS protocols and STS-transfer attestations in the documentation chain are the control point.
3. **Flag-hopping, registry-cleanup, and ownership opacity.** Vessels change flag and registered owner-of-record at frequencies inconsistent with normal commercial vessel lifecycle. Flag registries of convenience that have hardened (most major ones publicly tightened) drive the flow toward small-state or opaque registries. The signal is **registry-change frequency**, not the current registry alone.

`[inference]` The dark-fleet risk is the **product**, not the sum, of these patterns. A vessel with one pattern is an elevated-risk case. A voyage with two or three patterns is a different risk category. Apply pattern-density, not single-feature, scoring.

### The Iran actor distinction

Apply the Gulf + Middle East skill's Iran actor distinction whenever an Iran-touching cargo, vessel, or counterparty is in scope:

- **Iran-state actors** (NIOC, NITC, Iranian government ministries) — directly blocked under OFAC Iran program; voyage- or cargo-chain involvement should be treated as refuse-or-Stop-and-request, not as a tier upgrade.
- **IRGC-affiliated entities** — SDN-designated; basis of affiliation must be stated when claimed (designation, public reporting, network inference); same refuse-or-Stop-and-request posture as Iran-state at the operational level, with a higher bar for inference claims.
- **Iran-private commercial actors** — not categorically blocked; designation status varies; requires entity-level SDN screen via [U1].

Do not aggregate the three categories. The cargo / vessel / counterparty exposure differs across them, and the enforcement narrative differs as well.

### Transmission to refiner / trader exposure

For a refiner or trader, exposure transmits through:

- **OFAC SDN exposure** on a vessel, owner, manager, charterer, cargo-related counterparty, or facilitator anywhere in the voyage chain `[secondary][verify against U1, U2, U3]`. SDN exposure on any node in the chain blocks the whole flow.
- **Secondary-sanctions exposure** on the facilitator network — finance, freight, insurance, brokerage. Even non-US refiners and traders carry secondary-sanctions exposure under US doctrine `[secondary][verify against U2, U3]`.
- **Price-cap-regime breach** with attestation failure as the proximate cause `[secondary][verify against U4, U7]`. The breach can occur on otherwise-legitimate Russia-origin flow if the attestation chain is broken.
- **P&I and hull-insurance void** on a voyage where the dark-fleet pattern crystallizes mid-voyage `[secondary][verify against U10]`. The exposure is not only at booking; coverage can be void retrospectively on a finding of false declaration.
- **Trade-finance and correspondent-bank rail loss.** Letter-of-credit confirmations and trade-finance facilities tier their respondent exposure by deceptive-practice pattern; respondent traders / refiners can face rail tightening absent any designation.
- **Cargo seizure or detention at port** — port-state control authorities and downstream-jurisdiction customs can detain on suspicion of sanctions adjacency, with the burden on the cargo owner to prove origin.
- **Reputational concentration** — a single named enforcement action against a refiner or trader in a deceptive-practice pattern propagates across the firm's wider book and into board-level exposure.

## Exposure map

| Exposure concentration | Type | Control point | Provenance |
|---|---|---|---|
| Pattern-density voyages not visible in per-vessel screening | Sanctions / secondary-sanctions risk | Pattern-aware EDD on voyage chain (independent of named-vessel screening) | `[analyst-judgment]` |
| Attestation-chain gaps under G7 price cap | Price-cap compliance | Attestation discipline; documentation completeness; recordkeeping window | `[analyst-judgment]` |
| P&I and hull-coverage void on a dark-fleet finding | Insurance / commercial risk | Pre-voyage P&I confirmation; coverage-void scenarios stress-tested | `[analyst-judgment]` |
| Trade-finance / correspondent-bank rail loss | Operational / commercial risk | Diversified financing; defensive disclosure to correspondents on pattern controls | `[analyst-judgment]` |
| Cargo seizure at port | Operational / commercial risk | Pre-loading chain-of-custody documentation; port-state control intelligence | `[analyst-judgment]` |
| Iran actor mis-categorization | Sanctions / OFAC SDN risk | Apply Iran actor distinction taxonomy; refuse on Iran-state and IRGC-affiliated nexus; case-by-case on Iran-private commercial | `[analyst-judgment]` |
| Reputation cascade from a single enforcement action | Reputation / governance risk | Board-level limits on pattern-density concentration | `[analyst-judgment]` |

`[analyst-judgment]` Concentrated exposures for a typical refiner / trader: (1) screening systems priced on per-vessel list checks rather than pattern density; (2) attestation discipline weaker than the regime's evidentiary expectations; (3) insurance and finance assumed available rather than confirmed per voyage.

## Actor incentives

| Actor | Incentive | Leverage point | Provenance |
|---|---|---|---|
| Sanctioned-origin seller (Iran-state, Russia-state, Venezuelan PdVSA or proxies) | Maintain export volume despite sanctions environment | Dark-fleet capacity provision; intermediary network depth; documentation falsification | `[analyst-judgment]` |
| Dark-fleet vessel operator | Capture margin premium on sanctioned voyages | AIS manipulation, STS infrastructure, flag-hopping, registry obfuscation | `[analyst-judgment]` |
| Intermediary trader / brokerage | Capture margin on origin-obscuring intermediation | Chain-of-custody opacity; multiple intermediation layers | `[analyst-judgment]` |
| Refiner | Maintain feedstock supply at acceptable risk-adjusted return | Counterparty screening; voyage acceptance criteria; cargo origin verification | `[analyst-judgment]` |
| Oil trader | Capture trading margin; preserve banking and insurance rails | Pre-trade pattern screening; attestation discipline; rail-relationship management | `[analyst-judgment]` |
| P&I and hull insurer | Avoid claims on void coverage; maintain market discipline | Coverage-issuance discipline; voyage-specific declarations | `[analyst-judgment]` |
| Trade-finance bank | Avoid downstream exposure to deceptive-practice voyages | Pre-trade screening; respondent tiering; attestation requirements | `[analyst-judgment]` |
| US / EU / UK enforcement | Deter dark-fleet construction; impose cost on willful blindness | Designations; enforcement actions; maritime advisories | `[analyst-judgment]` |
| Gulf hub jurisdictions (UAE, Oman, others) | Balance commercial throughput against secondary-sanctions risk to domestic financial sector | Port-state controls; FATF / MENAFATF posture; licensing of intermediaries | `[analyst-judgment]` |

## Role-based implications

**Refining company commercial / compliance leadership:**
- Build a **pattern-density screen** at cargo acceptance: AIS history of the loading and discharge vessels, STS history, flag-change frequency, ownership opacity. Treat the screen as additive to per-vessel list checks, not as a replacement.
- Pre-agree refuse-or-Stop-and-request triggers with the commercial desk so escalation is not ad-hoc when a multi-pattern voyage arrives.
- Maintain **attestation discipline** under the price-cap regime as a documentation-completeness check — the breach surface is the documentation chain, not the trade.

**Oil trader risk / compliance leadership:**
- Same pattern-density screen at voyage authorization; add **broker-network screening** because origin-obscuring patterns often run through specific intermediation layers.
- Maintain a **STS-transfer policy** — pre-approved cooperating waters and protocols, refuse outside that set without compensating controls.
- Treat insurance and trade-finance rail loss as a **P&L line** risk; price the optionality of rail diversification into commercial decisions.

**Trade-finance bank (working with refiner / trader counterparties):**
- Apply pattern-density screening at trade-finance authorization; for facilities, build trigger-based reductions on rising pattern density across the counterparty's book.
- Demand attestation-package completeness as a documentary condition, not as a comfort check; price the documentary gap as a credit issue.

**Board risk committee:**
- Add **pattern-density concentration** to the standing risk dashboard. A refiner / trader can be SDN-clean and still rail-exposed and reputation-exposed on pattern grounds.
- Set an explicit appetite ceiling on pattern-density exposure; require named approval below threshold.

## Trigger points and indicators

| Indicator | Source category | Posture change if triggered | Provenance |
|---|---|---|---|
| New OFAC vessel designation in a voyage chain touched by the firm | OFAC SDN updates `[verify against U1]` | Immediate freeze on the named vessel; review voyage chain for related vessels / owners / managers | `[user-provided][verify]` |
| Price-cap-regime change (attestation requirements, recordkeeping window) | US Treasury Price Cap Coalition guidance `[verify against U4, U7]` | Refresh attestation packs; engage compliance and legal on documentary changes | `[user-provided][verify]` |
| New OFAC maritime advisory on deceptive shipping practices | OFAC compliance advisories `[verify against U5]` | Incorporate the named typology into pattern-density screen; brief desk and compliance | `[user-provided][verify]` |
| P&I market guidance change on dark-fleet voyages | International Group of P&I Clubs `[verify against U10]` | Re-confirm coverage on active voyages; review pre-voyage P&I confirmation protocol | `[user-provided][verify]` |
| Port-state control enforcement action against a sanctioned-adjacent cargo | Port-state authority releases, credible reporting cross-checked `[verify]` | Review the firm's recent activity in that port; pre-emptive engagement with port agents | `[analyst-judgment][verify]` |
| Material change in Iran-related secondary-sanctions doctrine | OFAC Iran program `[verify against U2][stale-risk: at point of decision]` | Re-evaluate Iran-conduit pattern weight; treat conservatively until guidance assessed | `[user-provided][verify]` |
| FATF / MENAFATF action against a Gulf hub jurisdiction | FATF / MENAFATF mutual-evaluation outputs `[verify against U11]` | Re-tier intermediary and trade-finance counterparties domiciled in the named jurisdiction | `[user-provided][verify]` |
| Public reporting of a specific enforcement action against a refiner / trader for dark-fleet adjacency | Treasury / DOJ / OFSI / OFAC press; credible reporting cross-checked `[verify]` | Stress-test the firm's exposure to the named pattern; engage with legal and PR proactively | `[analyst-judgment][verify]` |

## Unknowns

| Unknown | Impact | Provenance |
|---|---|---|
| Current SDN status of any specific vessel, owner, or counterparty | Time-sensitive; requires live OFAC SDN search at point of decision (U1) | `[analyst-judgment]` |
| Current G7 price-cap attestation requirements and recordkeeping window | Time-sensitive; requires live retrieval from U4 / U7 | `[analyst-judgment]` |
| Current OFAC maritime advisory state and typology list | Time-sensitive; requires live retrieval from U5 | `[analyst-judgment]` |
| Current P&I market posture on a specific voyage | Voyage-specific; not publicly stated; needs direct insurer engagement | `[analyst-judgment]` |
| Current AIS-derived patterns on a specific vessel or chokepoint | Time-sensitive; requires licensed maritime-intelligence provider — outside the skill's authority | `[analyst-judgment]` |
| Current enforcement-narrative tilt (active flags, registries, intermediary chains) | Drives where the next named action lands; structural reasoning cannot price the specific landing point | `[analyst-judgment]` |
| Trajectory of US-Iran negotiation file and direct effect on Iran-origin oil flow | Structural uncertainty with high pattern-weight implication | `[analyst-judgment]` |

## Confidence

**Overall confidence: Moderate.**

- **High confidence (structural):** the existence and durability of the three deceptive-practice patterns post-2022 `[secondary][verify]`; the six transmission channels into refiner / trader exposure; the inadequacy of pure per-vessel screening for joint-pattern risk.
- **Moderate confidence (analyst-judgment):** the role-based priority ranking proposed above; the relative weight of OFAC SDN exposure vs price-cap breach vs P&I void vs rail loss. A firm's actual weighting depends on book composition (own-account vs. third-party voyages; long-term contracts vs. spot; refining vs. trading).
- **Low confidence (not retrieved):** any specific current designation, current price-cap attestation requirement, current OFAC maritime advisory state, current P&I posture, current AIS-derived observation. Each requires live retrieval at point of decision.

This memo's confidence ceiling is moderate because no primary sources were retrieved and AIS-derived observations are outside the skill's authority. A higher-confidence brief requires live retrieval of OFAC / EU / UK / Swiss consolidated lists, current price-cap guidance, current maritime advisories, and licensed maritime-intelligence data.

## What would change the judgment

| Evidence update | Direction of change | Provenance |
|---|---|---|
| Enforcement action against a refiner or trader for dark-fleet adjacency in a Gulf-hub context | Increases urgency; pattern-density screening becomes mandatory baseline control across the sector | `[analyst-judgment]` |
| Material relaxation of Iran secondary-sanctions doctrine | Iran-conduit pattern weight decreases; dark-fleet risk shape shifts to Russia- and Venezuela-origin patterns | `[analyst-judgment]` |
| Material tightening of G7 price-cap attestation regime | Documentation discipline becomes table-stakes; the attestation gap becomes the dominant breach vector | `[analyst-judgment]` |
| Public hardening of P&I and hull insurance posture against dark-fleet voyages | Insurance-void transmission channel becomes binding constraint on dark-fleet commercial viability | `[analyst-judgment]` |
| FATF / MENAFATF action against a Gulf hub jurisdiction central to the intermediary network | Respondent-tiering posture across trade-finance banks tightens; intermediary chains re-route | `[analyst-judgment]` |
| Material change in major flag registries' dark-fleet posture | Registry-of-convenience supply contracts; flag-hopping pattern shifts to smaller / opaque registries | `[analyst-judgment]` |

## Three-value response logic — application to this memo

This memo applies the three-value logic from AGENTS.md as follows:

- **Answer (used):** structural risk shape; six transmission channels; three deceptive-practice patterns; role-based implications; trigger-point framework. Sufficient basis exists from publicly documented post-2022 OFAC maritime advisories, price-cap regime guidance, and P&I market posture `[secondary][verify]`.
- **Flag-but-don't-use (used):** specific enforcement-doctrine direction; current price-cap attestation requirement state; current P&I market posture on dark-fleet voyages. Acknowledged as uncertain; not used as a load-bearing input to the structural reasoning.
- **Stop and request (would apply):** any operational decision on a specific vessel, voyage, cargo, or counterparty requires source-backed re-verification (U1–U11) and qualified maritime-compliance and legal review, not this memo. A refiner or trader applying this memo to a real voyage decision should Stop and request live retrieval and licensed maritime-intelligence input before acting.

## Limitation note

This is a `user-provided sources` decision-support brief delivered as a skeleton packet plus structural framing. **The binding evidence is the user's retrieval of [U1]–[U11] and licensed maritime-intelligence data at the point of decision.** This memo does not retrieve those items itself, does not perform vessel screening, does not perform AIS analysis, and does not constitute maritime due diligence. It is not legal, sanctions, AML, price-cap compliance, vessel-screening, marine-insurance, or investment advice. It does not state any current vessel designation, IMO number, ownership chain, AIS observation, or named counterparty. It does not constitute an opinion on whether any specific voyage, cargo, or counterparty is permissible under any sanctions or price-cap regime.

Any operational application requires, at minimum:
- live retrieval from OFAC, EU consolidated, UK OFSI, and Swiss SECO at the point of decision;
- current OFAC maritime advisory state and current price-cap attestation guidance;
- licensed maritime-intelligence provider input for AIS-derived patterns, vessel ownership chains, and STS-transfer histories;
- qualified sanctions and maritime counsel review for any specific voyage in scope;
- P&I and hull insurer pre-voyage engagement;
- trade-finance counterparty engagement on attestation-package completeness.

This memo identifies structural patterns to support human refining / trading commercial, compliance, and risk-committee judgment. It does not replace any of the above.
