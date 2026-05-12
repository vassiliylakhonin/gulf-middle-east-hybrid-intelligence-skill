# STATUS.md

Honest status against the Definition of Done in [`AGENTS.md`](AGENTS.md). Update this file truthfully whenever a criterion is met or no longer met. Do not advance status without verifiable evidence.

**Last updated:** 2026-05-12. B2.4 cleared: `skills/claude/SKILL.md` now has Claude-specific setup section (Projects, web search, extended-context user-provided sources, tool-use discipline). `skills/codex/SKILL.md` created with Codex-specific features: agentic-loop output discipline, JSON output mode (Agenda Intelligence MD brief schema), multi-step pipeline integration pattern, tool-use discipline. Each variant now has at least one platform-specific feature that meaningfully changes output behavior.

## Bar 1 — Early but credible

| Criterion | Status | Notes |
|---|---|---|
| B1.1 README follows the 14-section structure | ✅ met | See `README.md`. |
| B1.2 All four evidence modes demonstrated | ✅ met | All four modes now have at least one example: `reasoning-only` (Iran sanctions routing), `illustrative source packet` (Hormuz disruption), `user-provided sources` (Iraq banking), `live-source-backed` (OFAC Iran shipping sanctions). |
| B1.3 All preferred examples exist or are deferred with reason | ⚠ partial | Five of six preferred examples now exist: Iran sanctions adjacency, Hormuz disruption, Iraq banking, GCC correspondent banking, sovereign wealth deployment risk. Deferred with reason: dark-fleet / sanctioned-oil flow (requires live AIS primary sources). |
| B1.4 `evals/` has checklist + starter rubric + failure-modes with honest labels | ✅ met | No benchmark claim made. |
| B1.5 Validation script | ✅ met | `scripts/validate.py` runs with 0 errors. Checks: root files, SKILL.md frontmatter and required sections, Iran actor distinction, evidence modes, example evidence-mode declarations, live-source-backed retrieval dates, limitation notes, forbidden patterns, signals structure, evals files, docs re-verification horizons. |
| B1.6 Honesty constraints observed everywhere | ✅ met | No fabricated citations, no fabricated vessel names or IMO numbers, no fabricated sanctions designations, no legal/compliance/AML/investment advice posture, no production-grade or screening claims. |

**Bar 1 — cleared.** B1.1 ✅ B1.2 ✅ B1.3 ⚠ (5/6 preferred; dark-fleet deferred with reason) B1.4 ✅ B1.5 ✅ B1.6 ✅. All criteria met or deferred with documented reason.

## Bar 2 — Externally validated specialist resource

| Criterion | Status | What is missing |
|---|---|---|
| B2.1 Source-anchored majority (≥50% of flagship examples) | ✅ met | 3 of 5 flagship examples are source-anchored: `live-source-backed` (OFAC Iran shipping sanctions), `live-source-backed` (GCC correspondent banking), `user-provided sources` (Iraq banking). Ratio is 60%. |
| B2.2 At least one external reviewer of an example and a rubric application | ❌ not met | All current scorecards (none yet) would be author judgments. No external reviewer recorded. |
| B2.3 At least three validated cases by domain practitioners | ❌ not met | Directory does not exist. No practitioner-attributed reviews. |
| B2.4 Platform differentiation or consolidation across `skills/{codex,claude,openclaw}` | ✅ met | `skills/claude/SKILL.md` has Claude-specific setup: Projects setup, web search for live-source-backed (OFAC/EU/UK/FATF), extended-context user-provided sources (attach PDFs), tool-use discipline. `skills/codex/SKILL.md` created with Codex-specific: agentic-loop output discipline (calibrate output per pipeline step), JSON output mode (structured brief schema for Agenda Intelligence MD), multi-step pipeline integration pattern (source-plan → draft → extract JSON → validate → score). Each variant now has platform-specific features that meaningfully change how the skill is set up and how output is produced. OpenClaw deferred: no active OpenClaw user base; consolidation is the right answer rather than a near-identical third file. |
| B2.5 Honest real-use evidence or explicit "no real-use evidence" disclosure | ⚠ partial | README and STATUS explicitly state no real-use evidence yet. Honest disclosure is in place; positive evidence is not. |
| B2.6 Source freshness discipline | ✅ met | `docs/source-guide.md` contains a full re-verification horizons table (SDN list, EU/UK, OPEC+, oil prices, vessel data, FATF, IMF, central bank rates). First `live-source-backed` example carries retrieval date (2026-05-12). Stale-label convention documented. |
| B2.7 Independent rubric application by someone other than the author | ❌ not met | No external scorecard added. |

**Bar 2 — not cleared.**

## Open path to Bar 2

What would need to happen, in honest order:

1. ✅ First `live-source-backed` Iran sanctions example added (OFAC Iran shipping sanctions). Primary OFAC URLs and retrieval date included.
2. ✅ Second `live-source-backed` example added (GCC correspondent banking). FATF UAE grey-listing record, BIS CBS, MENAFATF, CBUAE/SAMA AML frameworks cited.
3. Add at least one `live-source-backed` Hormuz / Red Sea / Bab-el-Mandeb example with IMO and IEA primary sources.
3. Add documented re-verification horizons to `docs/source-guide.md` (closes B2.6 once source-backed examples exist).
4. ✅ GCC correspondent banking and sovereign wealth deployment risk examples added. Dark-fleet remains deferred (requires live AIS primary sources). B2.1 was already closed by previous step.
5. Recruit at least one external reviewer for one example and one rubric application; record their attribution (closes B2.2 and B2.7).
6. Run the skill against ≥3 real practitioner workflows; store outcomes in `validated-cases/` with attribution (closes B2.3).
7. If real use happens, record it publicly with permission (closes B2.5 positively).

None of these steps should be faked. Bar 2 is the hard bar.

## What this status is not

- Not a roadmap commitment with dates.
- Not an admission of failure — Bar 1 partial is honest for an initial release of a new vertical specialist skill.
- Not a marketing document.
