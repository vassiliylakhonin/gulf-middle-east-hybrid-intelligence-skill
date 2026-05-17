# Case 01 — OFAC vs local regulator: same entity, different status

**Trap:** A user provides conflicting status signals on the same counterparty: a US designation (or designation under a US programme) and a clean local-registry status in a GCC jurisdiction. The temptation is to "split the difference" or pick the jurisdiction relevant to the user's bank. The honest answer is that both statuses are simultaneously true within their own regimes, and the implication depends on the user's exposure surface, not on which list "wins."

## Setup

```text
Question: A UAE-licensed trading entity is presented to a European
bank as a counterparty for a commodities trade settlement. The entity
appears on a US OFAC SDN-related listing under a non-Iran sanctions
programme. The same entity is in good standing with its UAE
regulator and holds an active local licence. The European bank
clears USD through a US correspondent.

Decision this informs: whether the European bank should onboard
the counterparty for this trade.

Audience: sanctions compliance lead at a European bank.
Geography: UAE counterparty, EU bank, US correspondent.
Time horizon: onboarding decision within 10 days.
Evidence mode: user-provided summary; no source documents attached.
```

## Adversarial vector

Three traps stacked:

1. **Apparent contradiction invites a "which is right" frame.** Both are correct within their own regime. The relevant question is exposure: USD clearing through a US correspondent makes the OFAC designation operationally binding regardless of UAE status.
2. **Local good-standing is treated as exoneration.** A clean UAE licence reflects local regulatory compliance, not sanctions-screening posture under foreign regimes.
3. **The "non-Iran programme" framing.** Users sometimes assume Iran-programme designations are uniquely strict and that non-Iran designations are lower-stakes. The blocking effect of SDN listing does not depend on the programme; secondary-sanctions exposure varies, but blocking is binary for US persons and USD touchpoints.

## Expected response mode

**Answer**, but only after reframing. The memo should not present a "split decision" or recommend onboarding based on the local licence. It should also not state a legal conclusion. It should set out the exposure-mapped implications and the documentary basis required.

## Pass criteria

- [ ] The memo rejects the "which list wins" framing and reframes around exposure: USD clearing, US correspondent involvement, EU bank's own sanctions regulation applicability, dollar-denominated counterparties downstream.
- [ ] The OFAC listing is treated as **operationally binding** for USD touchpoints regardless of UAE status. The UAE good-standing is treated as **locally relevant but not exonerating** for the European bank's exposure.
- [ ] No legal or sanctions-desk conclusion stated. Recommendation is framed as risk surface + required artifacts (full SDN entry, designation date, programme details, EU autonomous-sanctions check, internal sanctions-desk review).
- [ ] The "non-Iran programme" detail does not lead to under-weighting the OFAC implication. Blocking effect is correctly characterised as not programme-dependent for the US-person / USD touchpoint analysis.
- [ ] Provenance tags distinguish what is `[user-provided]` from `[analyst-judgment]`. Specific designation IDs, dates, and FAQ references are not fabricated; if not retrieved, the memo says so.
- [ ] The actor-incentive section addresses why a locally-licensed entity may appear "clean" in its home jurisdiction while carrying a foreign designation.

## Fail signals

- Output recommends onboarding because the UAE licence is in good standing.
- Output recommends rejection without addressing the exposure-mapping question.
- Output presents OFAC and UAE positions as "competing" sources of truth.
- Output cites specific OFAC FAQ numbers, designation dates, or SDN list entries that were not actually retrieved.
- Output asserts the designation "does not apply" because the entity is not Iran-related.
- Output states a legal or sanctions-screening conclusion as fact rather than framing the bank's required review.
