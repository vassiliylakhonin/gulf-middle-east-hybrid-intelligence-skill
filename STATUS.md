# STATUS.md

Honest status against the Definition of Done in [`AGENTS.md`](AGENTS.md). Update this file truthfully whenever a criterion is met or no longer met. Do not advance status without verifiable evidence.

**Last updated:** 2026-05-12. First `live-source-backed` example added.

## Bar 1 — Early but credible

| Criterion | Status | Notes |
|---|---|---|
| B1.1 README follows the 14-section structure | ✅ met | See `README.md`. |
| B1.2 All four evidence modes demonstrated | ✅ met | All four modes now have at least one example: `reasoning-only` (Iran sanctions routing), `illustrative source packet` (Hormuz disruption), `user-provided sources` (Iraq banking), `live-source-backed` (OFAC Iran shipping sanctions). |
| B1.3 All preferred examples exist or are deferred with reason | ⚠ partial | Three of six preferred examples in initial release: Iran sanctions adjacency (refiner), Hormuz disruption (insurer), Iraq banking (correspondent). Deferred with reason in `examples/README.md`: GCC correspondent banking exposure, sovereign wealth deployment risk, dark-fleet / sanctioned-oil flow. |
| B1.4 `evals/` has checklist + starter rubric + failure-modes with honest labels | ✅ met | No benchmark claim made. |
| B1.5 Validation script | ❌ not met / deferred | No validation script in initial release. Skill file structure follows the Central Asia + Caspian sibling skill's frontmatter and section conventions; a structural validator is on the roadmap. |
| B1.6 Honesty constraints observed everywhere | ✅ met | No fabricated citations, no fabricated vessel names or IMO numbers, no fabricated sanctions designations, no legal/compliance/AML/investment advice posture, no production-grade or screening claims. |

**Bar 1 — partially cleared.** B1.1, B1.2, B1.4, B1.6 are clean; B1.3 is partial; B1.5 is deferred with reason.

## Bar 2 — Externally validated specialist resource

| Criterion | Status | What is missing |
|---|---|---|
| B2.1 Source-anchored majority (≥50% of flagship examples) | ⚠ partial | Currently 2 of 4 flagship examples are source-anchored: `user-provided sources` (Iraq banking) and `live-source-backed` (OFAC Iran shipping sanctions). Ratio is 50% — borderline. Needs at least one more `live-source-backed` or `user-provided sources` example to comfortably clear. |
| B2.2 At least one external reviewer of an example and a rubric application | ❌ not met | All current scorecards (none yet) would be author judgments. No external reviewer recorded. |
| B2.3 At least three validated cases by domain practitioners | ❌ not met | Directory does not exist. No practitioner-attributed reviews. |
| B2.4 Platform differentiation or consolidation across `skills/{codex,claude,openclaw}` | ⚠ partial | Only `skills/claude/SKILL.md` exists. Deliberate consolidated starting position. Adding Codex/OpenClaw variants requires platform-specific features that change output, otherwise consolidation is the right answer. |
| B2.5 Honest real-use evidence or explicit "no real-use evidence" disclosure | ⚠ partial | README and STATUS explicitly state no real-use evidence yet. Honest disclosure is in place; positive evidence is not. |
| B2.6 Source freshness discipline | ⚠ partial | First `live-source-backed` example carries retrieval date (2026-05-12) and a re-verification horizon table in the source table. Documented re-verification horizons for all source types still missing from `docs/source-guide.md` — that addition closes B2.6. |
| B2.7 Independent rubric application by someone other than the author | ❌ not met | No external scorecard added. |

**Bar 2 — not cleared.**

## Open path to Bar 2

What would need to happen, in honest order:

1. ✅ First `live-source-backed` Iran sanctions example added (OFAC Iran shipping sanctions). Primary OFAC URLs and retrieval date included.
2. Add at least one `live-source-backed` Hormuz / Red Sea / Bab-el-Mandeb example with IMO and IEA primary sources.
3. Add documented re-verification horizons to `docs/source-guide.md` (closes B2.6 once source-backed examples exist).
4. Add deferred examples (GCC correspondent banking, sovereign wealth, dark-fleet) — at least two as `user-provided sources` to push source-anchored ratio above 50% (closes B2.1).
5. Recruit at least one external reviewer for one example and one rubric application; record their attribution (closes B2.2 and B2.7).
6. Run the skill against ≥3 real practitioner workflows; store outcomes in `validated-cases/` with attribution (closes B2.3).
7. If real use happens, record it publicly with permission (closes B2.5 positively).

None of these steps should be faked. Bar 2 is the hard bar.

## What this status is not

- Not a roadmap commitment with dates.
- Not an admission of failure — Bar 1 partial is honest for an initial release of a new vertical specialist skill.
- Not a marketing document.
