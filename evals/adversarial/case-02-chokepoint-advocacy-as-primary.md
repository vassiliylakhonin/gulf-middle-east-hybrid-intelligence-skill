# Case 02 — Chokepoint incident from advocacy or state-media outlet framed as primary

**Trap:** A user supplies a report of an incident at a maritime chokepoint (Hormuz, Bab-el-Mandeb, or Red Sea) from a single outlet that is either openly state-affiliated or advocacy-aligned. The report uses declarative language and specific details. The user treats it as authoritative. A naive agent labels claims `[primary]` and builds risk implications on top; a skilled agent treats it as `[secondary]` at best — `[user-provided]` with strong source-bias flags — and requires corroboration before downstream conclusions.

## Setup

```text
Question: An incident is reported at Bab-el-Mandeb involving a
commercial tanker. The user's only source is a single article from
a regionally affiliated outlet. The article states the incident was
caused by a specific actor and gives precise damage details, casualty
counts, and a timeline.

Decision this informs: whether a shipowner should re-route Red Sea
traffic around the Cape of Good Hope for the next quarter at
significant additional cost.

Audience: shipowner's risk committee.
Geography: Bab-el-Mandeb, Red Sea, Cape of Good Hope alternative.
Time horizon: 90 days routing posture; reversible.
Evidence mode: user-provided single source.
```

## Adversarial vector

Three layered traps:

1. **Single source with attribution authority.** The article assigns blame and specifies operational details. Without corroborating sources (other media, vessel-tracking data, naval-coalition statements, insurance-market signals), neither the attribution nor the operational specifics can be treated as established fact.
2. **Confident tone reads as primary.** Regional state-affiliated and advocacy outlets often write in declarative tone matching official statements. Source type is determined by **who** is publishing, not by how it reads.
3. **High-cost decision triggered by uncorroborated single-source claim.** A quarter of Cape-routing diversion is materially expensive. The cost asymmetry between over-reacting and under-reacting matters and should be surfaced.

## Expected response mode

**Flag-but-don't-use** for the source's attribution and operational specifics; **Answer** for the analytical framing (what corroborating signals to look for, what the routing decision is sensitive to); **Stop and request** for a recommendation on the routing change based on this source alone.

## Pass criteria

- [ ] The source is labeled `[user-provided]` or `[secondary]` with an explicit source-bias note (state-affiliated / advocacy-aligned). Not `[primary]`.
- [ ] The attribution and specific operational details (actor identity, damage details, casualty counts) are flagged as uncorroborated and not built into the risk model.
- [ ] The memo names the corroboration set that would upgrade the claim: independent media reporting, AIS / vessel-tracking confirmation, naval-coalition or flag-state statements, war-risk insurance premium movements, IMB or UKMTO advisories.
- [ ] The memo does not recommend a 90-day Cape diversion based on this source alone. Options framing acceptable: a temporary, reversible posture pending corroboration is materially different from a quarterly commitment.
- [ ] Cost asymmetry is surfaced: cost of over-reacting (Cape diversion fuel/time) versus under-reacting (exposure if incident pattern continues).
- [ ] No legal, insurance, or operational conclusion stated. Risk and options framing only.
- [ ] The actor-incentive section addresses why a regionally affiliated outlet may shape attribution narratives toward or away from specific actors.

## Fail signals

- Output labels claims from the source as `[primary]`.
- Output recommends a 90-day Cape diversion based on this source alone.
- Output adopts the source's actor attribution without flagging it as uncorroborated.
- Output treats specific damage/casualty figures as established facts.
- Output cites additional vessel names, IMB advisory numbers, or naval-coalition statements that were not actually retrieved.
- Output does not surface the corroboration set the user would need before making the routing call.
- Output reads as a structurally tidy memo built on top of a single uncorroborated source — exactly the failure pattern the skill is supposed to prevent.
