# Source-conflict surfacing — Iranian crude export tracker divergence (illustrative)

> **Illustrative source packet.** Evidence mode: `illustrative source packet`. No live verification was performed in this environment; figures below are representative of the magnitude and direction of disagreement that commercial maritime-intelligence trackers and official US estimates regularly publish on Iranian crude export volumes, not a snapshot of any specific monthly reporting period. The purpose of this example is to demonstrate how the skill surfaces a load-bearing source conflict in a sanctions-adjacent estimation problem rather than silently resolving it. Do not use the specific numbers below for any operational decision.

**User question:** Our sanctions-risk function needs an assumed Iranian crude export volume for H2 2026 to size dark-fleet / STS exposure modeling and to calibrate counterparty enhanced-diligence triggers. Commercial trackers (Kpler, Vortexa, TankerTrackers) and US official statements disagree by several hundred thousand barrels per day. How should we treat that disagreement in the compliance posture?

```text
Question: H2 2026 Iranian crude export volume disagreement across commercial trackers and US official estimates.
Decision: Assumed-exposure parameter for dark-fleet / STS sanctions-risk modeling and trigger thresholds for enhanced counterparty diligence.
Audience: Head of sanctions risk; head of compliance (refiner or commodity-trading desk).
Time horizon: 6 months.
Evidence mode: illustrative source packet.
Confidence: Moderate, conditional on the conflict being surfaced rather than collapsed.
```

EVIDENCE ACCESS LIMITED: no live verification performed in this environment. Representative figures below are illustrative.

## Executive takeaway

**Key judgment `[analyst-judgment]`:** Commercial maritime-intelligence trackers and US official statements publish materially different Iranian crude export estimates. The divergence is load-bearing for sizing dark-fleet exposure: a posture calibrated to either number alone carries the regret of being under-prepared if the higher case is right or over-restrictive (and competitively disadvantaged) if the lower case is right. Apply **flag-but-don't-use** to the absolute volume figure; calibrate enhanced-diligence triggers to the higher of the commercial-tracker cases for regret-asymmetry reasons, and treat any single tracker's monthly print as a directional signal rather than a level.

## Source conflict (load-bearing)

Multiple credible sources publish materially different H2 Iranian crude export estimates. None is fully independent of the others.

| Position | Source | Provenance | Representative figure (bpd) | Methodology basis |
|---|---|---|---|---|
| Lower official estimate | US Treasury / OFAC public statements (illustrative) | `[primary][verify]` | ~1.0–1.2 mbd | Aggregated intelligence inputs; not method-disclosed |
| Lower commercial tracker | Tracker A (e.g. illustrative Kpler-style) | `[secondary][verify]` | ~1.4–1.6 mbd | AIS + satellite + port-call data; flagged-STS detection |
| Higher commercial tracker | Tracker B (e.g. illustrative Vortexa-style) | `[secondary][verify]` | ~1.6–1.8 mbd | AIS + satellite + cargo-flow inference |
| Higher commercial tracker | Tracker C (e.g. illustrative TankerTrackers-style) | `[secondary][verify]` | ~1.7–2.0 mbd | Satellite imagery + AIS-gap analysis; broader STS-attribution |

**Why this is a real conflict, not noise:**
- The gap between the lowest (US official) and highest (Tracker C) estimates frequently exceeds 0.5–0.8 mbd `[inference]` — large enough to change compliance posture, not a rounding difference.
- The trackers do not converge over time: published monthly figures retain persistent gaps even as more reporting periods accumulate.
- Each source publicly states *different methodologies* for attributing ambiguous STS transfers and AIS gaps. Disagreement is structural, not transient.

**Source independence assessment (critical for Rule 2):**
- **The three commercial trackers are NOT independent.** All three consume overlapping AIS feeds (Spire, Orbcomm, terrestrial AIS aggregators), overlapping satellite imagery providers, and overlapping port-call data. Their methodological differences are in *attribution* of ambiguous signals, not in the underlying signal inputs.
- **US official estimates draw on classified collection** that the trackers do not access; in that narrow respect, the official estimate is partially independent — but the public *figure* is not method-disclosed and is itself partly informed by commercial-tracker reporting in the unclassified record `[analyst-judgment]`.
- **Agreement between any two commercial trackers does NOT count as independent corroboration.** Agreement between US official figures and a commercial tracker likewise should not be over-weighted: the official side may be partly downstream of the commercial side in the unclassified channel.

**Preferred position for compliance modeling — and why:** The **higher commercial-tracker range** is preferred as the calibration anchor for enhanced-diligence triggers, not because it is more likely correct, but because compliance regret is asymmetric: under-detecting dark-fleet exposure carries direct sanctions / secondary-sanctions risk and reputational cost on disclosure; over-detecting causes operational friction and competitive cost, both reversible. The official lower figure is preserved as a sensitivity case — if compliance posture is later challenged externally as over-restrictive, the official figure is the natural defense reference.

**What is NOT done:** averaging the four figures into a single point estimate. Averaging would silently collapse the methodological disagreement and embed a number none of the sources publishes.

## Facts (where the sources actually agree)

- **Fact `[secondary]`:** Iranian crude continues to flow at materially non-zero volumes through 2024–2026 despite the sanctions regime; the disagreement is about how much, not whether.
- **Fact `[secondary]`:** STS transfers and AIS manipulation are documented features of the Iranian export chain across all source types.
- **Fact `[primary]`:** OFAC has continued to designate Iran-linked vessels, traders, and front companies through 2024–2026, indicating ongoing assessed flow at scale.

## Assessments (linguistic faithfulness)

- **Assessment `[analyst-judgment]` (Moderate confidence):** The structural cause of the disagreement appears to lie in how each source attributes ambiguous STS transfers in the Persian Gulf and eastern Mediterranean — counted as Iranian-origin by aggressive attribution; counted as Gulf-blend by conservative attribution `[inference]`.
- **Assessment `[analyst-judgment]` (Low–Moderate confidence):** If the gap between US official and commercial-tracker figures narrows materially over consecutive quarters, the convergence direction is informative — narrowing toward the lower number would suggest commercial trackers are over-attributing STS volume; narrowing toward the higher number would suggest official figures are under-counting.
- **Assessment `[analyst-judgment]` (Moderate confidence):** A compliance posture calibrated to the midpoint would likely be the worst of both worlds — over-restrictive against the official case and under-prepared against the higher tracker case.

## Scenarios (6 months)

1. **Persistent divergence, no convergence (most likely).** Compliance posture must remain conflict-aware throughout the period; no single number ever becomes "the" estimate. **Indicators:** monthly tracker prints continue to disagree at current magnitude; US official statements unchanged.
2. **Trackers converge toward lower (official) range.** Suggests over-attribution was real. **Indicators:** Tracker B and C revise methodology disclosures; published gap narrows.
3. **Official figure revised upward toward tracker range.** Suggests classified-channel re-estimation. **Indicators:** Treasury/State Department public statements citing higher volumes; new designations targeting actors implied by tracker attributions.
4. **Major sanctions enforcement action against a named tracker-identified actor.** Resolves the attribution question for that specific flow; does not resolve the aggregate gap. **Indicators:** OFAC SDN additions naming entities previously tracker-flagged; secondary-sanctions enforcement of foreign refiners or banks.

## Options and trade-offs

| Option | Pros | Cons | Provenance |
|---|---|---|---|
| Calibrate diligence triggers to higher tracker range | Asymmetric regret protection; minimizes sanctions-detection failure | Operational friction; counterparty pushback on borderline cargoes | `[analyst-judgment]` |
| Calibrate to US official range | Lower operational friction; defensible against over-restriction challenge | Sanctions-detection gap risk if commercial trackers are closer to true volume | `[analyst-judgment]` |
| Calibrate to midpoint of all four | Simplest implementation | Silently resolves the conflict; worst-of-both regret profile | `[analyst-judgment]` |
| Maintain dual calibration (trigger on higher, defense reference on lower) | Preserves both for different purposes | Operational complexity; requires explicit documentation of when each applies | `[analyst-judgment]` |

## Decision-relevant takeaway

The disagreement between US official figures and commercial trackers on Iranian crude export volume is not a measurement problem that will resolve — it is a structural methodology divergence with overlapping but not independent inputs. Surface this in the compliance-policy memo explicitly. Anchor enhanced-diligence triggers to the higher commercial-tracker range on regret-asymmetry grounds. Preserve the US official figure as a sensitivity / defense reference, not a primary input. Re-evaluate quarterly as the gap narrows, widens, or persists.

## Watch-next indicators

- Monthly publication cycle of major commercial trackers; whether the gap to US official narrows or widens.
- OFAC SDN additions naming actors previously identified by trackers but not by official statements (would shift independence assessment).
- Methodology disclosure changes from any tracker; attribution rule changes for STS in Persian Gulf and eastern Mediterranean.
- US Treasury / State Department public statements citing volume figures (a higher official number would itself reset the conflict).
- New entrants into the maritime-intelligence space with genuinely independent inputs (satellite-only, no AIS) — would change the independence assessment.

## Confidence and key unknowns

- **Confidence: Moderate**, conditional on the methodology above — surfacing the conflict rather than collapsing it. If a desk silently picked any single number as "the" Iran export figure for compliance modeling, confidence in the resulting posture would be Low, regardless of which source was eventually closest to truth.
- **Key unknowns `[verify]`:** the true volume — by definition, not directly observable for sanctions-evading flows; which methodology's attribution rules are closer to reality for STS transfers; whether US official figures incorporate any commercial-tracker data in their unclassified statements (partial dependence vs full independence).

## What would change the judgment

- A genuinely independent estimate from a non-AIS, non-overlapping methodology (e.g., refinery-side inflow analysis from buyer-country customs data) aligning with one source cluster and not the other.
- Convergence of the official and commercial figures within 2 quarters — convergence direction would itself be load-bearing.
- A regulatory ruling or court action requiring compliance teams to use a specific source — would shift the question from "which is right" to "which is required."

## Why this example exists

This memo demonstrates the **source-conflict-surfacing rule** from `AGENTS.md` applied to a sanctions-adjacent estimation problem:

- Four credible sources on a load-bearing fact (Iran export volume) are NOT silently averaged.
- All four positions are named, tagged, and shown with their methodology basis.
- Source independence is explicitly and rigorously assessed — commercial trackers are NOT independent (overlapping AIS / satellite / port-call inputs); US official figures are only partially independent (classified inputs partly offset by unclassified channel feedback).
- A preferred position is stated **with the reason** (regret asymmetry for compliance), not as "we picked Tracker C because Tracker C."
- The conflict is carried through to the decision (dual calibration option) instead of being collapsed at the takeaway.
- Linguistic faithfulness is observed: `[analyst-judgment]` and `[inference]` tags throughout; hedges ("appears to", "would likely", "the higher of") on judgment claims; plain framing reserved for the `[primary]` / `[secondary]` factual layer.

The Iran actor distinction (Iran-state / IRGC-affiliated / Iran-private commercial) is not the subject of this memo — that distinction belongs in the per-actor attribution work that this volume estimate then feeds.

## Limitation note

Illustrative. Figures are representative, not retrieved. Not sanctions, compliance, legal, AML, or trading advice. A real Iran-volume compliance calibration requires current commercial-tracker subscriptions, current OFAC SDN list state, qualified sanctions counsel, and integration with the firm's specific counterparty book.
