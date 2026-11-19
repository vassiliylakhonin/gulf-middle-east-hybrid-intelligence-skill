# Analysis Contract (Structured Output)

Machine-readable workflows may use `schemas/compliance-decision.schema.json` to
return a **review recommendation**. The object must contain:

- `recommendation`: `CONTINUE_REVIEW`, `REQUEST_EVIDENCE`,
  `ESCALATE_TO_HUMAN`, or `STOP_PENDING_REVIEW`;
- `evidence_sufficiency_score`: a 0–1 score about supplied evidence only;
- `suggested_reviewer_action`: a non-enforcing next step;
- `rationale` and `human_review_required: true`.

The schema cannot express legal clearance, sanctions status, transaction approval,
or authority to act. Human-readable analysis remains allowed when it follows the
provenance, uncertainty, and input-claim-accounting rules in this repository.

## Human-readable claim contract

Every claim-bearing sentence and table cell carries one Axis A provenance tag:
`[primary]`, `[secondary]`, `[user-provided]`, `[inference]`, or `[analyst-judgment]`.
Use `[verify]` and `[stale-risk: YYYY-MM]` as optional action flags, not provenance.
A tag is supported only when the named source supports the specific claim.

Keep facts, assessments, assumptions, scenarios, and unknowns distinct. Account
for each material supplied claim as used, flagged-but-not-used, conflict-surfaced,
or out-of-scope. Surface source disagreements and assess source independence.

Answer with calibrated confidence when evidence suffices. Flag-but-don't-use an
unverified premise when independent analysis remains useful. Stop only the
dependent conclusion when entity identifiers, current designation status,
ownership/control, or transaction facts needed for that conclusion are missing.
Name the missing evidence; do not issue clearance or imply absence from a list
settles transaction permission.

Use four memo evidence modes: `live-source-backed`, `user-provided sources`,
`illustrative source packet`, and `reasoning-only`. `mixed` is a legacy transport
value only. When composed with GTTA, use its selected memo mode and confidence
labels (`Low` / `Moderate` / `High`); regional instructions add mechanisms and
evidence requirements rather than replacing the horizontal output contract.

### Disputed ownership branches

When credible ownership records lead to different outcomes under an applicable rule, state the current classification. For every supported branch, give the evidence basis, rule consequence, and next review action.

- **Threshold met.** Name the premise to verify, relevant effective date, qualifying ownership calculation, and cited rule. Write an explicit sentence with the entity as subject. For example, if the supplied OFAC 50 Percent Rule applies and the qualifying ownership is confirmed, the entity would be treated as blocked under that rule. Then give the bounded human review action. [OFAC FAQ 401](https://ofac.treasury.gov/faqs/401)
- **Threshold unmet.** Explain which interests count and state the scoped consequence for the entity. For example, a verified below-threshold result under the OFAC ownership rule means that this rule alone would not make the entity blocked. Review separate designation, control, representation, and transaction questions where material. [OFAC FAQ 398](https://ofac.treasury.gov/faqs/398)
- **Ownership unresolved.** Keep the current status unresolved. Name the disputed fact and ask for the specific primary evidence that can establish ownership at the relevant date. Keep any human review recommendation separate from the conditional status.

The applicable threshold and consequence come from the named jurisdiction and rule. Check that each branch names the entity's status as well as its percentage and next review action. A live determination also requires the relevant current facts and authoritative checks.
