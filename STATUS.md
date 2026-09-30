# STATUS.md

## Maintenance update — 2026-09-30

UK source routing now uses UK Sanctions List. Catalogue maintenance is separated
from primary-source checks; only the UK migration notice was re-checked in this
change. Other topic claims remain unverified. The runtime contract loads regional
references explicitly and uses the four canonical memo evidence modes.

Specialist-lift protocol 2 pins the full regional reference package and case
context, requires all saved outputs, exports blind judge packets, and calculates
scores from justified per-item decisions. It rejects numeric totals, missing or
changed answers, inconsistent applicability, and same-vendor judges with different
model IDs. Saved-byte hashes are integrity receipts, not proof of model authorship.
No generator or judge run has been executed and no substantive lift is claimed.
Older preparations remain unchanged and must be re-prepared before scoring.
A equal to B does not itself invalidate C minus B; a small null result does not
establish equivalence. Interpret prior retirement guidance in that limited sense.

Honest status against the Definition of Done in [`AGENTS.md`](AGENTS.md). Update this file truthfully whenever a criterion is met or no longer met. Do not advance status without verifiable evidence.

## What the invariants and the bars mean

Maturity is tracked on two axes.

**Continuous invariants (C1–C4)** must hold at every commit and *can regress*. They cover whether the repo currently works, not how much work has been done. A cleared bar never entitles the repo to a failing invariant, and an invariant failure takes precedence over new bar work.

**Bars** are sequential and one-way. Full criteria live in [`docs/definition-of-done.md`](docs/definition-of-done.md); the short version:

- **Bar 1 — Early but credible.** Structural minimum for a vertical specialist skill: README follows the section structure in [`docs/repo-conventions.md`](docs/repo-conventions.md) "README priorities", all four evidence modes (`live-source-backed`, `user-provided sources`, `illustrative source packet`, `reasoning-only`) demonstrated, all preferred examples present, an `evals/` triad (checklist + rubric + failure-modes) with honest labels, validation passing, no exaggerated claims.
- **Bar 2 — Agent-validated specialist resource.** The agent-integration bar: source-anchored majority of flagship examples, at least three agent-eval delta cases, evidence-mode mapping exercised through Agenda Intelligence MD's `analyze` tool, platform differentiation (or honest consolidation) across runtime variants, source freshness discipline, and explicit structural-only honesty on every agent-eval. B2.8 (practitioner review) is optional and audience-gated.
- **Bar 3 — Demonstrated specialist lift.** The bar that tests the repo's actual claim: that this vertical changes the *substance* of an answer beyond the horizontal method alone. Bar 2 measured structure, and a structural rubric rewards any well-formed skill file. Bar 3 measures substance under a pre-registered rubric, a three-condition protocol (no skill / horizontal only / horizontal + vertical), and a blind different-family judge. **Bar 3 can be cleared by a null result** — if the vertical demonstrably adds nothing, the honest outcome is to fold its content into the horizontal method and retire the separate repo.

Each criterion is binary: met with verifiable evidence, or not. Anti-criteria in `AGENTS.md` and `docs/definition-of-done.md` list moves that do *not* count as progress.

**Update (2026-08-30, later):** C1 and C2 fixed and verified; both now met. The `mcp` pin is `mcp>=2.0,<3` across the portfolio, the server ships as the namespaced package `gulf_middle_east_compliance_server`, and CI installs the package before running tests so the invariants are checked rather than asserted. Package version bumped 0.1.0 → 0.2.0: the import path changed. Bar 3 remains **not attempted**.

**Update (2026-08-30):** Added the continuous-invariant axis (C1-C4) and Bar 3 (demonstrated specialist lift). No previously recorded bar status was changed — cleared bars stay cleared, and rewriting them retroactively would break the audit trail this file exists to keep. Two invariants are recorded as **not met** on first assessment (C1, C2); both are verified defects in the executable surface, not new criteria applied to old work. Bar 3 is recorded as **not attempted**.

**Last updated:** 2026-08-24. The root skill now carries the complete runtime-neutral contract. A structural smoke test verified root-plus-Claude loading through the packaged skill and explicit root-plus-Codex loading. Existing `analyze` agent-eval delta cases remain compatibility evidence for the older strategic-intelligence runtime; they do not validate the current evidence-packet linter.

Current Agenda composition: this repo produces regional reasoning and an optional claim/source packet; Agenda Intelligence MD lints packet completeness before human review. The linter does not assess factual truth.

Update (2026-05-21, later in day): Added two new agent-eval delta cases — `evals/agent-eval/2026-05-21-dark-fleet-sanctioned-oil-mixed.md` (refiner / dark-fleet / sanctioned-oil; upstream `live-source-backed` + `user-provided sources` mapped through `analyze` as `mixed`; delta +6, 3/9 → 9/9) and `evals/agent-eval/2026-05-21-gcc-correspondent-tiering.md` (Western respondent bank tiering of GCC correspondents; `reasoning_only`; delta +5.5, 2.5/8 → 8/8). B2.2 ✅ (three agent-evals across distinct sub-domains: chokepoint underwriting, dark-fleet adjacency, GCC banking). B2.3 ✅ (dark-fleet case exercises `mixed` mapping). B2.7 ✅ across the full case set (each writeup states structural-only, self-scored, not factual / not model-quality / not aggregate). Added `evals/agent-eval/README.md` mirroring the CA-Caspian pattern.

Update (2026-05-27): Added `evals/skill-improvement/`, a SkillOpt-inspired improvement loop with JSONL stress cases, a manual structural rubric, a case validator, and before/after run notes. This is explicitly not a benchmark, certification, factual validation, sanctions screen, AML review, maritime-intelligence product, investment recommendation, or operational safety assessment. The change supports B1.4/B2.7 honesty discipline but does not create new real-use or practitioner-validation evidence.

Earlier (2026-05-15): Added `user-provided sources` skeleton-packet memo on dark-fleet / sanctioned-oil flow exposure for a refiner or trader — closing the last deferred preferred-example archetype. The memo does not assert specific vessel designations, IMO numbers, AIS observations, or named counterparties on its own authority; it delivers structural framing (three deceptive-practice patterns; six transmission channels; Iran actor distinction; attestation discipline under the G7 price cap) plus a packet of eleven canonical regulator, IFI, IMO, P&I, and FATF/MENAFATF mandate URLs the user retrieves at the point of decision. After this addition, B2.1 ratio is 6 of 8 flagship examples source-anchored (75%). B1.3 moves from ⚠ partial (5/6 preferred) to ✅ met (6/6 preferred).

Earlier (2026-05-15): Added third `live-source-backed` flagship example — Bab-el-Mandeb / Red Sea shipping disruption for a shipping insurer or industrial charterer. CMF (CTF 153) and IMO primary pages retrieved live on 2026-05-15. UKMTO and Lloyd's JWC cited `[verify]` because their pages could not be retrieved in this session.

Earlier (2026-05-12): B2.4 cleared. `runtimes/claude/SKILL.md` has Claude-specific setup section (Projects, web search, extended-context user-provided sources, tool-use discipline). `runtimes/codex/SKILL.md` created with Codex-specific features: agentic-loop output discipline, JSON output mode (Agenda Intelligence MD brief schema), multi-step pipeline integration pattern, tool-use discipline. Each variant has at least one platform-specific feature that meaningfully changes output behavior.

## Continuous invariants

Checked at every commit. These can regress. All four currently hold; C1 and C2 were recorded as failing on 2026-08-30 and fixed the same day, which is the axis working as intended.

| Invariant | Status | Evidence |
|---|---|---|
| C1 Declared executables run on a clean install | ✅ met | Verified end to end on a clean venv built only from the declared dependencies: `pip install -e .` resolves mcp 2.1.1, the console script `gulf-middle-east-compliance-server` starts, completes the MCP `initialize` handshake, and returns all three tools from `tools/list`. `scripts/validate.py` and the `unittest` suite also pass. CI installs the package before running tests, so this is checked on every commit rather than asserted. Previously not met: an unbounded `mcp>=1.2.0` pin against `from mcp.server.fastmcp import FastMCP`, which mcp 2.x renamed to `MCPServer` — the pin is now `mcp>=2.0,<3` and the whole portfolio targets the same major version. |
| C2 Package installs as a namespaced package | ✅ met | `pyproject.toml` declares a `[build-system]` block and `[tool.setuptools.packages.find]`. The wheel's `top_level.txt` contains exactly `gulf_middle_east_compliance_server`; nothing is installed at the top level of `site-packages`. The intra-package import is relative (`from .contract import ...`) and no longer depends on the working directory. `tests/test_mcp_contract.py` imports through the installed name, and `PackagingInvariantTests` asserts that the server module imports and that all three tools are registered — so the test now exercises the shipped artifact rather than a file path. |
| C3 No tool returns a fabricated finding | ✅ met | Every declared tool in `src/gulf_middle_east_compliance_server/server.py` returns `not_implemented` with `result_is_not_a_finding` and `human_review_required`. `test_every_declared_tool_refuses_rather_than_answering` now calls each tool through the server and checks the payload, and `test_structured_contract_cannot_approve_or_enforce` asserts that `schemas/compliance-decision.schema.json` cannot express `approve`, `block` or `freeze_funds` and that `human_review_required` is `const: true`. Enforced by test, not by prose. |
| C4 Documentation references resolve | ✅ met | `scripts/validate.py` checks tracked Markdown links and own-site links on every commit; currently passing. |

Invariant failures are defects, not roadmap items, and rank ahead of any bar work.

## Bar 1 — Early but credible

| Criterion | Status | Notes |
|---|---|---|
| B1.1 README follows the "README priorities" structure | ✅ met | See `README.md`. |
| B1.2 All four evidence modes demonstrated | ✅ met | All four modes now have at least one example: `reasoning-only` (Iran sanctions routing), `illustrative source packet` (Hormuz disruption), `user-provided sources` (Iraq banking), `live-source-backed` (OFAC Iran shipping sanctions). |
| B1.3 All preferred examples exist or are deferred with reason | ✅ met | All six preferred examples now exist with at least one source-anchored archetype per: Iran sanctions adjacency (Iran sanctions routing, OFAC Iran shipping sanctions); maritime chokepoint disruption (Hormuz illustrative + Bab-el-Mandeb / Red Sea live-source-backed); GCC correspondent banking; sovereign wealth deployment risk; Iraq banking; dark-fleet / sanctioned-oil flow (`user-provided sources` skeleton packet — AIS-derived observations explicitly stated as outside the skill's authority and required from licensed maritime-intelligence providers at point of decision). |
| B1.4 `evals/` has checklist + starter rubric + failure-modes with honest labels | ✅ met | No benchmark claim made. |
| B1.6 Honesty constraints observed everywhere | ✅ met | No fabricated citations. |

**Bar 1 — cleared.** B1.1 ✅ B1.2 ✅ B1.3 ✅ (6/6 preferred) B1.4 ✅ B1.5 ✅ B1.6 ✅.

## Bar 2 — Agent-validated specialist resource

| Criterion | Status | What is missing |
|---|---|---|
| B2.1 Source-anchored majority (≥50% of flagship examples) | ✅ met | 6 of 9 flagship examples in README are source-anchored: three `live-source-backed` and three `user-provided sources`. Ratio is 67%. The three non-source-anchored examples are Iran sanctions routing (`reasoning-only`), Hormuz shipping (`illustrative source packet`), and the Iran crude-export tracker source-conflict case (`illustrative source packet`). |
| B2.2 Agent-eval delta documented (≥3 cases) | ✅ met | Three agent-evals committed across distinct Gulf sub-domains: `evals/agent-eval/2026-05-20-hormuz-shipping-insurer.md` (chokepoint underwriting, `reasoning_only`, delta +6, 2/8 → 8/8); `evals/agent-eval/2026-05-21-dark-fleet-sanctioned-oil-mixed.md` (dark-fleet / sanctioned-oil adjacency for a refiner, `mixed` mapping, delta +6, 3/9 → 9/9); `evals/agent-eval/2026-05-21-gcc-correspondent-tiering.md` (GCC correspondent banking tiering for a Western respondent bank, `reasoning_only`, delta +5.5, 2.5/8 → 8/8). All three self-scored; each writeup states structural-only limitations. |
| B2.3 Evidence-mode mapping exercised through `analyze` | ✅ met | The dark-fleet / sanctioned-oil case (`2026-05-21-dark-fleet-sanctioned-oil-mixed.md`) maps upstream `live-source-backed` regulatory framework (OFAC Iran shipping sanctions example, retrieved 2026-05-12) plus upstream `user-provided sources` skeleton packet (eleven canonical OFAC / EU / UK / FATF / IMO / P&I / IMB / UKMTO mandate-page URLs, accessibility-checked 2026-05-15) into Agenda Intelligence `analyze` as `mixed`. `live_source_backed` is not used at the product-shell layer; the schema constraint is exercised. |
| B2.4 Platform differentiation or consolidation across `runtimes/{codex,claude,openclaw}` | ✅ met | Common behavior is consolidated in the root `SKILL.md`. Claude adds retrieval and document-use rules; Codex adds agent-loop, JSON-output, and validation-chaining rules. A [structural smoke test](evals/2026-08-24-runtime-loading-smoke.md) verified package loading in Claude and explicit root-plus-overlay loading in Codex. OpenClaw remains deferred because there is no active OpenClaw use case; the complete root contract can be used without an overlay. The validator rejects duplicated common sections, package-name drift, and missing or reordered Claude composition references. |
| B2.5 Honest real-use evidence or explicit "no real-use evidence" disclosure | ✅ met via negative disclosure | README and STATUS.md explicitly state no real-use evidence yet. Honest disclosure is in place; positive evidence is not. |
| B2.6 Source freshness discipline | ✅ met | `docs/source-guide.md` contains a full re-verification horizons table (SDN list, EU/UK, OPEC+, oil prices, vessel data, FATF, IMF, central bank rates). First `live-source-backed` example carries retrieval date (2026-05-12). Stale-label convention documented. |
| B2.7 Agent-eval honesty discipline | ✅ met | All three agent-evals state structural-only limitations explicitly: one model, one prompt run; self-scored; structural not factual; not statistically significant; not model-quality comparison; not aggregate benchmark; not compliance / sanctions / vessel screening; not practitioner validation. |
| B2.8 Practitioner review (optional, audience-gated) | optional / not required for Bar 2 | No `validated-cases/` directory yet. Add only if the downstream audience includes practitioner buying-side trust, not as the hard agent-integration gate. |

**Bar 2 — cleared for agent integration.** B2.1 ✅ (67% source-anchored). B2.2 ✅ (three agent-evals: Hormuz, dark-fleet, GCC correspondent). B2.3 ✅ (dark-fleet case exercises `mixed` mapping). B2.4 ✅. B2.5 ✅ via negative disclosure. B2.6 ✅. B2.7 ✅ across full case set. B2.8 optional / not required for agent-first Bar 2.

## Open path to Bar 2

What would need to happen, in honest order:

1. ✅ First `live-source-backed` Iran sanctions example added (OFAC Iran shipping sanctions). Primary OFAC URLs and retrieval date included.
2. ✅ Second `live-source-backed` example added (GCC correspondent banking). FATF UAE grey-listing record, BIS CBS, MENAFATF, CBUAE/SAMA AML frameworks cited.
3. ✅ GCC correspondent banking and sovereign wealth deployment risk examples added. Dark-fleet remains deferred (requires live AIS primary sources). B2.1 was already closed by previous step.
4. ✅ Re-verification horizons documented in `docs/source-guide.md` and checked by `scripts/validate.py`.
5. ✅ Added `live-source-backed` Bab-el-Mandeb / Red Sea example with CMF (CTF 153) and IMO primary sources retrieved live on 2026-05-15. UKMTO and Lloyd's JWC could not be retrieved in this session and are cited `[verify]`. No vessel names, IMO numbers, incident counts, or premium percentages claimed.
6. ✅ Added two more agent-eval delta cases under `evals/agent-eval/` (closes B2.2). Distinct sub-domains: dark-fleet / sanctioned-oil adjacency for a refiner (`2026-05-21-dark-fleet-sanctioned-oil-mixed.md`) and GCC correspondent banking tiering for a Western respondent bank (`2026-05-21-gcc-correspondent-tiering.md`).
7. ✅ Made one agent-eval source-backed through the product shell with `mixed` mapping (`2026-05-21-dark-fleet-sanctioned-oil-mixed.md`); upstream `live-source-backed` regulatory framework and `user-provided sources` skeleton packet map into `analyze` as `mixed`, not `live_source_backed` (closes B2.3).
8. ✅ Each agent-eval states structural-only limitations explicitly (closes B2.7 across the case set).
9. If real agent-integrator use happens, record it publicly with permission (strengthens B2.5 positively); if not, leave the negative disclosure as it stands.
10. If the audience expands to practitioner buying-side trust, add practitioner reviews under `validated-cases/`; do not treat them as required for agent-first Bar 2.

None of these steps should be faked. Bar 2 is the hard agent-integration bar, not practitioner validation.

## Bar 3 — Demonstrated specialist lift

**Instrument prepared; generation and blind scoring not performed.** Five preparation criteria are met with the model-drafted-rubric limitation below; no substantive result exists. This is the honest state, not a deferral: Bar 2 was cleared in May–August 2026 and no measurement of substantive lift has been run since.

Recorded plainly because it is the load-bearing gap in this repo. The Bar 2 agent-eval deltas are large (2/8 → 8/8, 3/9 → 9/9, 2.5/8 → 8/8), and every one of those writeups states that the rubric is structural. A structural rubric shows a large delta for any well-formed skill file. **There is currently no evidence that the Gulf + Middle East content adds anything over the horizontal method (`global-think-tank-analyst`) on its own.** That is the claim the repo is named for.

| Criterion | Status | What is missing |
|---|---|---|
| B3.1 Substantive rubric, pre-registered (≥8 checkable substantive items) | ✅ prepared — author review pending | Eight model-drafted, reference-derived items in `evals/specialist-lift/rubric.md`; no factual validation claimed. |
| B3.2 Three-condition protocol documented (no skill / horizontal only / horizontal + vertical) | ✅ prepared | Protocol 2 defines A/B/C with identical question, declared tool access and generation settings; C receives the complete reference package. |
| B3.3 ≥5 cases under `evals/specialist-lift/`, ≥3 distinct archetypes | ✅ prepared | Six cases across five documented archetypes, including one negative control. |
| B3.4 Blind, different-family judge | ❌ not met | One Bar 2 case (`2026-06-30-sdn-premise-stop.md`) used two blind judges including a cross-vendor one — the right method, applied to a structural rubric. Reusable here. |
| B3.5 Lift reported per case, including null and negative | ❌ not met | Nothing measured yet. |
| B3.6 ≥1 negative control (region should not change the substance) | ✅ prepared | UAE fintech retraining-cadence control; regional framing should not change the governance trade-offs. |
| B3.7 Re-runnable harness | ✅ prepared | Dependency-free prepare/judge/score harness with refusal tests and receipt recomputation; no provider calls. |
| B3.8 Scope statement on every Bar 3 case | ❌ not met | No generated or scored reports yet. |

### Open path to Bar 3

1. Review the eight model-drafted rubric items against their named regional references.
2. Select actual generator/judge identifiers from different vendor families; prepare and commit a protocol-2 run.
3. Generate every A/B/C output with the declared settings, record telemetry, export blind packets, and commit receipts.
4. Score every applicable item with reasons and positive evidence spans; publish all case results, including null and negative.
5. Review controls and repeat before making usefulness, equivalence or retirement claims. See `evals/specialist-lift/README.md`.


## What this status is not

- Not a roadmap commitment with dates.
- Not an admission of failure — Bar 1 partial is honest for an initial release of a new vertical specialist skill.
- Not a marketing document.
