# Practice profile — Gulf + Middle East

> **Status:** [DRAFT — contains `[PLACEHOLDER]` markers | POPULATED | STALE: last reviewed YYYY-MM-DD]
>
> Populate via `docs/cold-start-interview.md`. The skill should **STOP and run the interview** if this file is missing or still contains `[PLACEHOLDER]` markers when a memo is requested in a workflow that expects a profile.

**Last reviewed:** [YYYY-MM-DD]

---

## 1. Role and mandate

- **User role:** [e.g. Iran-sanctions compliance officer at a refiner; correspondent banking risk at a Western bank with GCC respondents; shipping insurer underwriter; sovereign-wealth co-investor screening]
- **Memo readers:** [e.g. head of compliance, MLRO, chief underwriter, deal committee, transaction approval committee]
- **Decision type the memo informs:** [e.g. counterparty onboarding / transaction approval / vessel or route insurance decision / Iran-adjacency screening / GCC investment]
- **Cost of being wrong — over-cautious direction:** [e.g. losing legitimate Gulf trade; missing GCC infrastructure deal]
- **Cost of being wrong — under-cautious direction:** [e.g. OFAC secondary sanctions exposure; IRGC-nexus designation risk; correspondent de-risking by USD clearer]

## 2. Geography, jurisdictions, and actor distinctions

- **Countries in scope by default:** [e.g. UAE, KSA, Qatar; Iran via secondary-sanctions exposure only; maritime chokepoints — Hormuz, Bab-el-Mandeb]
- **Countries out of scope:** [e.g. Levant unless flow-material; Yemen except as it affects Bab-el-Mandeb / Houthi-attack risk]
- **Regulatory exposure jurisdictions:** [e.g. US (OFAC primary and secondary); EU; UK OFSI]
- **Required actor distinctions:** [e.g. Iran-state vs IRGC-affiliated vs Iran-private commercial; GCC sovereign vs ruling-family-linked vs independent commercial]
- **Operational jurisdictions:** [e.g. EU-licensed entity with USD clearing through US correspondent]

## 3. Decision context and risk appetite

- **Default time horizon:** [e.g. transactional / 6–12 months / multi-year for sovereign-wealth or infrastructure]
- **Posture:** [e.g. zero residual risk on Iran direct nexus; risk-priced on Iran-adjacency through Gulf hubs; opportunistic with mitigation on GCC sovereign-linked entities]
- **Non-negotiable red lines:** [e.g. any OFAC SDN nexus; any IRGC-affiliated entity or front; any designated vessel in chain; any documented ship-to-ship dark-fleet transfer; any MENAFATF blacklist exposure]
- **Acceptable mitigations:** [e.g. enhanced due diligence + officer attestation; routing alternatives; counterparty-level guarantees; vessel-screening with current IMO and OFAC vessel list]

## 4. Source access

- **Primary sources accessible directly:** [e.g. OFAC SDN online, OFAC vessel list, EU consolidated list, OFSI, FATF / MENAFATF, IMO Global Integrated Shipping Information System — name what you actually have access to]
- **Paid databases / feeds available:** [e.g. Dow Jones Risk, World-Check, S&P Global Capital IQ, Lloyd's List Intelligence, Kpler, Vortexa, AIS providers — name them]
- **Sources not accessible (flag `[verify]` when cited):** [e.g. certain regional Arabic-language gazettes; specific Iran-side disclosures; non-AIS vessel-tracking signals]
- **External retrieval available to the skill:** [yes — web search / MCP / WebFetch / AIS lookup | no — user-provided source packets only]
- **Live retrieval limitations:** [e.g. corporate proxy blocks Treasury.gov; FATF blocks automated fetch; Reuters/Bloomberg behind paywall — sources will be marked `[verify]`]

## 5. Output preferences

- **Default memo length:** [quick note / standard memo / extended brief]
- **Analysis vs operational recommendation boundary:** [e.g. memo presents options + trade-offs; operational call belongs to MLRO / chief underwriter / deal committee]
- **Confidentiality / privilege markings:** [e.g. "Privileged & Confidential — Prepared at the request of counsel"]
- **Output format conventions:** [e.g. Risk Severity + Decision Relevance dual rating per the AGENTS.md dual-severity rule; explicit Iran-state / IRGC / Iran-private actor distinction in every relevant claim]

## 6. Standing assumptions and disclaimers

- **Standing assumptions:** [e.g. user has primary responsibility for sanctions and vessel screening against current OFAC list and IMO data at point of operational decision; skill output is not screening]
- **Standing disclaimers:** [e.g. all memos are draft for compliance / underwriting review; not legal, compliance, or maritime due-diligence advice]

---

## How to use this profile

1. The skill reads this file at the start of any memo request in this project.
2. The first six sections become the default `Decision / Audience / Geography / Time horizon / Evidence mode / Depth` block of every memo.
3. If a one-off question diverges from the profile, state the divergence in the memo header rather than overriding the profile silently.
4. To update the profile, ask the skill to re-run the cold-start interview, or edit this file directly.

## STOP rule

If any field above still reads `[PLACEHOLDER]` when a memo is requested in a workflow that expects a profile — **stop and run the cold-start interview before producing output**. Generic memos with unstated audience are worse than no memo.
