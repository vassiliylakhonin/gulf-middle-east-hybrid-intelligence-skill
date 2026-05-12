# OFAC Iran shipping-sector sanctions — exposure framing for a GCC-hub commodity trader

**Question:** What sanctions exposure does a commodity trader using UAE-based intermediaries face under the OFAC Iran shipping and energy sector sanctions regime?
**Decision:** Whether to tighten counterparty due diligence criteria, add provenance-documentation controls, or restructure payment rails for GCC-hub crude trades over the next 12 months.
**Audience:** Commodity trader sanctions compliance and trade-finance team.
**Time horizon:** 12 months, with structural overlay.
**Evidence mode:** `live-source-backed`.
**Primary sources retrieved:** See Source table below.
**Retrieval note:** Regulatory framework sources (E.O. texts, OFAC program page) are stable; entity-level SDN list state must be re-verified at each transaction. SDN list checked as of the retrieval date in the Source table; any entity-level claim not appearing in the SDN list row must be independently verified before operational use.
**Limitation note:** This is a decision-support brief. It is not legal advice, sanctions screening, or a compliance determination. Operational sanctions decisions require primary OFAC SDN List verification, qualified legal and compliance review, and entity-level screening against the OFAC, EU, and UK lists current as of the transaction date.

---

## Bottom line

The OFAC Iran shipping sanctions regime (E.O. 13846, E.O. 13902) covers Iranian shipping and shipbuilding sectors, petroleum and petrochemical product purchasers, and entities that provide material support to designated parties. For a GCC-hub commodity trader, the binding exposure is not the GCC jurisdiction itself but (a) whether counterparties trace to Iran-state or IRGC-affiliated entities through beneficial ownership, and (b) whether the cargo has Iranian-origin provenance that survives re-papering. The SDN list is the authoritative screen; no structural reasoning substitutes for it.

## Scope and evidence mode

`live-source-backed`. Primary sources retrieved and cited below. Mechanism analysis is structural (`Judgment`); entity-level conclusions require live SDN list verification by the reader.

## Primary sources

| Source | URL | Type | Re-verification horizon |
|---|---|---|---|
| OFAC Iran Sanctions program page | https://ofac.treasury.gov/sanctions-programs-and-country-information/iran-sanctions | Regulatory | Verify before each transaction; program guidance updates irregularly |
| OFAC SDN and Blocked Persons List (SDN List) | https://ofac.treasury.gov/specially-designated-nationals-and-blocked-persons-list-sdn-human-readable-lists | Entity list | Re-verify at each transaction; updated as designations are issued |
| E.O. 13846 — Reimposing Certain Sanctions With Respect to Iran (Aug 6, 2018) | https://home.treasury.gov/system/files/126/13846.pdf | Regulatory | Stable; re-read if program structure changes |
| E.O. 13902 — Sanctions on Iran's Shipping, Shipbuilding, Iron, Steel, Aluminum, Copper Sectors (Jan 10, 2020) | https://home.treasury.gov/system/files/126/13902.pdf | Regulatory | Stable; re-read if sector definitions change |
| OFAC General License guidance for Iran | https://ofac.treasury.gov/sanctions-programs-and-country-information/iran-sanctions#general-licenses | Regulatory | Verify before citing any license; general licenses are issued, amended, and revoked |
| OFAC FAQs: Iran-related | https://ofac.treasury.gov/faqs/topic/1541 | Guidance | Check for updates before compliance advice |
| Treasury press releases — Iran (OFAC actions) | https://home.treasury.gov/news/press-releases?field_keywords=Iran | Enforcement record | Monitor monthly; OFAC issues designations without fixed schedule |

**Retrieval date for above URLs:** 2026-05-12. SDN list state at that date is the baseline; re-verify before any transaction.

## Primary driver

`Primary driver (Judgment):` Extraterritorial reach of the OFAC Iran sanctions regime means any entity — including GCC-domiciled trading houses — that provides material support to, or transacts with, a Specially Designated National (SDN) faces blocking sanctions regardless of the transaction's jurisdiction.

## Mechanism

### Legal basis
- **E.O. 13846** restored broad Iran sanctions authority lapsed under JCPOA waiver. It authorises secondary sanctions on non-US persons who materially assist or transact with Iran in covered sectors. Petroleum and petroleum products are a covered sector.
- **E.O. 13902** added the Iranian shipping sector, shipbuilding sector, and specified metals sectors to the SDN designation framework. It authorises OFAC to designate any person who operates in those sectors, including foreign persons.

### Transmission channel for a GCC-hub commodity trader
1. Iranian-origin crude or blended crude with Iranian-origin component moves through a dark-fleet or STS-transfer chain and is re-papered as GCC-origin or "blend" cargo.
2. A UAE, Oman, or other GCC-hub entity — potentially on the SDN list or owned/controlled by an SDN — acts as the documentary counterparty.
3. The trader pays the GCC entity in USD through a correspondent bank. If the underlying transaction involves an SDN, the USD payment is a blocked transaction under OFAC rules regardless of the trader's intent.
4. Exposure transmits through: (a) direct deal with an SDN counterparty; (b) USD correspondent-bank processing of a blocked transaction; (c) reputational and regulatory exposure if post-hoc OFAC review identifies the cargo as Iranian-origin.

### Second-order effects
- Correspondent banks in New York are secondary exposure vectors: they are obligated to screen SDN names and may freeze or reject payments pending investigation.
- If an OFAC enforcement action names the trader's counterparty after the transaction, the trader may face retroactive disclosure obligations even without intent.
- Provenance documentation gaps become aggravating factors in OFAC enforcement; a voluntary self-disclosure program exists but requires legal coordination.

## Iran actor distinction

| Category | Relevance to this archetype |
|---|---|
| **Iran-state** (`Verified` regime type) | NIOC (National Iranian Oil Company) and NIORDC (National Iranian Oil Refining and Distribution Company) are SDN-listed. Trading with them directly is prohibited. |
| **IRGC-affiliated** (`Judgment` — requires entity-level verification) | IRGC-QF and affiliated entities control parts of Iran's shadow shipping fleet. Basis for affiliation claims: SDN list tags (IRGC, SDGT); public OFAC press releases naming networks. Do not assert IRGC affiliation without SDN list or primary-source basis. |
| **Iran-private commercial** (`Unknown — requires entity-level verification`) | Iranian private commercial firms are a heterogeneous category. Many are not designated; some are. Do not assume designation; verify against SDN list. |

## Exposure map

For a commodity trader operating through GCC hubs:

| Exposure concentration | Type | Control point |
|---|---|---|
| UAE free-zone trading-house counterparty | Counterparty SDN-list status | SDN screen at onboarding and periodically; enhanced due diligence on beneficial ownership |
| USD payment leg through New York correspondent | Correspondent-bank blocking risk | Correspondent bank screens independently; trader should screen before payment instruction |
| Cargo provenance — Iranian-origin crude re-papered | Cargo-origin risk | Provenance documentation depth: vessel history, STS transfer records, certificate of origin chain |
| Vessel — dark-fleet tanker used in STS transfer | Vessel SDN-list status | Vessel IMO number screen against SDN; maritime intelligence (Kpler, TankerTrackers, Windward) for AIS pattern |
| Re-export through third-country refinery | Secondary-sanctions exposure on refinery | Know-your-customer on refinery; OFAC enforcement actions on refineries are precedent |

Concentrated exposures for a typical GCC-hub crude trader: (1) thin-footprint UAE or Oman free-zone counterparties; (2) vessels without continuous AIS signal; (3) cargo documentation relying on counterparty certificates alone without independent provenance check.

## Actor incentives

| Actor | Incentive | Leverage point |
|---|---|---|
| OFAC | Enforce Iran sanctions, deter evasion, maintain secondary-sanctions deterrence | Designation authority; civil monetary penalties; voluntary self-disclosure discount |
| Iran (state) | Monetise petroleum exports; evade oil embargo | Layering through GCC hubs, re-papering, dark-fleet STS |
| IRGC-affiliated entities | Generate revenue for sanctioned network | Control parts of the shadow fleet; exploit thin-footprint front entities in GCC free zones |
| GCC-hub trading house (legitimate) | Access international commodity markets; avoid designation | Compliance programs; KYC on cargo origin; distance from Iranian-origin flows |
| GCC-hub trading house (sanctions-evasion) | Earn re-papering margin; channel Iranian oil to buyers | Thin documentation; rapid entity turnover; free-zone opaqueness |
| Western correspondent banks | Maintain USD clearing access; avoid OFAC penalties | Independent SDN screening; transaction monitoring; de-risking of high-risk commodity flows |

## Role-based implications

**Sanctions compliance team:**
- Screen counterparty at onboarding and at each transaction refresh against the OFAC SDN list (current as of transaction date).
- Require beneficial ownership disclosure to ultimate natural person; free-zone entities with opaque UBO are elevated-risk.
- Do not rely on counterparty-supplied certificates of origin as sole provenance documentation for Gulf-hub crude trades. Require vessel history (IMO number, AIS continuity, STS transfer records).
- Establish a defined escalation path for any new counterparty with documented connections to Iranian entities, vessels on the SDN list, or free-zone domicile with no operational substance.

**Trade-finance team:**
- Confirm USD payment leg: if any leg touches a blocked person or blocked property, the transaction is blocked regardless of the trader's location.
- New York correspondent banks will independently screen; coordinate with your bank's compliance team on any trade involving GCC-hub counterparties with Iranian-trade-adjacent activity.
- Where Iranian-origin cargo risk cannot be excluded, consider whether a payment structure avoiding USD clears the risk or simply shifts it.

## Trigger points and indicators

| Indicator | Source | Posture change if triggered |
|---|---|---|
| OFAC designates a new UAE/Oman/GCC-hub trading entity on the SDN list | OFAC press releases (https://home.treasury.gov/news/press-releases); OFAC SDN list | Immediate re-screen of all active counterparties; freeze any pending transactions with the named entity; legal review |
| OFAC enforcement action against a comparable trader for GCC-hub Iran-origin crude | OFAC enforcement actions page (https://ofac.treasury.gov/civil-penalties-and-enforcement-information) | Benchmark against own controls; consider voluntary disclosure if analogous exposure exists |
| Treasury OFAC updates FAQs or general licenses on Iran petroleum sector | OFAC FAQs Iran (https://ofac.treasury.gov/faqs/topic/1541) | Review for any scope change affecting permissible transactions or provenance documentation standards |
| Vessel used in recent trade appears on Kpler/TankerTrackers dark-fleet watch list or new IMO flag notice | Primary maritime intelligence vendors (Kpler, TankerTrackers, Windward, Lloyd's List Intelligence) | Escalate to legal; do not proceed with further trades involving that vessel pending verification |
| US-Iran diplomatic breakdown or new OFAC designation wave on Iran oil sector | OFAC press releases; US Treasury statements | Heightened counterparty re-screening cycle; reduce tolerance for thin-footprint counterparties |

## Unknowns

| Unknown | Impact |
|---|---|
| Beneficial ownership of specific GCC-hub trading-house counterparties | Unknown. Requires entity-level KYC and, where available, corporate registry search. Cannot be resolved by structural reasoning. |
| Current SDN list state for any specific entity | Unknown without live SDN list check. This memo does not name specific entities as designated or not designated; verify against the SDN list at the URL above. |
| US-Iran diplomatic trajectory and its effect on OFAC enforcement posture | Judgment-level uncertainty. Enforcement priority and designation tempo vary with diplomatic context. |
| Whether a specific cargo has Iranian-origin component | Unknown without independent vessel history and provenance documentation. |

## Confidence

**Overall confidence: Moderate.**

- **High confidence:** Regulatory framework (E.O. 13846, E.O. 13902) and their scope; OFAC SDN list as the authoritative entity screen; transmission mechanism (USD correspondent-bank blocking; SDN counterparty prohibition).
- **Moderate confidence:** Pattern of IRGC-affiliated entity activity in GCC hubs; dark-fleet STS re-papering as a primary evasion mechanism; free-zone entity risk as a concentration point. These patterns are well-documented in OFAC press releases and maritime intelligence reporting, but entity-level specifics require live verification.
- **Low confidence:** Current US-Iran diplomatic status and its near-term effect on OFAC enforcement tempo (structural uncertainty; changes without warning).

## What would change the judgment

| Evidence update | Direction of change |
|---|---|
| OFAC issues a General License broadly permitting certain Iran petroleum transactions | Reduces direct prohibition risk; scope and conditions of the license must be read precisely |
| Confirmed nuclear deal restoring JCPOA-era waivers | Would materially reduce near-term enforcement risk; would not remove SDN-list obligations until waivers are formally issued |
| Major OFAC enforcement action against a GCC-hub trading house with fact pattern matching the trader's own counterparties | Would raise urgency of voluntary self-disclosure review; would narrow any "I didn't know" defense |
| Primary maritime intelligence vendor flags the trader's vessel as IRGC-affiliated | Immediate escalation trigger; would change judgment from "screening risk" to "potential blocked transaction" |

## Limitation note

This is a `live-source-backed` decision-support brief, not a compliance determination or legal advice. Primary source URLs are cited and were retrieved on 2026-05-12; the SDN list changes without notice, and any entity-level claim requires re-verification against the live SDN list before operational use. This brief does not name specific entities as designated or not designated. Operational sanctions decisions require:
- primary OFAC SDN List screening (current as of transaction date);
- EU Consolidated List screening if EU nexus exists;
- UK OFSI Consolidated List screening if UK nexus exists;
- qualified legal and compliance review;
- entity-level KYC to beneficial ownership.

This brief does not constitute sanctions screening, AML transaction monitoring, or legal advice. It identifies structural risk patterns to support human analyst judgment.
