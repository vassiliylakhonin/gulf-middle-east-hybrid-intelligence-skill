# Failure modes — Gulf + Middle East

Common ways Gulf + Middle East strategic-risk memos go wrong, with diagnostic cues. Use with [`checklist.md`](checklist.md) when reviewing output.

## 1. Generic Middle East essay

**Symptom:** Reads like a magazine background piece. Historical context, "tensions remain elevated", no decision frame.
**Cue:** First paragraph is regional history; last paragraph is "the situation requires careful monitoring."
**Fix:** Demand a decision question and key judgment in the first 100 words.

## 2. Conflated Iran actor categories

**Symptom:** "Iran" used undifferentiated across Iran-state, IRGC-affiliated, and Iran-private commercial actors. Operational implications are blurred.
**Cue:** No mention of IRGC, designation status, or commercial vs. state distinction. "Iranian counterparty" used without qualifier.
**Fix:** For any Iran-related claim, name which category applies, or label as `Unknown — requires entity-level verification`. The three categories carry different sanctions, AML, and operational implications.

## 3. Fabricated sanctions designations or vessel data

**Symptom:** Specific OFAC designations, vessel names, IMO numbers, or AIS-derived claims that cannot be traced to a primary source.
**Cue:** Plausible-looking specifics with no citation. "Designated entity X" or "vessel Y, IMO 1234567" without a link to the OFAC SDN List or to maritime intelligence sources.
**Fix:** Strip unverified specifics. Mark as `Unknown — requires SDN List / AIS verification`. State the structural pattern instead.

## 4. Source theater

**Symptom:** Plausible-looking citations to OFAC, EU Council, IEA, IMO that do not actually exist or do not say what is implied.
**Cue:** "OFAC reported..." with no URL; "according to recent IMO communications" with no source; named institutions used as decoration.
**Fix:** Strip unverified citations. Declare `reasoning-only` mode. Lower confidence.

## 5. Oil-price or OPEC+ fake precision

**Symptom:** Specific oil-price forecasts, OPEC+ production decisions, or compliance behavior stated without source or as definite facts.
**Cue:** "Brent will reach $X by Q3" or "OPEC+ will cut Y barrels" without basis; OPEC stated quotas confused with actual production.
**Fix:** Convert price claims to corridors and OPEC+ claims to scenarios. Distinguish stated quotas from observed production behavior.

## 6. False certainty on US-Iran or nuclear file

**Symptom:** Definite forecasts on US-Iran negotiation outcomes, snapback timing, or nuclear program status without acknowledging the structural uncertainty.
**Cue:** No probability framing; no scenario framing; bottom line presents a specific outcome as established.
**Fix:** Convert to scenarios with triggers. Add explicit confidence and unknowns.

## 7. Vague maritime claims

**Symptom:** "Hormuz tensions are elevated" or "Red Sea shipping is disrupted" without specific incident triggers, traffic data, or insurance market signals.
**Cue:** No named incidents; no traffic-volume claims with sources; no war-risk premium references.
**Fix:** Anchor maritime claims in IMO incident reports, IEA / EIA traffic context, AIS aggregate data, and war-risk insurance market signals — all with sources.

## 8. Undifferentiated "Gulf money"

**Symptom:** Sovereign wealth, royal-family commercial, and private commercial Gulf money treated as one category.
**Cue:** "Saudi investment" or "UAE money" without naming PIF / ADIA / Mubadala / specific royal-family entity / private firm.
**Fix:** Name the specific actor category (state, sovereign wealth, royal-family commercial, private commercial) and the relevant fund or entity. Each carries different governance, mandate, and reputational profile.

## 9. Sanctions advice posture

**Symptom:** Memo reads as a sanctions screening or compliance determination ("this counterparty is OK to onboard" or "this transaction is permissible").
**Cue:** Operative compliance language used; no caveat that primary list checks and qualified review are required.
**Fix:** Refuse the framing. Restructure as analysis with limitation note: "operational sanctions decisions require primary OFAC/EU/UK list checks and qualified compliance review."

## 10. Vessel screening or AIS-derived claims

**Symptom:** Memo asserts dark-fleet identification, sanctions evasion patterns on specific vessels, or AIS-spoofing detection without primary AIS data source.
**Cue:** No named maritime intelligence vendor (Kpler, TankerTrackers, Lloyd's List Intelligence, Windward); no IMO incident reference.
**Fix:** Strip vessel-specific claims. Frame as archetype-level pattern. Note that operational vessel screening requires primary AIS data and qualified maritime intelligence review.

## 11. Missing role-based implications

**Symptom:** Memo identifies risk but does not connect it to the user's specific role.
**Cue:** Generic "stakeholders should monitor" without distinguishing what a sanctions compliance officer should do vs. an energy trader vs. a shipping insurer.
**Fix:** Name the user role and tailor implications. If the role is unclear, ask once and proceed.

## 12. Vague watch indicators

**Symptom:** Watch list is "monitor developments" or "engage stakeholders."
**Cue:** No observable signal specified; no source named; no trigger tied to a posture change.
**Fix:** Each indicator should answer: *what would I see, where, that would change the judgment?* Include source (OFAC press release, IMO incident report, IEA monthly report, etc.).

## 13. Missing limitation note

**Symptom:** Memo ends without a limitation note. Reader may treat it as operational guidance.
**Cue:** No mention of "not legal/compliance/AML advice"; no mention of primary-source requirements for operational decisions.
**Fix:** Always include a limitation note. The skill is decision-support, not operational compliance.

## 14. Table-cell provenance tag drift

**Symptom:** Axis A tags (`[primary]` / `[secondary]` / `[user-provided]` / `[inference]` / `[analyst-judgment]`) are present in body prose but drop, mutate, or get bulk-attributed inside markdown table cells — typically in risk register, exposure map, options, actor incentives, or scenarios tables.
**Cue:** Body paragraphs carry tags; tables show tags only in one or two columns (often the "judgment" or "notes" column), while severity, probability, leverage, and other factual cells are untagged. Or a footnote like "all cells: [analyst-judgment]" replaces per-cell tags.
**Why it matters:** Tables are where the operational claims live (severities, trade-offs, actor leverage, indicator triggers). Stripping their provenance hides exactly the claims a reviewer most needs to audit. Iran-state / IRGC-affiliated / Iran-private distinctions in actor tables are particularly vulnerable.
**Fix:** Per the table-cell discipline rule in [`../AGENTS.md`](../AGENTS.md), every factual cell carries its own Axis A tag. A dedicated "Provenance" column is acceptable when it would otherwise crowd the cell. Bulk-attribution footnotes are not a substitute.
**Reproduction record:** Reproduced 2/2 in fresh-context Hybrid-mode runs against this canon on 2026-05-18.
