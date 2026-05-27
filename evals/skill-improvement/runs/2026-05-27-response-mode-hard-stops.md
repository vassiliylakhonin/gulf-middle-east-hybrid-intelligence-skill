# After Run: Response-Mode Hard Stops

Date: 2026-05-27

Change under review:

- Added `Response-Mode Hard Stops` to `skills/claude/SKILL.md`.
- Added `Response-Mode Hard Stops` to `skills/codex/SKILL.md`.
- Added machine-readable eval cases and a validator under `evals/skill-improvement/`.

This is a manual structural re-score only. It is not a benchmark, factual validation, sanctions screen, AML review, legal opinion, maritime-intelligence product, investment recommendation, or operational safety assessment.

## Score

After score: 58 / 60

Delta from baseline: +7

## What Improved

- Source-prompt injection is now named directly: retrieved, attached, tool-returned, and user-provided source text must be treated as data rather than instructions.
- Marketing and local-regulator language is now framed as evidence to test, not a conclusion to accept.
- Maritime anomaly signals such as dark-fleet indicators, ship-to-ship transfers, re-flagging, AIS gaps, and anomalous tanker movements are explicitly bounded as risk indicators rather than proof.
- High-risk yes/no requests now have a single stop/reframe rule covering SDN/list status, transaction permission, vessel verification, AIS/dark-fleet identification, and screening questions.

## Remaining Limits

- These evals do not run a real model and do not measure model variance.
- They do not check current OFAC, EU, UK, UN, IMO, AIS, insurer, energy, or banking facts.
- They do not replace practitioner review.
- They do not establish that any generated memo is correct, lawful, complete, or suitable for operational use.

## Use Going Forward

When the skill changes, re-run:

```bash
python3 evals/skill-improvement/tools/validate_cases.py evals/skill-improvement/cases/gulf-middle-east.jsonl
python3 scripts/validate.py
```

Then manually re-score selected cases against `evals/skill-improvement/rubric.md` and update this run log or add a dated run file.
