# Agent-eval: gcc-correspondent-tiering

- **Question (verbatim):** A Western respondent bank is reviewing its GCC correspondent banking relationships (Saudi, UAE, Qatar, Kuwait, Bahrain, Oman) over the next 12–18 months. The UAE was grey-listed by FATF in February 2022 and removed in February 2024; Saudi banks operate under SAMA and were not grey-listed. How should the bank tier and manage these relationships — what is the structural risk shape that should drive maintain / enhance-EDD / selectively-de-risk decisions, independent of any single enforcement event?
- **Decision:** Whether to maintain, enhance due diligence on, or selectively de-risk GCC correspondent banking relationships, and on what tiering criteria, over the next 12–18 months.
- **Model:** Claude Sonnet 4.7 (acting as host model in this session for both conditions)
- **Date:** 2026-05-21
- **Evidence mode:** reasoning_only (both conditions). The Condition B run does not pass source-backed material into `analyze`; the `mixed` mapping case for B2.3 is exercised separately in `2026-05-21-dark-fleet-sanctioned-oil-mixed.md`.
- **Skill under test:** gulf-middle-east-hybrid-intelligence-skill
- **Routing in Condition B:** GTTA + gulf-middle-east (geography "GCC" plus correspondent-banking / AML keyword set).

## Condition A — Baseline (no MCP)

Prompt: "Answer concisely and decision-usefully in 350-450 words. No structure imposed."

Generated output:

> A Western respondent bank reviewing GCC correspondents should not treat "GCC" as a category. The risk shape varies materially by jurisdiction and within each jurisdiction by counterparty profile. Saudi banks operate under SAMA in a system that did not go through FATF grey-listing; the UAE was grey-listed February 2022 and removed February 2024 after remediation; Qatar, Kuwait, Bahrain, and Oman each have their own regulator and risk profile.
>
> The binding question is not "GCC exposure" but the tiering criteria: which specific correspondent banks, with what AML/CFT controls, with what beneficial-owner transparency on the underlying clients, in which free-zone or onshore context. UAE free zones in particular are heterogeneous; some have tightened BO transparency post-FATF remediation, others remain harder to penetrate. Saudi correspondents typically carry counterparty-level risk that is more tractable than the UAE's free-zone-adjacent risk.
>
> Mechanism: the Western bank's exposure transmits through (a) sanctions adjacency — Iran sanctions, Russia sanctions, and secondary-sanctions exposure routed through GCC payment rails; (b) AML — typologies including trade-based money laundering, BO opacity in free zones, professional service intermediaries; (c) regulatory — home-supervisor expectations on third-country correspondent relationships, especially for jurisdictions with FATF history; (d) operational — settlement risk, KYC refresh cadence, suspicious transaction reporting.
>
> Practical tiering: Tier 1 — large, well-capitalized GCC banks with strong AML controls and transparent ownership, maintained with standard correspondent due diligence; Tier 2 — mid-size or specialized banks in jurisdictions with remediation history (UAE post-FATF), maintained with enhanced due diligence, more frequent KYC refresh, deeper underlying-client scrutiny on flagged corridors; Tier 3 — banks with weak controls, high free-zone exposure, or known concentration in higher-risk client segments, considered for selective de-risking on specific corridors rather than blanket exit.
>
> Watch: FATF and MENAFATF mutual evaluation cycle outputs; CBUAE and SAMA AML circulars; OFAC and EU enforcement actions naming GCC correspondents; BIS Consolidated Banking Statistics for cross-border exposure trends; home-supervisor (Fed, ECB, FCA) guidance on third-country correspondents. Specific list status for any GCC counterparty must be verified against current OFAC, EU, UK, and FATF country status sources before acting.

Word count: 386.

## Condition B — Agenda Intelligence MCP attached (GTTA + Gulf+ME loaded)

The `analyze` system prompt loaded GTTA reasoning method and the Gulf + Middle East regional reference (which carries the GCC jurisdictional differentiation, the UAE FATF grey-listing timeline, the SAMA / CBUAE regulator distinction, and the Iran-sanctions-adjacency-through-GCC-rails frame). Output (excerpt; agenda-memo schema):

```json
{
  "meta": {
    "evidence_mode": "reasoning_only",
    "depth": "decision_pack",
    "geography": "GCC (Saudi Arabia, UAE, Qatar, Kuwait, Bahrain, Oman)",
    "modules_used": [
      {"module": "global-think-tank-analyst", "role": "reasoning_method"},
      {"module": "gulf-middle-east", "role": "regional_specialist"}
    ],
    "timestamp": "2026-05-21T11:05:00Z"
  },
  "risk_summary": {
    "short": "Tier GCC correspondents by jurisdiction-times-counterparty risk, not by 'GCC' as a category. The binding drivers are FATF remediation history (UAE), regulator strength (SAMA vs. CBUAE vs. smaller-state regulators), free-zone BO transparency, and the sanctions-adjacency footprint of underlying clients — not the headline jurisdiction.",
    "detailed": "Western respondent exposure to GCC correspondents transmits through four mechanisms: sanctions adjacency (Iran / Russia / secondary-sanctions routed through GCC payment rails), AML typologies (trade-based money laundering, free-zone BO opacity, professional intermediaries), regulatory (home-supervisor expectations on third-country correspondents post-FATF cycles), and operational (settlement, KYC refresh, STR cadence). The right portfolio decision is tiered maintain / enhanced-EDD / selective-de-risk along these mechanisms, applied per counterparty, not blanket de-risking or blanket acceptance."
  },
  "decision_frame": {
    "decision": "Set GCC correspondent tiering (maintain / enhance-EDD / selectively de-risk) and supporting due-diligence cadence for 12-18 months.",
    "stakeholders": ["AML / financial crime head", "Correspondent banking head", "Sanctions compliance", "Senior management / risk committee", "Home-country supervisory relationship lead"],
    "constraints": ["Cannot pre-empt home-supervisor guidance", "De-risking has reputational and access-to-payment-system costs to client base", "FATF country status changes between cycles", "Free-zone BO data quality is uneven across jurisdictions"]
  },
  "analysis": {
    "facts": [
      "Saudi Arabia operates correspondent banking through SAMA-regulated institutions; was not FATF grey-listed in the most recent cycle.",
      "The UAE was FATF grey-listed in February 2022 and removed in February 2024 following remediation.",
      "Iran sanctions adjacency and Russia secondary-sanctions exposure can transmit through GCC payment rails depending on the underlying-client mix."
    ],
    "assessments": [
      "Jurisdiction-times-counterparty is the binding tiering variable; jurisdiction alone over-aggregates and counterparty alone under-prices regulator-level effects.",
      "UAE post-FATF carries a remediation-trajectory risk shape distinct from a non-grey-listed jurisdiction even after removal; home supervisors typically apply lagged scrutiny.",
      "Free-zone BO opacity is the highest-leverage AML driver inside the UAE tier; counterparties with concentrated free-zone client exposure carry materially different risk than onshore-focused counterparties.",
      "Selective de-risking on specific corridors is usually preferable to blanket-exit; blanket exit imposes access-to-payments costs on legitimate client populations and signals weak control rather than strong control."
    ],
    "assumptions": [
      "Home supervisor expectations remain in line with current FATF cycle outputs; no major shift in third-country correspondent guidance in the 18-month horizon.",
      "GCC regulators (SAMA, CBUAE, QCB, CBK, CBB, CBO) maintain current AML/CFT supervisory posture.",
      "No major Iran or Russia secondary-sanctions doctrine shift that re-prices GCC-rail exposure."
    ],
    "unknowns": [
      "Counterparty-level AML and BO control quality for any specific GCC correspondent in the bank's pipeline.",
      "Current FATF / MENAFATF mutual evaluation findings beyond the last published cycle.",
      "Current OFAC / EU / UK enforcement actions naming GCC correspondents.",
      "Current home-supervisor (Fed / ECB / FCA / SNB) guidance on third-country correspondents."
    ]
  },
  "scenarios": [
    {
      "name": "Baseline — stable supervisory posture, no major enforcement event",
      "probability_range": {"low": 0.50, "high": 0.70},
      "drivers": ["FATF cycle stable for GCC jurisdictions", "Home supervisor guidance stable", "No major OFAC / EU enforcement action naming GCC correspondents"],
      "implications": ["Tier 1 maintained with standard CDD; Tier 2 maintained with EDD; Tier 3 selectively reviewed", "No portfolio-level repricing"]
    },
    {
      "name": "Targeted enforcement event — a GCC correspondent or its underlying clients are named in an OFAC / EU action",
      "probability_range": {"low": 0.15, "high": 0.30},
      "drivers": ["OFAC or EU enforcement naming a GCC correspondent or its underlying clients", "Home supervisor issues sector-specific guidance", "A free-zone-adjacent typology surfaces in a mutual evaluation"],
      "implications": ["Mid-cycle tier review of named counterparty and similar-profile peers", "EDD intensifies on overlapping corridors", "Possible selective de-risking on the affected corridor"]
    },
    {
      "name": "Regime shift — FATF re-evaluation downgrades a GCC jurisdiction or home supervisor tightens third-country guidance",
      "probability_range": {"low": 0.05, "high": 0.20},
      "drivers": ["FATF mutual evaluation downgrade for a GCC jurisdiction", "Home supervisor (Fed / ECB / FCA) issues stricter third-country correspondent guidance", "Major secondary-sanctions doctrine shift affecting GCC rails"],
      "implications": ["Tier boundaries move inward (more counterparties enter EDD or de-risk)", "Portfolio-level repricing of GCC exposure", "Senior-management / board review triggered"]
    }
  ],
  "options": [
    {
      "option": "Jurisdiction-times-counterparty tiering (Tier 1 maintain / Tier 2 enhance-EDD / Tier 3 selectively de-risk by corridor) with documented criteria approved at risk-committee level.",
      "pros": ["Prices both regulator strength and counterparty quality", "Preserves access for legitimate underlying clients", "Composable with home-supervisor expectations"],
      "cons": ["Operational overhead to maintain tier criteria and refresh cadence", "Requires counterparty-level BO and AML control visibility"],
      "trade_offs": ["Operational cost vs. precision on the binding driver"]
    },
    {
      "option": "Jurisdiction-only tiering (treat UAE as one tier, Saudi as another, smaller GCC states as another).",
      "pros": ["Operationally simple", "Easy to communicate to home supervisor"],
      "cons": ["Over-aggregates within jurisdiction; misprices high-quality counterparties in higher-risk jurisdictions and vice versa", "Vulnerable to enforcement events that target counterparty-level patterns"],
      "trade_offs": ["Simplicity vs. accuracy on the binding mechanism"]
    },
    {
      "option": "Blanket de-risking of higher-risk GCC jurisdictions (e.g., exit UAE non-Tier-1 correspondents).",
      "pros": ["Eliminates the tail of free-zone-adjacent exposure", "Reduces home-supervisor narrative risk"],
      "cons": ["Cuts access for legitimate underlying clients", "Signals weak control rather than strong control", "Hard to re-enter; franchise damage"],
      "trade_offs": ["Tail-risk elimination vs. legitimate-trade access and franchise"]
    }
  ],
  "recommended_actions": [
    {"action": "Adopt jurisdiction-times-counterparty tiering matrix with documented criteria and risk-committee sign-off.", "priority": "high", "trigger": "Now", "time_horizon": "60 days"},
    {"action": "Set differentiated KYC refresh cadence by tier (standard / EDD / corridor-conditional).", "priority": "high", "trigger": "Matrix adoption", "time_horizon": "90 days"},
    {"action": "Sync tier criteria with home-supervisor expectations through proactive supervisory engagement.", "priority": "medium", "trigger": "Matrix adoption", "time_horizon": "120 days"},
    {"action": "Add UAE free-zone BO transparency as a specific Tier 2 sub-criterion; identify counterparties with concentrated free-zone client exposure.", "priority": "medium", "trigger": "Matrix adoption", "time_horizon": "90 days"},
    {"action": "Build Iran-state / IRGC-affiliated / Iran-private commercial distinction into the underlying-client AML typology bank for GCC rails.", "priority": "medium", "trigger": "Matrix adoption", "time_horizon": "120 days"}
  ],
  "failure_modes": [
    {"scenario": "Bank treats 'GCC' as a category; misprices high-quality Saudi counterparty as elevated-risk and low-quality UAE free-zone-adjacent counterparty as standard.", "likelihood": "medium", "impact": "medium", "mitigation": "Enforce jurisdiction-times-counterparty matrix; no jurisdiction-only tier assignments"},
    {"scenario": "Enforcement event lands on a GCC correspondent; bank's tier matrix is not refreshed and similar-profile peers are not flagged.", "likelihood": "medium", "impact": "high", "mitigation": "Event-driven tier-refresh trigger; named owner inside compliance"},
    {"scenario": "Bank conflates Iran-state, IRGC-affiliated, and Iran-private commercial actors in underlying-client AML typology; mispricing sanctions adjacency.", "likelihood": "medium", "impact": "medium", "mitigation": "Encode actor distinction in AML typology bank; escalate ambiguous BO chains"},
    {"scenario": "Blanket de-risking executed under reputational pressure; legitimate trade is cut and home supervisor reads this as weak control.", "likelihood": "low", "impact": "high", "mitigation": "Default to selective corridor de-risking; document the legitimate-access case for any retained relationship"}
  ],
  "watch_next": [
    {"indicator": "FATF / MENAFATF mutual evaluation cycle outputs", "trigger": "Any new mutual evaluation finding or follow-up report for a GCC jurisdiction", "source_type": "international_standard_setter"},
    {"indicator": "CBUAE / SAMA / QCB / CBK / CBB / CBO AML circulars and supervisory actions", "trigger": "Any new AML circular or enforcement action", "source_type": "regulator_announcement"},
    {"indicator": "OFAC / EU / UK enforcement actions naming GCC correspondents or underlying clients", "trigger": "Any enforcement action with a GCC nexus", "source_type": "regulator_announcement"},
    {"indicator": "BIS Consolidated Banking Statistics — Western bank cross-border exposure to GCC counterparties", "trigger": "Material shift in exposure trend (sustained inflow or outflow over consecutive periods)", "source_type": "open_data"},
    {"indicator": "Home-supervisor (Fed / ECB / FCA / SNB) guidance on third-country correspondent relationships", "trigger": "Any new guidance or thematic review with GCC scope", "source_type": "regulator_announcement"}
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
      {"check": "evidence_mode_within_contract", "passed": true}
    ],
    "provenance": [
      {"claim": "Saudi Arabia was not FATF grey-listed in the most recent cycle; operates under SAMA.", "basis": "fact"},
      {"claim": "UAE was FATF grey-listed February 2022 and removed February 2024.", "basis": "fact"},
      {"claim": "Jurisdiction-times-counterparty is the binding tiering variable.", "basis": "assessment"},
      {"claim": "Free-zone BO opacity is the highest-leverage AML driver inside the UAE tier.", "basis": "assessment"},
      {"claim": "Counterparty-level AML and BO control quality for any specific GCC correspondent.", "basis": "unknown"}
    ]
  }
}
```

Approximate equivalent prose length: 1300 words.

## Scoring

| Criterion | A | B |
|---|---:|---:|
| Fact / assessment / assumption / unknown separation | 0 | 1 |
| Provenance discipline | 0 | 1 |
| Decision frame present | 0.5 | 1 |
| Scenarios with probability ranges | 0 | 1 |
| Options with explicit trade-offs | 0.5 | 1 |
| Failure modes with likelihood and impact | 0 | 1 |
| Watch-next indicators with triggers | 0.5 | 1 |
| Honest scope | 1 | 1 |
| **Total** | **2.5 / 8** | **8 / 8** |

**Delta:** +5.5.

## Observations

The baseline output is solid: it correctly rejects "GCC" as a category, names the FATF UAE timeline, identifies SAMA / CBUAE as distinct regulators, and proposes a tiered approach. Where it falls short is structural — no fact / assessment / assumption / unknown separation, no machine-readable provenance, no probability-ranged scenarios, and no failure-mode discipline.

The MCP-attached output adds value in three places specific to correspondent-banking decisions: (1) it makes jurisdiction-times-counterparty explicit as the binding tiering variable rather than letting it remain implicit; (2) it surfaces free-zone BO transparency as a specific UAE sub-criterion rather than a general AML concern; (3) it embeds the Iran-state / IRGC-affiliated / Iran-private commercial actor distinction into the underlying-client AML typology, which a bare-model output typically does not reach for in a banking-tiering question framed away from Iran.

This case suggests the regional lens's value in correspondent banking is mostly precision: pulling out the right sub-criteria (free zones, actor distinctions, FATF remediation trajectory) that a bare model treats generically. The delta is smaller than the dark-fleet case because the bare model has reasonable correspondent-banking priors; the delta is larger than the Hormuz case because correspondent-banking tiering rewards machine-readable provenance more than chokepoint-risk underwriting does.

## Limitations

- One model, one prompt run. Not statistically significant.
- Self-scored by the author / host model. Not external review.
- Structural eval only. It does not verify the current FATF, OFAC, EU, UK, or home-supervisor facts. The FATF UAE grey-listing dates (Feb 2022 entry / Feb 2024 removal) are public-record facts but should be re-verified against the FATF site at point of operational use.
- The agent-eval is structural, not factual. Specific tiering decisions for any GCC correspondent require entity-level AML / BO due diligence and home-supervisor engagement.
- This is not a factual benchmark, model-quality comparison, aggregate claim, compliance conclusion, AML determination, or practitioner validation.
- The Gulf+ME regional lens specifically requires preserving Iran-state / IRGC-affiliated / Iran-private commercial distinctions; this eval would underestimate the regional lens's value on cases where the underlying-client mix has direct Iran-actor adjacency.
