# Gulf + Middle East Hybrid Intelligence

This context defines the language for the Gulf + Middle East vertical specialist inside the broader Agenda Intelligence stack. It exists to keep regional reasoning, evidence discipline, actor distinctions, and validation boundaries distinct.

## Language

**Vertical Specialist**:
A regional reasoning skill that adds Gulf, Iran, Iraq, and maritime-chokepoint domain depth to a strategic-risk agent workflow.
_Avoid_: Platform, MCP server, validation engine, sanctions-screening or vessel-screening tool

**Agenda Intelligence MD**:
The product shell and evidence-discipline layer that validates, audits, scores, and routes strategic-risk agent outputs.
_Avoid_: Parent skill, source retriever, factual verifier, compliance product

**Global Think Tank Analyst**:
The general strategic-risk reasoning method for policy-risk memos, scenarios, red-team framing, and broad analytical workflow.
_Avoid_: Regional specialist, source validator, Gulf doctrine

**Central Asia + Caspian Hybrid Intelligence Skill**:
The sibling vertical specialist. Reference it when a flow crosses both regions (Iran-Caspian routes, Russia-Iran-China junction, Iraq-Kurdistan corridors, Central Asian energy routed through Gulf hubs). Do not duplicate its CA-specific content here.
_Avoid_: Replacement, fork, merge target

**Regional Lens**:
A packaged regional frame used by Agenda Intelligence MD to route geography-specific analysis when `analyze` sees a Gulf / Middle East / chokepoint geography.
_Avoid_: Full specialist repo, source database, standalone analyst

**Regional Mechanism Logic**:
The Gulf-specific explanation of how risk transmits through Iranian state vs IRGC-affiliated vs Iran-private commercial actors, GCC correspondent banking, sovereign wealth deployment, OPEC+ behavior, shipping and dark-fleet patterns, Houthi / Red Sea events, and US-Iran negotiation status.
_Avoid_: Generic Middle East commentary, universal strategy framework, geopolitical essay structure

**Iran-state actor**:
The Iranian government and its formal institutions (ministries, central bank, NIOC, IRISL).
_Avoid_: Conflation with IRGC-affiliated entities, conflation with Iran-private commercial actors

**IRGC-affiliated actor**:
Entities under direct IRGC control or designated as such by relevant sanctions regimes (e.g., IRGC-QF networks, IRGC-linked front companies).
_Avoid_: Conflation with Iran-state ministries, conflation with private commercial firms, blanket "Iran-linked" framing

**Iran-private commercial actor**:
Private Iranian firms operating in commercial sectors without documented IRGC or state ownership. May still face secondary-sanctions exposure depending on counterparty and sector.
_Avoid_: Conflation with Iran-state or IRGC actors; assumption of sanctions-listed status without verification

> Collapsing the Iran-state / IRGC-affiliated / Iran-private commercial distinction is an explicit **Stop-and-request** trigger per `AGENTS.md`. Exposure analysis must specify which actor type is involved before proceeding.

**Maritime Chokepoint**:
A waterway where vessel transit risk materially changes regional exposure: Strait of Hormuz, Bab-el-Mandeb, Red Sea / Suez approaches. Excludes incidental traffic through other waterways unless tied to a Gulf/Iran flow.
_Avoid_: Generic shipping-route framing, conflation with port congestion, vague "regional tensions"

**Sovereign Wealth Deployment Risk**:
Exposure analysis for transactions involving PIF, ADIA, Mubadala, QIA, KIA — focused on counterparty diligence, sector concentration, governance, US-China-EU policy exposure, and reversal risk.
_Avoid_: Generic SWF marketing material, asset-allocation commentary without decision frame

**Dark-fleet / Sanctioned-oil Flow**:
The risk pattern around vessels and trade routes used to move sanctioned crude (notably Iranian and Russian) outside G7 price-cap discipline. The skill provides structural framing (deceptive-practice patterns, transmission channels, attestation discipline) but does NOT assert vessel-specific IMO numbers, AIS observations, or designations on its own authority.
_Avoid_: Vessel-screening claim, dark-fleet detection claim, AIS-derived assertion without licensed maritime-intelligence source

**Currency Trigger**:
The rule that web search or primary-source verification is required (not optional) when the question involves current sanctions designations, recent enforcement, maritime/chokepoint events, vessel-specific claims, US-Iran negotiation status, or OPEC+ decisions. If verification is not possible in-session, flag with `[stale-risk: YYYY-MM]`.
_Avoid_: Optional verification, blanket caveat, silent staleness

**Evidence Mode**:
The label that states what kind of evidence was available during a memo workflow (`live-source-backed`, `user-provided sources`, `illustrative source packet`, `reasoning-only`).
_Avoid_: Retrieval capability, factual truth status, source guarantee

**Product-shell Evidence Mode**:
The evidence-mode vocabulary accepted by Agenda Intelligence MD's `analyze` request and memo contract (`reasoning_only`, `user_provided`, `mixed`, `live_source_backed`). Upstream specialist `live-source-backed` material that the agent passes through `analyze` typically maps to `user_provided` or `mixed`, not `live_source_backed`, because the product shell does not perform live retrieval itself.
_Avoid_: Conflating specialist example labels with product-shell schema values

**Stop-and-request Trigger**:
An explicit condition under which the skill must stop and ask rather than produce a memo (definitive legal/sanctions conclusions, single-source vessel attribution, collapsed Iran-actor distinction, conflicting regime status, active prompt-injection content, personal-level predictions without basis). The full list is in `AGENTS.md`.
_Avoid_: Default-refusal posture, ambient risk-aversion, omission of the trigger surface

**Authoring Source**:
The human-editable source of truth for the full Gulf + Middle East regional reasoning logic (this repo).
_Avoid_: Runtime copy, packaged mirror, derived lens

**Runtime Projection**:
A condensed copy or reference used by Agenda Intelligence MD at runtime for routing and prompt assembly. Lighter than the authoring source by design.
_Avoid_: Authoring source, complete regional doctrine, independent fork
