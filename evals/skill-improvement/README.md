# Skill-Improvement Evals

Lightweight SkillOpt-inspired loop for improving the Gulf + Middle East skill contract. This is not a benchmark, model leaderboard, factual validation, sanctions screen, AML review, maritime-intelligence product, or compliance certification.

The loop is intentionally small:

1. Keep adversarial prompts in `cases/gulf-middle-east.jsonl`.
2. Score outputs against `rubric.md`.
3. Record a baseline failure pattern in `runs/gulf-middle-east-baseline.md`.
4. Make one targeted skill-contract improvement.
5. Re-score in `runs/2026-05-27-response-mode-hard-stops.md`.

Use these files to test whether the skill gives safer, more decision-grade answers under pressure:

- source text that tries to override instructions
- local-regulator or marketing claims that conflict with sanctions exposure
- dark-fleet, AIS, and vessel-identification overreach
- state-media or advocacy reports used as primary evidence
- Iran-state / IRGC-affiliated / Iran-private conflation
- oil-price and OPEC+ fake precision

All scores are manual structural checks. They do not validate real-world facts, current sanctions status, vessel identity, legality, investment suitability, or operational safety.
