# Companion patterns

How to compose this skill with the other repos in the portfolio. These are structural patterns; for current interfaces, schemas and tooling, consult those repos directly.

## With Global Think Tank Analyst

Use Global Think Tank Analyst (GTTA) for the broader memo workflow (intake, evidence-mode declaration, scenarios, options, indicators, confidence, what-would-change-the-judgment). Use this skill to add Gulf + Middle East depth: Iran actor distinctions, GCC banking and sovereign wealth specifics, maritime chokepoint mechanics, dark-fleet patterns, OFAC/EU/UK sanctions handling.

Suggested composition:

1. Frame the memo with GTTA's intake block (`Question / Decision / Audience / Time horizon / Evidence mode`).
2. Apply this skill's regional logic to scope the analysis (Gulf core, conditional extension, Iran actor distinction).
3. Use GTTA's memo modes (Quick Brief, Standard, Scenario, Red-Team, Decision Pack) for output structure.
4. Apply this skill's risk archetypes and source guide for mechanism and source discipline.
5. Apply GTTA's self-check before finalizing.

## With Central Asia + Caspian Hybrid Intelligence Skill

Cross-reference the Central Asia + Caspian skill when a flow crosses both regions:
- Iran-Caspian routes (Iran-Azerbaijan-Russia, Iran-Turkmenistan, Iran-Caspian shipping).
- Iraq-Iran-Turkey corridor flows.
- Russia-Iran-China tri-junction in oil and dual-use goods routing.
- Sanctions-circumvention patterns that move from Central Asia transshipment to Gulf/Iran end-use, or vice versa.

Do not duplicate Central Asia + Caspian content here. State the cross-reference and let the regional specialist handle the Central Asian leg.

## With Agenda Intelligence MD

For the current primary handoff:

- Produce the regional memo with facts, assessments, assumptions, scenarios, and unknowns kept distinct.
- Select externally checkable factual and quantitative claims; do not serialize analyst judgments as sourced facts.
- Build the claim/source packet described in [`docs/evidence-packet-handoff.md`](evidence-packet-handoff.md).
- Run `agenda-intelligence check evidence-packet.json --strict`.
- Use missing references, quote mismatches, weak lexical support, unmatched numbers, and reviewer actions to revise the packet or originating memo.

This skill does not lint the packet itself. Agenda Intelligence MD reports packet completeness, not factual truth, sanctions status, vessel identity, ownership, or operational clearance. The older brief-schema, scoring, `analyze`, and MCP paths remain compatibility workflows for callers that explicitly depend on them.

## Pattern: Hormuz disruption memo

A typical end-to-end pattern for a Hormuz disruption analysis:

1. **GTTA intake** — frame the decision (e.g., European industrial energy buyer over 90 days).
2. **This skill — regional logic** — Gulf core + Bab-el-Mandeb if the user has Red Sea exposure too.
3. **This skill — risk archetype #5** — maritime chokepoint disruption mechanism.
4. **This skill — source guide** — IEA, EIA, IMO, war-risk insurance market, AIS aggregate data sources.
5. **GTTA — Mode C scenario brief or Mode E decision pack** — structure the output.
6. **Evidence-packet extraction** — select externally checkable claims and caller-supplied source text; keep scenarios and judgments in the memo.
7. **Agenda Intelligence MD** — lint packet completeness before human review.
