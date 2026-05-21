# Agent-eval: dark-fleet-sanctioned-oil-mixed

- **Question (verbatim):** A mid-size refining company is reviewing its 2026–2027 framework for exposure to crude / fuel oil / condensate cargoes that may have dark-fleet or sanctioned-origin adjacency (Iran-, Russia-, or Venezuela-origin oil; sanctioned vessels in the voyage chain; STS-transfer or origin-obscuring patterns). What is the structural risk shape it should price into counterparty screening, voyage acceptance, attestation discipline, and policy — independent of any single vessel designation event?
- **Decision:** Counterparty acceptance and tiering; voyage and cargo acceptance criteria; attestation discipline; insurance and trade-finance posture; board-level appetite for adjacency exposure over the next 12 months.
- **Model:** Claude Sonnet 4.7 (acting as host model in this session for both conditions)
- **Date:** 2026-05-21
- **Evidence mode:** `mixed` through Agenda Intelligence `analyze`. Upstream specialist material is `live-source-backed` for regulatory framework (`examples/live-source-backed-ofac-iran-shipping-sanctions.md`, E.O. 13846/13902 and OFAC Iran program page retrieved 2026-05-12) plus `user-provided sources` for current-state retrievals (`examples/user-provided-sources-dark-fleet-sanctioned-oil.md`, eleven canonical regulator / IFI / IMO / P&I / FATF mandate-page URLs, accessibility-checked 2026-05-15, no point-in-time content extracted in this session). The product-shell mapping is `mixed` because `analyze` does not accept `live_source_backed`; the upstream source-backed regulatory framework composes with the user-supplied skeleton-packet retrievals into a `mixed` evidence stance at the memo level.
- **Skill under test:** gulf-middle-east-hybrid-intelligence-skill
- **Routing in Condition B:** Local `agenda-intelligence-md` `analyze` request validation routed to GTTA + `gulf-middle-east` (geography "Iran / Gulf / chokepoint" plus sanctions-keyword trigger). No external LLM was invoked locally; the host model completed both conditions using the same model.

## Condition A — Baseline (no MCP)

Prompt: "Answer concisely and decision-usefully in 350-450 words. No structure imposed."

Generated output:

> A refiner reviewing dark-fleet adjacency should treat the question as a portfolio-shape problem, not a list-screening problem. Vessel designations are point events; the structural risk is that the refiner's counterparty chain, voyage chain, and attestation chain produce material exposure even when no single vessel or counterparty is OFAC-listed on the day of the trade.
>
> The right frame is three concentric perimeters. The first is counterparty: who the refiner contracts with, their beneficial ownership, their trading history, their exposure to Iran-state / IRGC-affiliated / Iran-private commercial actor distinctions (Russia and Venezuela have their own actor sets but the Iran distinctions are the most asymmetric). The second is voyage: vessel, operator, flag, prior port calls, AIS history, STS-transfer behavior. The third is cargo: origin documentation, certificate-of-origin chain, attestation under the G7 price cap regime where Russia-origin is in scope.
>
> Mechanism: secondary-sanctions exposure under the Iran shipping regime (E.O. 13846 / 13902) and the price-cap attestation regime do not require the refiner itself to be listed. They require the refiner's chain to include designated actors, designated vessels, or attestation failures that the U.S. or coalition regulators can later assert as material support. Insurance and trade-finance counterparties have their own attestation discipline; a failure at any link can pull the cargo, the payment rail, or the P&I cover.
>
> Practically: tier counterparties (long-standing major IOCs and known traders vs. new entities, opaque-BO traders, traders with sanctioned-origin history); restrict voyage acceptance to vessels with clean AIS continuity and disclosed ownership; require attestation packets that cover origin, route, and price-cap (where applicable); maintain a written adjacency-appetite policy approved at board level. Re-screen at each cargo; do not rely on counterparty-level screening from quarter to quarter.
>
> Watch: OFAC vessel designations and maritime advisories; EU/UK shipping designations; price-cap attestation guidance changes; P&I clubs' exclusion language; war-risk and sanctions-clause practice in cargo policies. Any specific vessel, counterparty, or designation status must be verified against current OFAC SDN list, EU/UK consolidated lists, and the carrier's screening record before acting on this analysis.

Word count: 393.

## Condition B — Agenda Intelligence Product Shell (GTTA + Gulf+ME loaded), `mixed` mapping

The `analyze` request used `evidence_mode: "mixed"` and routed to two modules:

```json
[
  {"module": "global-think-tank-analyst", "role": "reasoning_method"},
  {"module": "gulf-middle-east", "role": "regional_specialist"}
]
```

Generated output excerpt in agenda-memo shape:

```json
{
  "meta": {
    "evidence_mode": "mixed",
    "depth": "decision_pack",
    "geography": "Iran / Gulf / global shipping",
    "modules_used": [
      {"module": "global-think-tank-analyst", "role": "reasoning_method"},
      {"module": "gulf-middle-east", "role": "regional_specialist"}
    ],
    "timestamp": "2026-05-21T10:20:00Z",
    "source_set_summary": "Upstream regulatory framework live-source-backed (E.O. 13846 / 13902 and OFAC Iran program page, retrieved 2026-05-12 in the specialist OFAC Iran shipping sanctions example). Upstream operational source packet user-provided (eleven canonical OFAC / EU / UK / FATF-MENAFATF / IMO / P&I / IMB / UKMTO mandate-page URLs, accessibility-checked 2026-05-15, no point-in-time content extracted in this session). The product-shell evidence_mode `mixed` reflects this composition; `live_source_backed` is not used because part of the source set is user-provided and not independently verified in this run."
  },
  "risk_summary": {
    "short": "Treat dark-fleet / sanctioned-oil adjacency as a three-perimeter portfolio problem (counterparty / voyage / cargo) priced against secondary-sanctions and price-cap attestation mechanisms — not as a vessel-screening compliance problem the refiner can solve by list checks alone.",
    "detailed": "Secondary-sanctions exposure under E.O. 13846 / 13902 and the G7 price-cap attestation regime is triggered by the refiner's chain, not by the refiner's own listing status. The binding risks transmit through counterparty (Iran-state / IRGC-affiliated / Iran-private commercial distinctions, Russia-origin operators, Venezuela-origin operators, opaque BO traders), through voyage (vessel ownership, AIS continuity, STS-transfer patterns, flag, P&I cover), and through cargo (origin documentation, certificate-of-origin chain, price-cap attestation). The refiner's policy posture is a portfolio choice across these three perimeters, not a binary screen at any one of them. Adjacency posture must be reset at each cargo; counterparty-level approvals do not transfer across quarters."
  },
  "decision_frame": {
    "decision": "Set counterparty tiering, voyage acceptance, attestation discipline, and adjacency-appetite policy for 2026-2027.",
    "stakeholders": ["Commercial / trading head", "Sanctions and trade compliance", "Trade finance", "Marine and insurance", "Board risk committee"],
    "constraints": ["Cannot screen against AIS or vessel data without licensed maritime-intelligence providers", "Cannot make legal designations or compliance determinations on its own authority", "Price-cap regime evolves; attestation language changes", "Insurance and bank counterparties have their own thresholds that may be tighter than the refiner's"]
  },
  "analysis": {
    "facts": [
      "OFAC Iran sanctions are administered under E.O. 13846 and E.O. 13902 (regulatory framework, primary sources retrieved upstream 2026-05-12).",
      "OFAC's maritime industry compliance advisory enumerates deceptive shipping practices: AIS manipulation, STS transfers in non-routine locations, flag-hopping, falsified documentation, complex ownership structures (user-provided source packet, mandate-page URLs accessibility-checked 2026-05-15).",
      "Agenda Intelligence `analyze` does not accept `live_source_backed`; this run maps the upstream source-backed regulatory framework plus user-provided operational packet to `mixed`."
    ],
    "assessments": [
      "The binding decision is portfolio-perimeter design across counterparty, voyage, and cargo; not a vessel-screening procurement.",
      "Iran-state / IRGC-affiliated / Iran-private commercial distinctions drive different secondary-sanctions and attestation risk shapes; collapsing them produces both false positives (over-rejection of legitimate Iran-private trade routes that may be permitted under specific regimes) and false negatives (under-screening of IRGC-affiliated counterparties through layered ownership).",
      "Price-cap attestation is the cheapest discipline to install and the highest-leverage; without it, every Russia-origin cargo carries downstream legal-exposure tail risk.",
      "P&I and war-risk cover is the silent gating constraint: refiners that lose cover on a route lose the route, regardless of their own compliance posture."
    ],
    "assumptions": [
      "The refiner can require attestation and documentation from counterparties at cargo level.",
      "Licensed maritime-intelligence providers (e.g., for AIS, vessel ownership) are available to the refiner; this skill does not screen vessels itself.",
      "The refiner has no current counterparty that is OFAC-listed under E.O. 13846 / 13902 or the EU/UK equivalents."
    ],
    "unknowns": [
      "Current OFAC SDN status of any specific counterparty, vessel, operator, or beneficial owner in the refiner's pipeline.",
      "Current EU / UK / Swiss listings for the same actors.",
      "Current price-cap attestation language and General Licenses; the regime evolves and is verified at point of decision.",
      "Whether any cargo in the refiner's pipeline has Iran-, Russia-, or Venezuela-origin adjacency that survives re-papering."
    ]
  },
  "scenarios": [
    {
      "name": "Baseline — adjacency in long tail, no chain-level designations",
      "probability_range": {"low": 0.55, "high": 0.75},
      "drivers": ["Refiner's counterparty set remains majority-IOC / known-trader", "No new OFAC vessel cluster designations affecting refiner's voyage chain", "Price-cap attestation language stable"],
      "implications": ["Tiered counterparty discipline holds; attestation packets sufficient", "No insurance or trade-finance re-pricing"]
    },
    {
      "name": "Single chain-event — a counterparty, vessel, or operator in the refiner's pipeline is designated mid-cycle",
      "probability_range": {"low": 0.15, "high": 0.30},
      "drivers": ["New OFAC vessel designation cluster", "EU / UK adds a shipping-network actor", "An IRGC-affiliated ownership chain is exposed through enforcement"],
      "implications": ["Mid-policy cargo unwind", "P&I cover renegotiation on specific voyages", "Board-level adjacency-appetite review triggered"]
    },
    {
      "name": "Regime shift — price-cap attestation tightens or secondary-sanctions doctrine expands materially",
      "probability_range": {"low": 0.05, "high": 0.20},
      "drivers": ["G7 / Coalition tightens price-cap attestation rules", "US shifts Iran enforcement posture", "EU/UK aligns secondary-sanctions doctrine"],
      "implications": ["Counterparty tiering boundary moves inward", "Capacity for adjacency-exposed cargoes shrinks at the trader and insurer layer", "Bank counterparties pull trade-finance lines"]
    }
  ],
  "options": [
    {
      "option": "Three-perimeter portfolio control (counterparty tiering + voyage acceptance + cargo-level attestation) with hard board-approved adjacency appetite ceiling.",
      "pros": ["Prices adjacency explicitly across perimeters", "Survives chain-events without policy crisis", "Composable with P&I and bank counterparty requirements"],
      "cons": ["Operational overhead at cargo level", "Requires maritime-intelligence provider access for the voyage perimeter"],
      "trade_offs": ["Operational cost vs adjacency tail-risk pricing"]
    },
    {
      "option": "Counterparty-only screen (rely on counterparty due diligence; accept voyage / cargo risk implicitly).",
      "pros": ["Operationally cheap", "Familiar process for the compliance function"],
      "cons": ["Does not control voyage- or cargo-perimeter exposure", "Underprices tail risk where the chain has hidden Iran-state / IRGC-affiliated / Iran-private commercial substitution"],
      "trade_offs": ["Cost simplicity vs blind spots on the binding mechanism"]
    },
    {
      "option": "Withdraw from any adjacency-exposed route (Russia-origin under price cap, Iran-origin under secondary sanctions, Venezuela-origin under sectoral sanctions).",
      "pros": ["Eliminates the chain-event exposure tail", "Removes attestation operational burden"],
      "cons": ["Loses market access in segments where compliant trade is possible", "Hard to re-enter at scale once franchise is broken"],
      "trade_offs": ["Short-term tail elimination vs long-term franchise"]
    }
  ],
  "recommended_actions": [
    {"action": "Adopt three-perimeter portfolio control framework (counterparty / voyage / cargo) with documented adjacency-appetite ceiling approved at board level.", "priority": "high", "trigger": "Now", "time_horizon": "60 days"},
    {"action": "Mandate price-cap attestation language on all Russia-origin-eligible cargoes; align attestation packet with G7 / Coalition guidance.", "priority": "high", "trigger": "Now", "time_horizon": "30 days"},
    {"action": "Embed Iran-state / IRGC-affiliated / Iran-private commercial actor distinction into counterparty due-diligence templates; route ambiguous cases to compliance.", "priority": "high", "trigger": "Now", "time_horizon": "45 days"},
    {"action": "Contract or expand maritime-intelligence provider access for vessel ownership, flag history, AIS continuity, STS-transfer pattern detection.", "priority": "medium", "trigger": "Three-perimeter framework adoption", "time_horizon": "90 days"},
    {"action": "Sync adjacency policy with P&I, war-risk, and bank trade-finance counterparties; reconcile thresholds where the refiner is the weakest link.", "priority": "medium", "trigger": "Three-perimeter framework adoption", "time_horizon": "90 days"}
  ],
  "failure_modes": [
    {"scenario": "Refiner conflates Iran-state, IRGC-affiliated, and Iran-private commercial actors; mistakenly accepts an IRGC-affiliated counterparty layered behind a private trader.", "likelihood": "medium", "impact": "high", "mitigation": "Encode the actor distinction in the counterparty template; escalate ambiguous BO chains to compliance"},
    {"scenario": "Mid-policy chain-event designation lands on a vessel or operator in flight; cargo is in voyage when designation hits.", "likelihood": "medium", "impact": "high", "mitigation": "Designation-event clause in contracts; pre-document the unwind path; voyage-level diversification"},
    {"scenario": "Price-cap attestation packet is treated as a one-time form rather than a maintained record; coalition guidance evolves and the refiner falls behind.", "likelihood": "medium", "impact": "medium", "mitigation": "Quarterly attestation language review; named owner inside compliance"},
    {"scenario": "P&I or war-risk insurer tightens exclusions; refiner's voyage acceptance criteria do not adjust in time and cover gaps open.", "likelihood": "low", "impact": "high", "mitigation": "Insurer policy review on each material renewal; reconcile internal voyage criteria"}
  ],
  "watch_next": [
    {"indicator": "OFAC vessel designations and maritime industry advisories", "trigger": "Any new vessel-cluster designation or revised maritime advisory", "source_type": "regulator_announcement"},
    {"indicator": "EU consolidated and UK OFSI shipping-network designations", "trigger": "Any new shipping-network actor added", "source_type": "regulator_announcement"},
    {"indicator": "G7 / Coalition price-cap attestation language", "trigger": "Any revision to attestation language or General License changes", "source_type": "legal_act"},
    {"indicator": "P&I clubs' exclusion and sanctions-clause practice", "trigger": "Any revision to standard clauses or club-level guidance", "source_type": "industry_self_regulation"},
    {"indicator": "FATF / MENAFATF guidance on shipping and trade-finance typologies", "trigger": "Any new typology paper or revised mutual evaluation finding", "source_type": "international_standard_setter"}
  ],
  "audit": {
    "validation_score": 1.0,
    "machine_verified": true,
    "validation_details": [
      {"check": "schema_valid", "passed": true},
      {"check": "fact_assessment_separation", "passed": true},
      {"check": "unknowns_acknowledged", "passed": true},
      {"check": "modules_used_match_routing", "passed": true},
      {"check": "watch_next_present", "passed": true},
      {"check": "evidence_mode_within_contract", "passed": true},
      {"check": "evidence_mode_not_live_source_backed", "passed": true}
    ],
    "provenance": [
      {"claim": "OFAC Iran sanctions are administered under E.O. 13846 and E.O. 13902.", "basis": "fact"},
      {"claim": "Binding refiner risk transmits through the three perimeters (counterparty / voyage / cargo) under secondary-sanctions and price-cap mechanisms.", "basis": "assessment"},
      {"claim": "Iran-state / IRGC-affiliated / Iran-private commercial distinctions drive different secondary-sanctions risk shapes.", "basis": "assessment"},
      {"claim": "No current counterparty in the refiner's pipeline is OFAC-listed.", "basis": "assumption"},
      {"claim": "Current SDN, EU, UK, Swiss list status for any specific counterparty.", "basis": "unknown"}
    ]
  }
}
```

Approximate equivalent prose length: 1250 words.

## Scoring

| Criterion | A | B |
|---|---:|---:|
| Fact / assessment / assumption / unknown separation | 0 | 1 |
| Provenance discipline | 0.5 | 1 |
| Decision frame present | 0.5 | 1 |
| Scenarios with probability ranges | 0 | 1 |
| Options with explicit trade-offs | 0.5 | 1 |
| Failure modes with likelihood and impact | 0 | 1 |
| Watch-next indicators with triggers | 0.5 | 1 |
| Evidence-mode mapping (`mixed`, not `live_source_backed`) | 0 | 1 |
| Honest scope | 1 | 1 |
| **Total** | **3 / 9** | **9 / 9** |

**Delta:** +6.

## Observations

The baseline output is competent: it identifies the three-perimeter framing, names the right regulatory mechanisms (E.O. 13846 / 13902, price-cap attestation), preserves the Iran actor distinctions, and ends with a verification disclaimer. Where it falls short is structural — there is no fact / assessment / assumption / unknown separation, no machine-readable provenance, no probability-ranged scenarios, and no evidence-mode tag at the run level.

The MCP-attached condition adds the integration-critical behavior this case was designed to test: source-backed specialist material from the upstream OFAC Iran shipping sanctions example (regulatory framework, `live-source-backed`) is composed with user-provided skeleton-packet operational URLs (`user-provided sources`) and mapped through `analyze` as **`mixed`** — not `live_source_backed`. This proves the specialist evidence vocabulary does not break the product-shell schema. The `source_set_summary` in `meta` makes the composition auditable: a reviewer can trace upstream evidence modes back to the originating example files and dates.

Beyond the mapping itself, B adds explicit unknowns ("current SDN / EU / UK / Swiss status"), failure-mode-level discipline (likelihood + impact + mitigation per scenario), and watch-next triggers with source-type tags that an agent workflow can act on.

The structural delta is the largest of the three Gulf+ME cases so far, primarily because the bare model under-uses provenance and evidence-mode discipline on a question that is fundamentally about evidence chain integrity. This is the case the MCP shell is designed for.

## Limitations

- One model, one prompt run. Not statistically significant.
- Self-scored by the author / host model. Not external review.
- Structural eval only. It does not verify the current OFAC SDN, EU, UK, Swiss, or price-cap attestation facts.
- The local `analyze` request was validated for routing and evidence-mode mapping; no external LLM was invoked in Condition B.
- The upstream `user-provided sources` packet is mandate-page-URL accessibility-checked only; no point-in-time content was extracted in this session. Operational use requires the user to retrieve current content from those mandate pages.
- This is not a factual benchmark, model-quality comparison, aggregate claim, compliance conclusion, sanctions screening, vessel screening, or practitioner validation.
- The Gulf+ME regional lens specifically requires preserving Iran-state / IRGC-affiliated / Iran-private commercial distinctions; this eval would underestimate the regional lens's value on cases where the bare model collapses these.
