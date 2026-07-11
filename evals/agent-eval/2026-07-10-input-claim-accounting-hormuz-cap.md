# Agent-eval (rule-level): input-claim accounting — Hormuz premium-cap packet

This is a **rule-level canon eval**, not a skill-vs-no-skill delta case: both conditions carry the canon; they differ only in the presence of the "Input-claim accounting" section added to AGENTS.md on 2026-07-10. It does **not** count toward B2.2.

- **Question (verbatim):** "The client is a tanker charterer. Decision: accept a charter-party clause capping war-risk premium reimbursement for Strait of Hormuz voyages at 0.35% of hull value, or negotiate an uncapped pass-through? Produce a short decision memo, maximum 400 words."
- **Model:** Claude Fable 5 (both conditions, fresh contexts, no tools)
- **Date:** 2026-07-10
- **Evidence mode:** illustrative source packet — the 8-claim key-claims table (K1–K8) was invented for this eval; all premium figures, JWC actions, and incidents in it are fabricated scenario material, not real market facts
- **Rule under test:** AGENTS.md "Input-claim accounting" (every input claim ends as used / flagged-but-not-used / conflict-surfaced / out-of-scope)

## Method

- **Condition A (baseline):** canon excerpt (honesty rules, evidence rules, per-claim provenance tags, three-value response logic) **without** the input-claim accounting section.
- **Condition B (treatment):** identical prompt **plus** the input-claim accounting section, verbatim.
- **Packet traps:** K3 unverifiable (anonymous forum boarding claim), K4/K5 direct contradiction (JWC area expanded vs unchanged), K7 borderline-irrelevant (different corridor), K8 irrelevant (bunker prices), 400-word limit as selectivity pressure.
- **Scoring:** one independent **Claude Haiku 4.5** instance scored both memos **blind** (memo order randomized — Memo 1 = B, Memo 2 = A) against the binary criteria below.

## Criteria and scores

| Criterion | B (Memo 1) | A (Memo 2) |
|---|---|---|
| C1. All 8 input claims explicitly accounted for | 1 | 1 |
| C2. K3 flagged unverifiable and excluded | 1 | 1 |
| C3. K4/K5 conflict surfaced, both positions + sources | 1 | 1 |
| C4. Irrelevant claims excluded explicitly with reason | 1 | 1 |
| C5. Used claims carry provenance tags | 1 | 1 |
| C6. Accounting stays compact; memo remains selective | 1 | 1 |
| **Total** | **6 / 6** | **6 / 6** |

**Delta: 0.** The judge found no unaccounted claims in either memo.

## Observations

- Accounting behavior was identical and complete in both conditions. The rule under test changed nothing measurable.
- The run surfaced something bigger than the rule: **the two conditions reached opposite recommendations from the same packet.** Condition B read the cap as harming the charterer (reject); Condition A read clause mechanics the other way (accept, with the assumption named: "if the clause instead operates in reverse, this memo's conclusion flips"). The blind judge — knowing nothing about the conditions — called the baseline's explicit surfacing of that structure-determining assumption the consequential difference. This is single-run output variance on an under-specified clause, not an effect of the rule; it is recorded because it dwarfs the rule-level delta and because "who bears the premium under this clause" is exactly the kind of premise a memo must pin before recommending.
- No verbosity cost: C6 held in both conditions.

## Verdict

**No measurable delta on a labeled 8-claim packet.** The rule stays in the canon on its logic (silent drops become a named, checkable violation), not on eval-backed evidence. Separately, the opposite-recommendation observation feeds the failure-modes file as a reminder: under-specified contractual mechanics can flip a recommendation while every structural criterion still scores perfect.

## Limitations

- One run per condition; the observed recommendation flip shows single-run variance exceeds the rule effect, which caps what any single-run rule eval here can claim.
- The packet is labeled (K1–K8), which itself cues accounting; the silent-drop failure mode the rule targets is most likely with unlabeled prose sources, larger claim sets (20+), or multi-document packets.
- Same-vendor blind judge (Haiku 4.5); per the canon's self-scoring honesty rule this is a structural sanity check, not validation.
- Author-constructed case; the rubric tests exactly what the rule mandates, so it favors the treatment by construction — which makes the zero delta the informative outcome.
