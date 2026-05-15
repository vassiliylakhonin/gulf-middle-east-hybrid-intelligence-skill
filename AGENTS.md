# AGENTS.md

## Project identity

Gulf + Middle East Hybrid Intelligence Skill is a vertical specialist skill for AI agents working on the Gulf Cooperation Council states, Iran, Iraq, maritime chokepoints (Hormuz, Bab-el-Mandeb, Red Sea), Levant when material, sanctions, AML, energy, banking, sovereign wealth flows and geopolitical risk.

Use this positioning:

> Gulf & Middle East specialist skill for AI agents working on Iran sanctions, GCC financial and energy hubs, maritime chokepoint risk, and regional geopolitical exposure.

This repo is a domain skill, not an infrastructure product.

## Relationship to the broader stack

Agenda Intelligence MD:
- validation
- schemas
- evidence audit
- scoring
- CLI / MCP / CI tooling where implemented

Global Think Tank Analyst:
- broad strategic-risk memo workflows
- general policy-risk analysis
- scenario and red-team memo modes

Central Asia + Caspian Hybrid Intelligence Skill:
- Central Asia / Caspian regional specialist
- adjacent vertical for sanctions-circumvention, corridor and BO patterns

Gulf + Middle East Hybrid Intelligence Skill:
- specialist Gulf, Iran, Iraq, maritime-chokepoint risk reasoning
- Iran sanctions, GCC banking and sovereign wealth, energy market and shipping route analysis patterns

Source Ingest skill (Agenda Intelligence MD):
- use before analysis when a user provides a PDF, DOCX, XLSX, URL, article, or transcript
- normalizes the document into a structured source record: metadata, Axis A/B provenance tags, key claims table, excerpts, limitations
- for routing, load `docs/source-guide.md` from this repo — it defines the regional source tier hierarchy, freshness horizons, and specific URL pointers for Gulf / Middle East analysis
- do not duplicate source-guide content inside the source record; reference it

## Preflight: cold-start interview and practice profile

Before producing memos in a workflow that expects user-specific calibration, run the cold-start interview defined in [`docs/cold-start-interview.md`](docs/cold-start-interview.md). It captures role, geography, decision context, risk appetite, source access, and required actor distinctions (Iran-state / IRGC / Iran-private commercial) into [`templates/practice-profile.md`](templates/practice-profile.md), which downstream memos use as the default `Decision / Audience / Geography / Time horizon` block.

**STOP rule:** if `templates/practice-profile.md` is missing or contains `[PLACEHOLDER]` markers when a memo is requested in a profile-expecting workflow, stop and run the interview before producing output. Generic memos with unstated audience are worse than no memo.

Skip the preflight when the user supplies the four anchors inline, when a populated profile already covers the current question, or for explicit one-off `reasoning-only` runs with stated scope.

## Currency watch

Fast-moving regional topics that any source-backed memo should re-verify against current primary sources are listed in [`docs/currency-watch.md`](docs/currency-watch.md). The file is not a database of current facts — it is a list of *what to re-check now*, with a 90-day staleness rule. Update the `Last reviewed` date at the top and per-topic when adding or refreshing entries.

Do not duplicate Agenda Intelligence MD inside this repo.
Do not duplicate Central Asia + Caspian skill content; reference it when a flow crosses both regions.
Do not turn this repo into a CLI, MCP server, screening engine, or validation platform unless explicitly requested.

## Scope

Core scope:
- Gulf Cooperation Council (Saudi Arabia, UAE, Qatar, Kuwait, Bahrain, Oman)
- Iran
- Iraq
- maritime chokepoints (Hormuz, Bab-el-Mandeb, Red Sea / Suez approaches)
- Iran sanctions, US/EU/UK secondary sanctions, OFAC SDN exposure
- correspondent banking and trade-finance routes through Gulf hubs
- sovereign wealth deployment (PIF, ADIA, Mubadala, QIA, KIA)
- oil and LNG market dynamics; OPEC+ behavior
- shipping, tanker tracking, dark-fleet patterns
- Houthi / Red Sea attacks; Iranian proxy network exposure
- Levant (Lebanon, Syria, Jordan) when material to flows
- US-Iran negotiation status; nuclear file
- Israel-Gulf normalization and adjacent regional risk
- US-China-EU energy and supply-chain exposure to Gulf

Expand geography only when it changes the mechanism, risk exposure, leverage, or decision. Do not expand geography for decoration.

Out of scope:
- North Africa unless directly tied to a Gulf/Iran flow (Morocco, Algeria, Tunisia → Maghreb specialist)
- Turkey except as Iran-flow conduit or Iraq-Kurdistan flow
- Israel-Palestine internal political detail (use specialist sources)
- terrorism analysis beyond financial/sanctions transmission

## Evidence rules

Every example must state its evidence mode:
- live-source-backed
- user-provided sources
- illustrative source packet
- reasoning-only

Do not fabricate:
- citations
- sanctions designations
- legal conclusions
- compliance conclusions
- company facts
- ownership structures
- enforcement actions
- vessel names or IMO numbers
- dates
- statistics
- prices
- regulatory changes

If facts are not verified, say so.

Use labels where helpful:
- Verified
- Plausible
- Judgment
- Unknown

## Safety and limitation rules

This repo must not claim to provide:
- legal advice
- compliance advice
- sanctions screening
- AML transaction monitoring
- vessel screening or maritime due diligence
- investment advice
- factual verification by itself
- live source retrieval by itself
- guaranteed correctness
- production-grade risk controls

Avoid exaggerated claims:
- revolutionary
- best-in-class
- fully autonomous
- guarantees compliance
- solves hallucinations
- detects sanctions evasion
- detects dark-fleet activity

Use careful language:
- helps structure analysis
- supports analyst-style reasoning
- requires source-backed verification for factual claims
- does not replace professional review

## Analytical style

Prefer mechanism-first reasoning.

Good output should include:
- bottom line
- scope and evidence mode
- primary driver
- risk transmission mechanism
- exposure map
- actor incentives and leverage
- role-based implications
- trigger points
- unknowns
- confidence
- what would change the judgment
- limitation note

Avoid:
- generic geopolitical essays on the Middle East
- alarmism without transmission channel
- fake precision (oil-price forecasts, vessel counts without source)
- overconfident forecasting on Iran nuclear or US-Iran negotiation outcomes
- unsupported legal/compliance conclusions
- vague "monitor closely" recommendations
- conflating Iran-state, IRGC-affiliated, and Iran-private commercial actors without distinction

## README priorities

README should make value clear in 30 seconds.

Recommended structure:
1. One-line positioning
2. Problem
3. Try this prompt
4. What it does
5. What it is not
6. Relationship to Agenda Intelligence MD, Global Think Tank Analyst, and Central Asia + Caspian Skill
7. Quick usage
8. Before / after
9. Flagship examples and examples learning path
10. Signal archive
11. Skill files
12. Source guide
13. Risk archetypes
14. Review checklist
15. Limitations
16. Roadmap

## Examples

Examples should be concrete and role-relevant.

Preferred examples:
- Iran sanctions adjacency for an energy buyer
- maritime chokepoint disruption (Hormuz / Bab-el-Mandeb) for a shipping insurer or industrial buyer
- Gulf correspondent banking exposure for a Western respondent bank
- sovereign wealth deployment risk for a target company or co-investor
- dark-fleet / sanctioned-oil flow exposure for a refiner or trader
- Iraq banking-sector reform exposure for a fintech or correspondent bank

Every example must include evidence mode and limitation note.

Examples should be navigable as a learning path, not only as a flat file list. Keep `examples/README.md` aligned with the flagship examples section in `README.md`.

## Evaluation docs

Use honest labels:
- review checklist
- starter rubric
- failure modes

Do not call it a benchmark unless benchmark cases and results actually exist.

## Validation

If validation scripts exist, run them before finalizing changes.

Prefer additive improvements.
Do not introduce heavy dependencies unless necessary.

## Definition of done

The repo aims to clear two bars in sequence. Bar 1 is the threshold for being a credible artifact. Bar 2 is the threshold for being an externally validated specialist resource. The repo's `STATUS.md` must always state honestly which bar has been cleared and which has not. **Do not pretend a bar is cleared if it is not.**

### Bar 1 — Early but credible (the minimum bar)

A senior AI or agent engineering reviewer should understand that this repo is not a generic regional prompt. It should read as an early but credible vertical specialist skill for Gulf + Middle East strategic-risk agents, with evidence discipline, mechanism-first reasoning, examples, source guidance and clear limitations. Specifically:

- **B1.1** README follows the 14-section structure in "README priorities".
- **B1.2** All four canonical evidence modes are demonstrated by at least one example each.
- **B1.3** All preferred examples in "Examples" exist or are explicitly deferred with a reason.
- **B1.4** `evals/` has a review checklist, a starter rubric and a failure-modes file with honest labels (no benchmark claim).
- **B1.5** Validation script exists and passes — or is explicitly deferred with a reason in `STATUS.md`.
- **B1.6** Honesty constraints in "Safety and limitation rules" are observed everywhere.

### Bar 2 — Externally validated specialist resource (the harder bar)

The criteria below close the weaknesses that Bar 1 alone cannot close. Each criterion is binary: either met with verifiable evidence, or not.

- **B2.1 — Source-anchored majority.** At least half of the flagship examples in `examples/` are `live-source-backed` or `user-provided sources` (not `reasoning-only` or `illustrative source packet`). Source-backed examples must cite primary URLs (regulators, OFAC, IFIs, FATF/MENAFATF, central banks, IMO, court records) for legal-grade claims, with secondary reporting clearly tiered.
- **B2.2 — External review.** At least one reviewer outside the author has reviewed at least one example and one application of the starter rubric, and either (a) findings have been incorporated, or (b) the response is explicitly addressed and recorded. The reviewer must be identifiable.
- **B2.3 — Validated cases (not a benchmark).** At least three memos produced with the skill have been reviewed by a domain practitioner (sanctions compliance, AML, energy trading, shipping, Gulf banking, Iran-watcher analyst) and labeled as either "useful in their workflow" or "useful with the specified revisions". Stored in a `validated-cases/` directory. **This is not a benchmark.** No aggregated scores; no claims of "X% accuracy".
- **B2.4 — Platform differentiation or consolidation.** Each variant in `skills/{codex,claude,openclaw}/SKILL.md` either has at least one platform-specific feature that meaningfully changes output, or is consolidated.
- **B2.5 — Honest real-use evidence.** Either the repo links to at least one public, attributable real-use record, or the README and `STATUS.md` explicitly state that no real-use evidence exists yet.
- **B2.6 — Source freshness discipline.** `live-source-backed` examples carry a retrieval date; documented re-verification practice in `docs/source-guide.md`. Examples beyond the horizon are refreshed or labeled stale.
- **B2.7 — Independent rubric application.** At least one application of `evals/starter-rubric.md` to a memo has been performed by someone other than the author, with their scorecard added under their attribution.

### Anti-criteria (things that do **not** count as progress toward done)

- Adding more `reasoning-only` examples once Bar 1 is cleared. Source-anchored ratio is the binding constraint.
- Adding worked scorecards by the same author to imply external validation.
- Renaming a starter rubric a "benchmark" without underlying validated cases.
- Adding adoption-style language ("used by", "trusted by", "production-grade") without B2.5 evidence.
- Adding more topics, badges or boilerplate without a corresponding substance change.

### Honest current status

Current honest status (2026-05-12):

- **Bar 1 — cleared.** B1.1, B1.2, B1.4, B1.5 (validation script, 0 errors), B1.6 met. B1.3 partial (5 of 6 preferred examples; dark-fleet deferred with documented reason — requires live AIS primary sources).
- **Bar 2 — partially cleared.** B2.1 met (3 of 5 examples source-anchored, 60%). B2.6 met (re-verification horizons in source-guide.md; live-source-backed examples carry retrieval dates). B2.5 honest (no real-use evidence disclosed). B2.2, B2.3, B2.7 not met — require external humans. B2.4 met (two platform variants: claude with Claude Projects/web-search setup, codex with agentic-loop output discipline and JSON output mode). Single-author state; no external review, no validated cases.

Future contributors must update this status truthfully as criteria are met, and must not advance the status without verifiable evidence.
