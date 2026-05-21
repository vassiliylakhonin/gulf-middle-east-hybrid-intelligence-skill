# Agent-Eval Delta Cases

This directory records structural with/without evaluations for agent integration. These cases test how output shape changes when Agenda Intelligence routes a question through the Gulf + Middle East specialist: provenance, uncertainty, evidence mode, watch-next indicators, role-based actions, Iran-state / IRGC-affiliated / Iran-private commercial actor distinctions, and regional mechanism depth.

Agent-eval delta is not factual verification, not a model-quality comparison, not practitioner validation, and not an aggregate benchmark.

## Completed Cases

- [`2026-05-20-hormuz-shipping-insurer.md`](2026-05-20-hormuz-shipping-insurer.md) — maritime chokepoint / war-risk underwriting for a shipping insurer in `reasoning_only` mode.
- [`2026-05-21-dark-fleet-sanctioned-oil-mixed.md`](2026-05-21-dark-fleet-sanctioned-oil-mixed.md) — source-backed dark-fleet / sanctioned-oil adjacency case for a refiner, exercising `mixed` evidence-mode mapping through Agenda Intelligence `analyze` (upstream `live-source-backed` regulatory framework + `user-provided sources` skeleton packet → `mixed` at the product-shell layer).
- [`2026-05-21-gcc-correspondent-tiering.md`](2026-05-21-gcc-correspondent-tiering.md) — GCC correspondent banking tiering for a Western respondent bank in `reasoning_only` mode (jurisdiction-times-counterparty matrix, UAE FATF remediation trajectory, free-zone BO opacity).

## Planned Cases

Planned files do not count toward B2.2 until both conditions, scoring, observations, and limitations are completed.

No planned files are active at this time.

## Completion Rules

A completed agent-eval must include:

- the exact or reproducible user question;
- model name and date;
- evidence mode;
- Condition A output: same model and question without Agenda Intelligence product shell / MCP specialist routing;
- Condition B output: same model and question with Agenda Intelligence routing to the relevant modules;
- structural scoring for both conditions;
- delta observations;
- limitations stating that the eval is structural only.

Source-backed specialist work passed through Agenda Intelligence `analyze` must use the product-shell evidence modes `user_provided` or `mixed`, not `live_source_backed`.
