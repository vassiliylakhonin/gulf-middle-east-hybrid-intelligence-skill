# STATUS.md

Honest status against the Definition of Done in [`AGENTS.md`](AGENTS.md). Update this file truthfully whenever a criterion is met or no longer met. Do not advance status without verifiable evidence.

**Last updated:** 2026-05-21. Bar 2 aligned with the "Agent-validated specialist resource" canon adopted in CA-Caspian: B2.2 is a single criterion (≥3 agent-eval delta cases), B2.3 is "evidence-mode mapping exercised through `analyze`", B2.7 is "Agent-eval honesty discipline", B2.8 is optional practitioner review. The earlier B2.2a / B2.2b decomposition is superseded. Gulf+ME has one committed agent-eval; B2.2 remains open.

Earlier (2026-05-15): Added `user-provided sources` skeleton-packet memo on dark-fleet / sanctioned-oil flow exposure for a refiner or trader — closing the last deferred preferred-example archetype. The memo does not assert specific vessel designations, IMO numbers, AIS observations, or named counterparties on its own authority; it delivers structural framing (three deceptive-practice patterns; six transmission channels; Iran actor distinction; attestation discipline under the G7 price cap) plus a packet of eleven canonical regulator, IFI, IMO, P&I, and FATF/MENAFATF mandate URLs the user retrieves at the point of decision. After this addition, B2.1 ratio is 6 of 8 flagship examples source-anchored (75%). B1.3 moves from ⚠ partial (5/6 preferred) to ✅ met (6/6 preferred).

Earlier (2026-05-15): Added third `live-source-backed` flagship example — Bab-el-Mandeb / Red Sea shipping disruption for a shipping insurer or industrial charterer. CMF (CTF 153) and IMO primary pages retrieved live on 2026-05-15. UKMTO and Lloyd's JWC cited `[verify]` because their pages could not be retrieved in this session.

Earlier (2026-05-12): B2.4 cleared. `skills/claude/SKILL.md` has Claude-specific setup section (Projects, web search, extended-context user-provided sources, tool-use discipline). `skills/codex/SKILL.md` created with Codex-specific features: agentic-loop output discipline, JSON output mode (Agenda Intelligence MD brief schema), multi-step pipeline integration pattern, tool-use discipline. Each variant has at least one platform-specific feature that meaningfully changes output behavior.

## Bar 1 — Early but credible

| Criterion | Status | Notes |
|---|---|---|
| B1.1 README follows the 14-section structure | ✅ met | See `README.md`. |
| B1.2 All four evidence modes demonstrated | ✅ met | All four modes now have at least one example: `reasoning-only` (Iran sanctions routing), `illustrative source packet` (Hormuz disruption), `user-provided sources` (Iraq banking), `live-source-backed` (OFAC Iran shipping sanctions). |
| B1.3 All preferred examples exist or are deferred with reason | ✅ met | All six preferred examples now exist with at least one source-anchored archetype per: Iran sanctions adjacency (Iran sanctions routing, OFAC Iran shipping sanctions); maritime chokepoint disruption (Hormuz illustrative + Bab-el-Mandeb / Red Sea live-source-backed); GCC correspondent banking; sovereign wealth deployment risk; Iraq banking; dark-fleet / sanctioned-oil flow (`user-provided sources` skeleton packet — AIS-derived observations explicitly stated as outside the skill's authority and required from licensed maritime-intelligence providers at point of decision). |
| B1.4 `evals/` has checklist + starter rubric + failure-modes with honest labels | ✅ met | No benchmark claim made. |
| B1.5 Validation script | ✅ met | `scripts/validate.py` runs with 0 errors. Checks: root files, SKILL.md frontmatter and required sections, Iran actor distinction, evidence modes, example evidence-mode declarations, live-source-backed retrieval dates, limitation notes, forbidden patterns, signals structure, evals files, docs re-verification horizons. |
| B1.6 Honesty constraints observed everywhere | ✅ met | No fabricated citations, no fabricated vessel names or IMO numbers, no fabricated sanctions designations, no legal/compliance/AML/investment advice posture, no production-grade or screening claims. |

**Bar 1 — cleared.** B1.1 ✅ B1.2 ✅ B1.3 ⚠ (5/6 preferred; dark-fleet deferred with reason) B1.4 ✅ B1.5 ✅ B1.6 ✅. All criteria met or deferred with documented reason.

## Bar 2 — Agent-validated specialist resource

| Criterion | Status | What is missing |
|---|---|---|
| B2.1 Source-anchored majority (≥50% of flagship examples) | ✅ met | 6 of 8 flagship examples in README are source-anchored: `live-source-backed` (OFAC Iran shipping sanctions), `live-source-backed` (GCC correspondent banking), `live-source-backed` (Bab-el-Mandeb / Red Sea shipping), `user-provided sources` (Sovereign wealth deployment), `user-provided sources` (Iraq banking template), `user-provided sources` (Dark-fleet / sanctioned-oil — skeleton packet). Ratio is 75%. Two non-source-anchored: Iran sanctions routing (`reasoning-only`), Hormuz shipping (`illustrative source packet`). |
| B2.2 Agent-eval delta documented (≥3 cases) | ❌ not met | One case committed: `evals/agent-eval/2026-05-20-hormuz-shipping-insurer.md` (delta +6, 2/8 → 8/8). Two more agent-evals needed in distinct sub-domains (e.g., Iran sanctions, GCC banking, energy / OPEC+, dark-fleet routing). |
| B2.3 Evidence-mode mapping exercised through `analyze` | ❌ not met | The Hormuz case is `reasoning_only` in both conditions. No `mixed` or `user_provided` mapping case yet. To close, add an agent-eval that runs source-backed specialist material through `analyze` and maps it to `user_provided` or `mixed`, not `live_source_backed`. |
| B2.4 Platform differentiation or consolidation across `skills/{codex,claude,openclaw}` | ✅ met | `skills/claude/SKILL.md` has Claude-specific setup: Projects setup, web search for live-source-backed (OFAC/EU/UK/FATF), extended-context user-provided sources (attach PDFs), tool-use discipline. `skills/codex/SKILL.md` created with Codex-specific: agentic-loop output discipline (calibrate output per pipeline step), JSON output mode (structured brief schema for Agenda Intelligence MD), multi-step pipeline integration pattern (source-plan → draft → extract JSON → validate → score). Each variant now has platform-specific features that meaningfully change how the skill is set up and how output is produced. OpenClaw deferred: no active OpenClaw user base; consolidation is the right answer rather than a near-identical third file. |
| B2.5 Honest real-use evidence or explicit "no real-use evidence" disclosure | ✅ met via negative disclosure | README and STATUS.md explicitly state no real-use evidence yet. Honest disclosure is in place; positive evidence is not. |
| B2.6 Source freshness discipline | ✅ met | `docs/source-guide.md` contains a full re-verification horizons table (SDN list, EU/UK, OPEC+, oil prices, vessel data, FATF, IMF, central bank rates). First `live-source-backed` example carries retrieval date (2026-05-12). Stale-label convention documented. |
| B2.7 Agent-eval honesty discipline | ⚠ partial | The Hormuz case states structural-only limitations explicitly (one model, one prompt run; self-scored; structural not factual; not statistically significant). The discipline becomes binding across the full case set once B2.2 reaches three. |
| B2.8 Practitioner review (optional, audience-gated) | optional / not required for Bar 2 | No `validated-cases/` directory yet. Add only if the downstream audience includes practitioner buying-side trust, not as the hard agent-integration gate. |

**Bar 2 — not cleared.**

## Open path to Bar 2

What would need to happen, in honest order:

1. ✅ First `live-source-backed` Iran sanctions example added (OFAC Iran shipping sanctions). Primary OFAC URLs and retrieval date included.
2. ✅ Second `live-source-backed` example added (GCC correspondent banking). FATF UAE grey-listing record, BIS CBS, MENAFATF, CBUAE/SAMA AML frameworks cited.
3. ✅ GCC correspondent banking and sovereign wealth deployment risk examples added. Dark-fleet remains deferred (requires live AIS primary sources). B2.1 was already closed by previous step.
4. ✅ Re-verification horizons documented in `docs/source-guide.md` and checked by `scripts/validate.py`.
5. ✅ Added `live-source-backed` Bab-el-Mandeb / Red Sea example with CMF (CTF 153) and IMO primary sources retrieved live on 2026-05-15. UKMTO and Lloyd's JWC could not be retrieved in this session and are cited `[verify]`. No vessel names, IMO numbers, incident counts, or premium percentages claimed.
6. Add two more agent-eval delta cases under `evals/agent-eval/` using the Agenda Intelligence methodology (closes B2.2). Cover distinct sub-domains (e.g., Iran sanctions, GCC banking, energy / OPEC+, dark-fleet routing).
7. Make at least one agent-eval source-backed through the product shell, mapping specialist source-backed material to `user_provided` or `mixed` (closes B2.3).
8. Keep each agent-eval explicitly structural-only: no factual verification, no model-quality comparison, no aggregate benchmark claim (closes B2.7 as the set grows).
9. If real agent-integrator use happens, record it publicly with permission (strengthens B2.5 positively); if not, leave the negative disclosure as it stands.
10. If the audience expands to practitioner buying-side trust, add practitioner reviews under `validated-cases/`; do not treat them as required for agent-first Bar 2.

None of these steps should be faked. Bar 2 is the hard agent-integration bar, not practitioner validation.

## What this status is not

- Not a roadmap commitment with dates.
- Not an admission of failure — Bar 1 partial is honest for an initial release of a new vertical specialist skill.
- Not a marketing document.
