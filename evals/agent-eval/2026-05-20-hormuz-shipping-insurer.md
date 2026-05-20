# Agent-eval: hormuz-shipping-insurer

- **Question (verbatim):** How should a shipping insurer with significant Hormuz-transiting tanker book frame and price war-risk exposure during a period of elevated US-Iran tension and sporadic incident activity?
- **Decision:** War-risk premium structure, exposure aggregation limits, and underwriting discipline over the next 90 days.
- **Model:** Claude Sonnet 4.7 (acting as host model in this session)
- **Date:** 2026-05-20
- **Evidence mode:** reasoning_only (both conditions)
- **Skill under test:** gulf-middle-east-hybrid-intelligence-skill
- **Routing in Condition B:** GTTA + gulf-middle-east (geography "Hormuz" matches Gulf+ME term set; no sanctions keyword in the question)

## Condition A — Baseline (no MCP)

Prompt: "Answer concisely and decision-usefully in 350-450 words. No structure imposed."

Generated output:

> A shipping insurer with a Hormuz tanker book during elevated US-Iran tension is dealing with a fat-tailed exposure: most quarters look like incident-light baselines, and a small share of quarters carry either a named seizure or a sustained traffic-degrading event that materially changes loss expectations. The wrong move is to anchor war-risk premium on either the recent median quarter (too cheap) or the recent worst quarter (overpriced for the modal case).
>
> The framing that holds up is to treat Hormuz as a risk corridor with dispersion explicitly priced in. Premium structure should reflect the gap between the baseline (sporadic incidents, no closure) and the upside (named seizure event, sustained transit degradation, or formal closure). Exposure aggregation limits should constrain how much of the book can be exposed to a single chokepoint event — if Hormuz transit is correlated for your entire tanker book on a given day, you have clash risk.
>
> Underwriting discipline over 90 days should: (1) refresh war-risk surveys with current IRGC posture, AIS-derived traffic stress signals, and any named-vessel incident pattern; (2) tighten exposure aggregation limits per chokepoint, not per geographic radius; (3) require attestation around vessel ownership and operator due diligence (sanctions adjacency); (4) build a tabletop on a sustained-closure scenario with explicit loss assumptions.
>
> The actor distinctions matter: Iran-state actions (formal closure, naval intercepts), IRGC-affiliated activity (seizures of named vessels, asymmetric attacks), and Iran-private commercial risk (sanctions-adjacent counterparties) drive different loss patterns. Collapsing them is the most common analytical error.
>
> What to watch: IRGC posture signals, US 5th Fleet/CMF advisories, UKMTO/IMB incident reports, AIS chokepoint traffic anomalies, named-vessel detentions or interventions, and US-Iran negotiation track status.

Word count: 333.

## Condition B — Agenda Intelligence MCP attached (GTTA + Gulf+ME loaded)

The `analyze` system prompt loaded two modules: GTTA reasoning method and the Gulf + Middle East regional reference (which carries the Iran-state / IRGC-affiliated / Iran-private commercial actor distinction and the Hormuz / Bab-el-Mandeb chokepoint frame). Output (excerpt; agenda-memo schema):

```json
{
  "meta": {
    "evidence_mode": "reasoning_only",
    "depth": "decision_pack",
    "geography": "Hormuz",
    "modules_used": [
      {"module": "global-think-tank-analyst", "role": "reasoning_method"},
      {"module": "gulf-middle-east", "role": "regional_specialist"}
    ],
    "timestamp": "2026-05-20T15:55:00Z"
  },
  "risk_summary": {
    "short": "Price Hormuz as a risk corridor, not a point estimate; the binding underwriting question is dispersion between baseline (sporadic incidents) and upside (named seizure or sustained transit degradation), and exposure aggregation per chokepoint is the operational lever — not premium level alone.",
    "detailed": "Most 90-day windows historically look like incident-light baselines; a minority carry named-seizure or sustained transit-degrading events that materially change loss expectations. Anchoring premium on the median-recent quarter underprices the upside; anchoring on the worst-recent overprices the modal case. The correct posture is explicit corridor pricing plus per-chokepoint exposure-aggregation discipline. The Iran-state / IRGC-affiliated / Iran-private commercial actor distinctions drive different loss patterns and must not be collapsed: a formal Iran-state closure is a different risk shape than IRGC-affiliated vessel seizures, which is different again from Iran-private commercial sanctions adjacency."
  },
  "decision_frame": {
    "decision": "War-risk premium structure, exposure aggregation limits, and underwriting discipline over the next 90 days.",
    "stakeholders": ["Head of underwriting (marine war)", "Head of risk (aggregation)", "Reinsurance lead", "Sanctions / compliance"],
    "constraints": ["Existing book cannot be repriced mid-policy", "Reinsurer appetite for clash cover", "Limited intraday AIS / advisory infrastructure"]
  },
  "analysis": {
    "facts": [
      "Hormuz carries a material share of seaborne crude and LNG flows globally.",
      "UKMTO, IMB, US 5th Fleet / CMF, and IRGC public statements are the primary chokepoint advisory inputs.",
      "War-risk premium markets typically widen rapidly on named-seizure or attack events."
    ],
    "assessments": [
      "The binding underwriting risk in elevated-tension periods is dispersion (fat tail), not the central tendency.",
      "Per-chokepoint aggregation is more decision-useful than per-geographic-radius aggregation when one event correlates the book.",
      "Iran-state, IRGC-affiliated, and Iran-private commercial actor activity drive distinct loss patterns; collapsing them is a common analytical error that misprices risk.",
      "Sustained closure (multi-week traffic degradation) is a tail-but-not-zero scenario; underwriters typically underweight it because the modal quarter is benign."
    ],
    "assumptions": [
      "No structural change in IRGC posture in the 90-day horizon (i.e., not a formal closure declaration).",
      "Reinsurance market remains open; clash cover is available at non-prohibitive cost.",
      "AIS traffic data and advisories are accessible at sufficient timeliness for underwriting decisions."
    ],
    "unknowns": [
      "Exact IRGC operational tempo in the next 90 days.",
      "US-Iran negotiation file status as of the next major policy window.",
      "Whether named-vessel detentions (if any) will cluster on a specific flag, operator, or cargo type — driving differential pricing."
    ]
  },
  "scenarios": [
    {
      "name": "Baseline — sporadic incidents, no closure",
      "probability_range": {"low": 0.55, "high": 0.75},
      "drivers": ["Status quo IRGC posture", "No US-Iran escalation event", "Named-vessel incidents at recent-quarterly cadence"],
      "implications": ["War-risk premium remains in current corridor band", "Aggregation limits hold; clash cover not triggered"]
    },
    {
      "name": "Named seizure or attack event",
      "probability_range": {"low": 0.15, "high": 0.35},
      "drivers": ["IRGC-affiliated seizure of a named tanker", "Or a Houthi-pattern attack on a Hormuz-adjacent vessel"],
      "implications": ["War-risk premium step-jumps; new submissions priced at the higher band", "Aggregation limits may bind on existing book"]
    },
    {
      "name": "Sustained closure / transit degradation",
      "probability_range": {"low": 0.05, "high": 0.15},
      "drivers": ["Formal Iran-state closure declaration", "Or multi-vessel incident pattern causing days-long traffic stoppage", "Or material US-Iran military exchange"],
      "implications": ["Catastrophic clash risk realizes on existing book", "Reinsurance market reprices or withdraws", "Premium structure no longer meaningful; capacity becomes the constraint"]
    }
  ],
  "options": [
    {
      "option": "Two-tier premium structure (baseline corridor + named-event surcharge) with hard per-chokepoint aggregation limits.",
      "pros": ["Prices dispersion explicitly", "Aggregation discipline constrains clash exposure", "Communicable to reinsurers"],
      "cons": ["Requires real-time advisory feed for surcharge trigger", "Reinsurer alignment needed on chokepoint definition"],
      "trade_offs": ["Operational complexity vs pricing accuracy"]
    },
    {
      "option": "Single corridor premium with strict per-vessel underwriting attestations (ownership, operator, flag, sanctions adjacency).",
      "pros": ["Simpler to administer", "Pushes sanctions-adjacency risk to attestations"],
      "cons": ["Does not price dispersion; underprices fat tail", "Attestation reliability is variable"],
      "trade_offs": ["Simplicity vs accuracy on the tail"]
    },
    {
      "option": "Withdraw or sharply reprice Hormuz capacity for new business; run off existing book.",
      "pros": ["Reduces gross exposure during high-uncertainty window", "Frees capital"],
      "cons": ["Loses market position; hard to re-enter at scale", "Existing book still carries the tail"],
      "trade_offs": ["Short-term risk reduction vs long-term franchise"]
    }
  ],
  "recommended_actions": [
    {"action": "Implement per-chokepoint aggregation limits (Hormuz, Bab-el-Mandeb, Red Sea as distinct nodes).", "priority": "high", "trigger": "Now", "time_horizon": "30 days"},
    {"action": "Negotiate clash cover reinstatement or top-up with reinsurers at current pricing.", "priority": "high", "trigger": "Aggregation limits set", "time_horizon": "45 days"},
    {"action": "Stand up daily UKMTO / IMB / 5th Fleet advisory ingestion into underwriting workflow.", "priority": "high", "trigger": "Now", "time_horizon": "30 days"},
    {"action": "Run a tabletop on the sustained-closure scenario with reinsurance and compliance present.", "priority": "medium", "trigger": "Aggregation discipline in place", "time_horizon": "60 days"},
    {"action": "Tighten vessel-level attestations (ownership, operator, flag, sanctions adjacency) on new submissions.", "priority": "medium", "trigger": "Now", "time_horizon": "45 days"}
  ],
  "failure_modes": [
    {"scenario": "Named-seizure event hits during current quarter; submissions in flight are priced on baseline corridor.", "likelihood": "medium", "impact": "high", "mitigation": "Pre-document the surcharge trigger mechanism; condition open submissions on event-clause"},
    {"scenario": "Reinsurer withdraws clash cover or reprices materially after an event.", "likelihood": "medium", "impact": "high", "mitigation": "Diversify clash providers; document existing-cover language carefully"},
    {"scenario": "Underwriter collapses Iran-state / IRGC-affiliated / Iran-private commercial distinctions, mispricing a counterparty.", "likelihood": "medium", "impact": "medium", "mitigation": "Embed the actor distinction in underwriting checklist; route ambiguous cases to compliance"},
    {"scenario": "AIS or advisory ingestion fails during a critical event window.", "likelihood": "low", "impact": "high", "mitigation": "Redundant feeds; documented manual-fallback procedure"}
  ],
  "watch_next": [
    {"indicator": "IRGC posture and statement cadence", "trigger": "Any new formal IRGC statement on Hormuz transit or named operator", "source_type": "state_actor_communication"},
    {"indicator": "UKMTO / IMB chokepoint incident reports", "trigger": "Any named-vessel detention or attack in or near Hormuz", "source_type": "maritime_advisory"},
    {"indicator": "US 5th Fleet / CMF advisories", "trigger": "Posture change or named-incident report", "source_type": "state_actor_communication"},
    {"indicator": "AIS-derived chokepoint traffic anomalies", "trigger": "Material deviation from baseline transit pattern", "source_type": "open_data"},
    {"indicator": "US-Iran negotiation track public signals", "trigger": "Material shift in posture (sanctions snapback, JCPOA-track event)", "source_type": "state_actor_communication"}
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
      {"claim": "Hormuz carries a material share of seaborne crude and LNG flows.", "basis": "fact"},
      {"claim": "Binding underwriting risk in elevated-tension periods is dispersion, not central tendency.", "basis": "assessment"},
      {"claim": "Iran-state, IRGC-affiliated, and Iran-private commercial activity drive distinct loss patterns.", "basis": "assessment"},
      {"claim": "No structural change in IRGC posture in the 90-day horizon.", "basis": "assumption"}
    ]
  }
}
```

Approximate equivalent prose length: 1100 words.

## Scoring

| Criterion | A | B |
|---|---|---|
| Fact / assessment / assumption / unknown separation | 0 | 1 |
| Provenance discipline | 0 | 1 |
| Decision frame present | 0.5 | 1 |
| Scenarios with probability ranges | 0 | 1 |
| Options with explicit trade-offs | 0.5 | 1 |
| Failure modes with likelihood and impact | 0 | 1 |
| Watch-next indicators with triggers | 0 | 1 |
| Honest scope | 1 | 1 |
| **Total** | **2 / 8** | **8 / 8** |

**Delta:** +6.

## Observations

The baseline output is closer to the MCP-attached output here than in the GTTA / CA cases. The reason: the Iran-state / IRGC-affiliated / Iran-private commercial actor distinction is well-known in Hormuz underwriting commentary, and the bare model surfaces it correctly even without the regional lens. The baseline also correctly identifies the corridor-vs-point-estimate framing and names the right advisory sources.

The MCP-attached output adds value in three specific places: explicit scenario probability ranges (where the bare model just says "fat-tailed"), failure-mode level discipline (named, likelihood × impact, mitigation each), and the operational decomposition of recommended actions into trigger + time horizon. Where the bare model gives a list of "what to watch," the structured output gives indicator + trigger + source type — which is what an agent-driven workflow can actually act on programmatically.

This eval suggests the MCP value-add is largest on questions where the bare model lacks substantive priors (CBAM mechanics, regional CA banking), and smallest on questions where the bare model has rich priors (Hormuz underwriting is well-trodden in LLM training data). The structural delta is still substantial, but it's mostly framing discipline, not new substance.

## Limitations

- One model, one prompt run. Not statistically significant.
- Self-scored.
- The Gulf+ME regional lens specifically requires preserving Iran-state / IRGC-affiliated / Iran-private commercial distinctions; the bare model did surface this, but on lower-tension questions it often collapses them. This eval would underestimate the regional lens's value on those harder cases.
- The agent-eval is structural, not factual. Specific underwriting practice would require live market data.
