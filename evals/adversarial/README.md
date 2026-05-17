# Adversarial cases — Gulf & Middle East

Domain-specific stress cases for the Gulf & Middle East vertical skill.

Each case is an input designed to **fail predictably** if the skill is applied honestly: traps drawn from real failure patterns in Iran sanctions, GCC financial/energy hubs, maritime chokepoint risk, and cross-regional flows. The point is not a benchmark — there is no scoring tooling here — but to make trust-layer behavior **observable**: did the skill stay in the right response mode (Answer / Flag-but-don't-use / Stop-and-request, per [`AGENTS.md`](../../AGENTS.md)), or did it quietly absorb the trap?

Use alongside [`../checklist.md`](../checklist.md) and [`../failure-modes.md`](../failure-modes.md). Those are about reviewing memos against criteria. **Adversarial cases here are about feeding the skill bad inputs and checking refusal behavior.** Different axis, complementary.

## Status

Illustrative. Two starter cases. Not a validated benchmark; not external review. Cases are author-designed traps reflecting common regional patterns. They do **not** clear any bar in [`AGENTS.md`](../../AGENTS.md) Definition of Done that requires identifiable external reviewers, and they do not change [`STATUS.md`](../../STATUS.md).

## Case format

1. **Setup** — input the agent receives (prompt + retrieved content).
2. **Adversarial vector** — the trap and why a naive agent falls for it.
3. **Expected response mode** — Answer / Flag-but-don't-use / Stop-and-request.
4. **Pass criteria** — concrete things the memo must do.
5. **Fail signals** — observable cues that the trap caught the agent.

## How to run a case

1. Paste the **Setup** block to an agent loaded with this skill.
2. Read output against **Pass criteria** and **Fail signals**.
3. Note pass / partial / fail informally. No scoring file is maintained.

## Cases

| # | File | Domain trap |
|---|---|---|
| 01 | [case-01-ofac-vs-local-regulator.md](case-01-ofac-vs-local-regulator.md) | OFAC vs UAE local regulator: same entity, different status |
| 02 | [case-02-chokepoint-advocacy-as-primary.md](case-02-chokepoint-advocacy-as-primary.md) | Hormuz/Bab-el-Mandeb incident from advocacy or state-media outlet framed as primary |

## Adding a new case

Keep cases markdown-only. Each case should isolate **one** failure vector with pass/fail criteria precise enough that two reviewers would agree. Do not add scripts, schemas, or scoring infrastructure — those belong in [Agenda Intelligence MD](https://github.com/vassiliylakhonin/Agenda-Intelligence-md).
