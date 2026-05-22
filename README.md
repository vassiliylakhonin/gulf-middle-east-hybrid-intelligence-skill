# Gulf + Middle East Hybrid Intelligence Skill

> **GULF + MIDDLE EAST RISK REASONING SKILL** — a reasoning method for AI agents working on Iran sanctions, GCC financial and energy hubs, maritime chokepoint risk and regional geopolitical exposure. Open-source. No live data. No legal or compliance advice.

> **Regional specialist module for [Agenda Intelligence](https://github.com/vassiliylakhonin/agenda-intelligence-md).** Activated automatically when the `analyze` tool sees a Gulf / Middle East / chokepoint geography (Iran, UAE, Saudi Arabia, Qatar, Bahrain, Kuwait, Oman, Yemen, Iraq, Red Sea, Hormuz, Bab-el-Mandeb). Also usable standalone via paste/attach into any agent.

## 1. What this is

A reasoning method that runs inside an AI agent (Claude, ChatGPT, Codex, or a custom assistant) and produces mechanism-first, evidence-aware risk analysis on the Gulf and Middle East — instead of the generic "tensions remain elevated" commentary that default LLM output usually returns.

It does not replace sanctions screening, AML monitoring, vessel due diligence, legal review or human analyst judgement. It changes the *shape* of the reasoning your AI tool produces before any of those steps.

## 2. Who it is for

- sanctions compliance and AML teams at banks, fintechs and trade-finance providers with Iran adjacency or GCC correspondent exposure
- energy traders, refiners and commodity desks tracking OFAC SDN risk, dark-fleet patterns and OPEC+ dynamics
- shipping insurers and maritime risk teams covering Hormuz, Bab-el-Mandeb, Red Sea and Suez approaches
- sovereign wealth co-investors and corporate development teams assessing PIF / ADIA / Mubadala / QIA / KIA deployment risk
- analysts and researchers covering Iran, GCC states, Iraq and adjacent Levant exposure
- AI builders embedding regional risk reasoning into agents or assistants

## 3. What you get

- mechanism-first reasoning: primary driver → transmission channel → exposure map
- explicit Iran-state / IRGC-affiliated / Iran-private commercial actor distinctions where they matter
- explicit uncertainty labels: `Verified` / `Plausible` / `Judgment` / `Unknown`
- role-based actions and trigger points — not "tensions remain elevated"
- an explicit evidence mode and a limitation note on every output
- no fabricated citations, sanctions designations, vessel names, IMO numbers or dates

**Where this sits in the production AI stack**

Reasoning skills (markdown-first reasoning contracts for agents):
- [Global Think Tank Analyst](https://github.com/vassiliylakhonin/global-think-tank-analyst) — horizontal: policy, sanctions, regulatory, geopolitical, trade memos
- [Central Asia + Caspian Hybrid Intelligence Skill](https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill) — vertical: sanctions, AML, banking, corridor risk in Central Asia / Caspian
- **→ Gulf + Middle East Hybrid Intelligence Skill (this repo)** — vertical: Iran sanctions, GCC banking, sovereign wealth, maritime chokepoint risk

Evidence & audit layer (CI / MCP / schemas):
- [Agenda Intelligence MD](https://github.com/vassiliylakhonin/agenda-intelligence-md) — validate, score and audit strategic-risk agent output structure

The skills define how agents *reason*. Agenda Intelligence MD defines how the output is *audited*. Together they let agents produce auditable strategic-intelligence — not just plausible-sounding summaries.

## 4. Try this prompt

Paste this into an AI agent using the Claude or Codex skill file:

```text
Use the Gulf + Middle East Hybrid Intelligence Skill.

Question: A GCC-hub commodity trader is reviewing exposure to Iran-linked shipping, payment rails, and Gulf correspondent banks. What sanctions, AML, maritime and counterparty risks matter over the next 90 days?
Audience: sanctions compliance and trading-risk leadership.
Time horizon: 90 days.
Evidence mode: reasoning-only unless live source tools are available.
Mode: risk / compliance.

State the primary driver, mechanism, exposure map, actor incentives, role-based actions, trigger points, confidence, unknowns, and limitation note.
```

Expected shape of a good answer:
- starts with `Primary driver is: ...`;
- distinguishes Iran-state, IRGC-affiliated, and Iran-private commercial actors where material;
- explains how risk transmits through shipping, payment rails, correspondent banking, energy flows or sovereign wealth channels;
- labels uncertainty using `Verified` / `Plausible` / `Judgment` / `Unknown` where useful;
- gives trigger points and role-based actions, not vague "monitor closely" advice;
- includes a limitation note and avoids legal, compliance, sanctions, AML or investment determinations.

## 5. What it does

This skill helps agents produce mechanism-first, evidence-aware, decision-useful regional risk analysis for the Gulf and Middle East. It:

- frames regional questions as concrete risk or strategy problems
- explains mechanisms before implications
- separates `Verified` / `Plausible` / `Judgment` / `Unknown`
- maps risk transmission channels across Iran sanctions, GCC banking, sovereign wealth, energy markets and maritime routes
- distinguishes Iran-state, IRGC-affiliated, and Iran-private commercial actors where it matters
- supports sanctions adjacency, dark-fleet and ship-to-ship transfer, correspondent banking, sovereign wealth, energy market and shipping route analysis
- identifies leverage shifts and actor incentives across GCC states, Iran, US, EU and Asian buyers
- produces trigger points and watch-next indicators
- supports role-based implications for sanctions compliance, AML, energy traders, shipping insurers, Gulf bank correspondents, sovereign wealth co-investors and policy analysts
- runs a cold-start interview ([`docs/cold-start-interview.md`](docs/cold-start-interview.md)) to capture role, geography, decision context, risk appetite, source access and required actor distinctions (Iran-state / IRGC / Iran-private commercial) into a populated practice profile ([`templates/practice-profile.md`](templates/practice-profile.md)) before substantive memos
- carries an active currency watch ([`docs/currency-watch.md`](docs/currency-watch.md)) listing fast-moving topics — Iran SDN evolution, IRGC scope, US-Iran negotiation file, Houthi / Bab-el-Mandeb posture, Hormuz, dark-fleet, GCC correspondent banking, Iraq CBI, MENAFATF, OPEC+ — that source-backed memos should re-verify against current primary sources, with a 90-day staleness rule

## 6. What it is not

- not legal advice
- not compliance advice
- not sanctions screening
- not AML transaction monitoring
- not vessel screening or maritime due diligence
- not factuality verification by itself
- not a live source retriever
- not a risk database
- not an agent framework
- not a CLI, MCP server, or validation platform
- not a replacement for human analyst, counsel, or compliance review

## 7. Relationship to Agenda Intelligence MD, Global Think Tank Analyst and Central Asia + Caspian Skill

This skill is one of four repos in a wider portfolio. Each has a distinct role; do not blur them.

| Layer | Repo | Role |
|---|---|---|
| Product shell | [agenda-intelligence-md](https://github.com/vassiliylakhonin/agenda-intelligence-md) | MCP server, request/memo schemas, geography routing, evidence audit, scoring |
| Reasoning method | [global-think-tank-analyst](https://github.com/vassiliylakhonin/global-think-tank-analyst) | Strategic-risk reasoning contract; loaded by `analyze` as the default method |
| Vertical specialist | [central-asia-caspian-hybrid-intelligence-skill](https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill) | Central Asia / Caspian / Middle Corridor domain depth; routed by geography |
| **Vertical specialist** (this repo) | **gulf-middle-east-hybrid-intelligence-skill** | Iran / GCC / maritime chokepoint domain depth; routed by geography |

> **Project maturity.** This repo uses a two-bar Definition of Done (Bar 1 — early but credible; Bar 2 — agent-validated specialist resource). Current honest status, per criterion, lives in [STATUS.md](STATUS.md). Criteria are defined in [AGENTS.md](AGENTS.md) under "Definition of done".

- **Gulf + Middle East Hybrid Intelligence Skill** *(this repo)* — specialist Gulf, Iran, Iraq and maritime-chokepoint risk reasoning; Iran sanctions, GCC banking, sovereign wealth, energy market and shipping route analysis patterns.
- **Central Asia + Caspian Hybrid Intelligence Skill** — Central Asia / Caspian regional specialist; reference it when a flow crosses both regions (e.g., Iran-Caspian routes, Iraq-Kurdistan corridors, Russia-Iran-China tri-junction): https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill
- **Global Think Tank Analyst** — broader strategic-risk memo workflow, general policy-risk analysis, scenario and red-team memo modes: https://github.com/vassiliylakhonin/global-think-tank-analyst
- **Agenda Intelligence MD** — schemas, validation, evidence audit, scoring, CLI / MCP / CI tooling where implemented: https://github.com/vassiliylakhonin/agenda-intelligence-md

> Use this repo for specialist Gulf + Middle East reasoning. Use Global Think Tank Analyst for broader strategic-risk memo workflows. Use Agenda Intelligence MD to validate, score or audit outputs where that functionality is implemented.

This repo does **not** itself perform Agenda Intelligence MD validation, schema enforcement on outputs, or live source retrieval.

For the full portfolio architecture, see [PORTFOLIO.md in Global Think Tank Analyst](https://github.com/vassiliylakhonin/global-think-tank-analyst/blob/main/PORTFOLIO.md). [docs/companion-patterns.md](docs/companion-patterns.md) describes structural patterns for using this skill alongside the other repos.

## 8. Quick usage

Use the skill variant matching your environment as the operating instruction in your agent setup:

| Environment | File | Notes |
|---|---|---|
| Claude | `skills/claude/SKILL.md` | Claude Projects setup, web search guidance, extended-context user-provided source workflows |
| Codex | `skills/codex/SKILL.md` | Agentic-loop output discipline, JSON output mode, Agenda Intelligence MD pipeline pattern |
| ChatGPT / other LLMs | `skills/claude/SKILL.md` or `skills/codex/SKILL.md` | Paste or attach as system / project instruction |

Validation:

```bash
python3 scripts/validate.py
```

The validator checks skill structure, evidence-mode declarations, retrieval-date discipline, limitation notes, forbidden determinative claims, signal structure, eval files, and source-guide freshness rules. It does **not** verify factuality of any output produced by the skill.

## 9. Before / after

**Before — generic LLM answer:**
- broad regional commentary ("tensions remain elevated")
- undifferentiated treatment of Iran-state / IRGC / Iran-private actors
- vague "monitor sanctions"
- no transmission mechanism
- no role-based implications
- no trigger points

**After — skill-style answer:**
- primary driver
- mechanism (how the risk transmits through banking, shipping, energy, sovereign wealth)
- exposure map (where it concentrates: corridor, sector, counterparty class)
- actor incentives and leverage (GCC states, Iran, US, EU, Asian buyers)
- uncertainty labels (`Verified` / `Plausible` / `Judgment` / `Unknown`)
- trigger points and watch-next indicators
- role-based implications (sanctions compliance, AML, energy trader, shipping insurer, banker, sovereign wealth co-investor)
- evidence mode stated explicitly

## 10. Flagship examples

For a guided route through the examples, start with [examples/README.md](examples/README.md).

| File | Mode | Topic |
|---|---|---|
| [examples/live-source-backed-ofac-iran-shipping-sanctions.md](examples/live-source-backed-ofac-iran-shipping-sanctions.md) | `live-source-backed` | OFAC Iran shipping-sector sanctions — GCC-hub commodity trader exposure |
| [examples/live-source-backed-gcc-correspondent-banking.md](examples/live-source-backed-gcc-correspondent-banking.md) | `live-source-backed` | GCC correspondent banking — Western respondent bank exposure |
| [examples/live-source-backed-bab-el-mandeb-red-sea-shipping.md](examples/live-source-backed-bab-el-mandeb-red-sea-shipping.md) | `live-source-backed` | Bab-el-Mandeb / Red Sea shipping disruption — war-risk underwriter or industrial charterer exposure (CMF and IMO retrieved 2026-05-15; UKMTO and Lloyd's JWC `[verify]`) |
| [examples/user-provided-sources-sovereign-wealth-deployment.md](examples/user-provided-sources-sovereign-wealth-deployment.md) | `user-provided sources` | Sovereign wealth deployment risk for a target company or co-investor |
| [examples/iran-sanctions-routing-exposure.md](examples/iran-sanctions-routing-exposure.md) | `reasoning-only` | Iran sanctions adjacency for a European refiner sourcing Gulf crude |
| [examples/hormuz-shipping-disruption.md](examples/hormuz-shipping-disruption.md) | `illustrative source packet` | Hormuz disruption exposure for a shipping insurer |
| [examples/user-provided-sources-iraq-banking.md](examples/user-provided-sources-iraq-banking.md) | `user-provided sources` | Iraq banking-sector reform exposure for a correspondent bank (template) |
| [examples/user-provided-sources-dark-fleet-sanctioned-oil.md](examples/user-provided-sources-dark-fleet-sanctioned-oil.md) | `user-provided sources` | Dark-fleet / sanctioned-oil flow exposure for a refiner or trader — skeleton packet (OFAC, EU, UK OFSI, Swiss SECO, IMO, IGP&I, FATF/MENAFATF) + structural framing of three deceptive-practice patterns and six transmission channels; Iran actor distinction applied |
| [examples/source-conflict-iran-crude-export-trackers.md](examples/source-conflict-iran-crude-export-trackers.md) | `illustrative source packet` | Iranian crude export tracker divergence — source-conflict surfacing rule applied to dark-fleet / STS exposure sizing |

<!-- TAXONOMY:START -->

### Examples by archetype

_Generated from `taxonomy.json`. To update, edit `taxonomy.json` and run `python3 scripts/render-readme.py`._

**Iran sanctions adjacency**
- [`examples/iran-sanctions-routing-exposure.md`](examples/iran-sanctions-routing-exposure.md) — `reasoning-only`
- [`examples/live-source-backed-gcc-correspondent-banking.md`](examples/live-source-backed-gcc-correspondent-banking.md) — `live-source-backed`
- [`examples/live-source-backed-ofac-iran-shipping-sanctions.md`](examples/live-source-backed-ofac-iran-shipping-sanctions.md) — `live-source-backed`
- [`examples/user-provided-sources-iraq-banking.md`](examples/user-provided-sources-iraq-banking.md) — `user-provided-sources`

**Dark-fleet and ship-to-ship transfers**
- [`examples/iran-sanctions-routing-exposure.md`](examples/iran-sanctions-routing-exposure.md) — `reasoning-only`
- [`examples/live-source-backed-ofac-iran-shipping-sanctions.md`](examples/live-source-backed-ofac-iran-shipping-sanctions.md) — `live-source-backed`
- [`examples/user-provided-sources-dark-fleet-sanctioned-oil.md`](examples/user-provided-sources-dark-fleet-sanctioned-oil.md) — `user-provided-sources`

**GCC correspondent banking exposure**
- [`examples/live-source-backed-gcc-correspondent-banking.md`](examples/live-source-backed-gcc-correspondent-banking.md) — `live-source-backed`

**Sovereign wealth deployment risk**
- [`examples/user-provided-sources-sovereign-wealth-deployment.md`](examples/user-provided-sources-sovereign-wealth-deployment.md) — `user-provided-sources`

**Maritime chokepoint disruption**
- [`examples/hormuz-shipping-disruption.md`](examples/hormuz-shipping-disruption.md) — `illustrative-source-packet`
- [`examples/live-source-backed-bab-el-mandeb-red-sea-shipping.md`](examples/live-source-backed-bab-el-mandeb-red-sea-shipping.md) — `live-source-backed`

**Sanctioned-oil flow concentration**
- [`examples/iran-sanctions-routing-exposure.md`](examples/iran-sanctions-routing-exposure.md) — `reasoning-only`
- [`examples/live-source-backed-ofac-iran-shipping-sanctions.md`](examples/live-source-backed-ofac-iran-shipping-sanctions.md) — `live-source-backed`
- [`examples/user-provided-sources-dark-fleet-sanctioned-oil.md`](examples/user-provided-sources-dark-fleet-sanctioned-oil.md) — `user-provided-sources`

**Sanctioned-party post-designation reconstitution**
- [`examples/iran-sanctions-routing-exposure.md`](examples/iran-sanctions-routing-exposure.md) — `reasoning-only`

<!-- TAXONOMY:END -->

## 11. Signal archive

[`signals/`](signals/) holds short public examples of the skill style: one regional event or structural condition, why it matters, a bounded assessment, and indicators to watch.

- [`signals/latest.md`](signals/latest.md) — single-file pointer to the latest signal
- [`signals/index.json`](signals/index.json) — machine-readable signal index
- [`signals/feed.json`](signals/feed.json) — JSON Feed for ingestion
- [`signals/TEMPLATE.md`](signals/TEMPLATE.md) — template for contributing a signal

These are public examples of skill output, not official intelligence or real-time data.

## Repository layout

```text
.
├── README.md            # Public positioning (this file)
├── AGENTS.md            # Canonical project contract (identity, scope, evidence rules)
├── CLAUDE.md            # Claude Code working rules (inherits AGENTS.md)
├── SKILL.md             # Runtime skill contract
├── STATUS.md            # Honest Bar 1 / Bar 2 status against the Definition of Done
├── CONTRIBUTING.md      # Local validator workflow and CI invariants
├── llms.txt             # Orientation for LLMs and agent indexers
├── taxonomy.json        # Example archetypes (drives an auto-generated README block)
├── skills/              # Runtime skill files per platform (claude/, codex/)
├── examples/            # Flagship memo examples (state evidence mode)
├── evals/               # Review checklist, failure modes, starter rubric, agent-eval cases
├── signals/             # Public signal archive + JSON Feed + template
├── docs/                # Source guide, currency watch, cold-start interview, regional logic
├── templates/           # Practice-profile template populated by the cold-start interview
├── scripts/             # Validator (validate.py) and README renderer (render-readme.py)
└── .github/             # CI workflows and issue templates
```

## Contributing

New contributors: [`CONTRIBUTING.md`](CONTRIBUTING.md) opens with a "First 15 minutes" onboarding path — read the three load-bearing files (`README.md`, `AGENTS.md`, `STATUS.md`), run `python3 scripts/validate.py` locally (and `python3 scripts/render-readme.py --check` if `taxonomy.json` changes), and walk one concrete `live-source-backed` flagship example end-to-end. CI runs the validator on every push; run it locally before opening a PR.

Cross-repo terminology — evidence modes, Verified/Plausible/Judgment/Unknown labels, Axis A/B provenance tags (incl. table-cell discipline), three-value response logic (incl. the Iran actor-distinction Stop-and-request trigger), and the deliberate maturity-framework asymmetry across the four-repo stack (this repo and the CA-Caspian sibling use Bar 1/2; `global-think-tank-analyst` uses `VALIDATION_PLAN.md`; `agenda-intelligence-md` uses `ROADMAP.md` version targets) — is consolidated in the portfolio glossary at [`agenda-intelligence-md/docs/glossary.md`](https://github.com/vassiliylakhonin/agenda-intelligence-md/blob/main/docs/glossary.md).

## 12. Skill files

- [`skills/claude/SKILL.md`](skills/claude/SKILL.md) — Claude variant with Projects setup, web search guidance for `live-source-backed` mode, extended-context `user-provided sources` workflows and tool-use discipline.
- [`skills/codex/SKILL.md`](skills/codex/SKILL.md) — Codex variant with agentic-loop output discipline, JSON output mode for Agenda Intelligence MD, and a multi-step pipeline integration pattern.
- [`docs/cold-start-interview.md`](docs/cold-start-interview.md) — preflight procedure that captures role, geography, decision context, risk appetite, source access, and required Iran-state / IRGC / Iran-private actor distinctions before substantive memo work. STOP rule blocks generic memos when the practice profile is missing or contains `[PLACEHOLDER]` markers.
- [`templates/practice-profile.md`](templates/practice-profile.md) — populated profile read by every memo in the session as the default `Decision / Audience / Geography / Time horizon` block.
- [`docs/currency-watch.md`](docs/currency-watch.md) — active list of fast-moving topics that source-backed memos should re-verify against current primary sources. 90-day staleness rule.
- OpenClaw is intentionally not provided yet. See `STATUS.md` for B2.4 reasoning.

## 13. Source guide

[`docs/source-guide.md`](docs/source-guide.md) lists primary and authoritative sources for Gulf + Middle East risk analysis: OFAC, BIS, EU Council, UK OFSI, MENAFATF, IEA, IMF, BIS banking statistics, central banks (SAMA, CBUAE, QCB, CBI Iran, CBI Iraq, CBL Lebanon), IMO, and tiered secondary sources (think tanks, energy and shipping reporters).

## 14. Risk archetypes

[`docs/risk-archetypes.md`](docs/risk-archetypes.md) catalogues recurring risk patterns: Iran sanctions adjacency, dark-fleet and ship-to-ship transfers, GCC correspondent-banking exposure, sovereign wealth deployment risk, maritime chokepoint disruption, sanctioned-oil flows, sanctioned-party post-designation reconstitution.

Patterns, not factual claims about any specific entity, vessel or jurisdiction. Operational use requires source-backed verification.

## 15. Review checklist

[`evals/checklist.md`](evals/checklist.md) — yes/no review pass over any memo produced with the skill. Aid for human reviewers, not an automated validator.

[`evals/failure-modes.md`](evals/failure-modes.md) — common ways Gulf / Middle East memos go wrong, with diagnostic cues.

[`evals/starter-rubric.md`](evals/starter-rubric.md) — starter scoring rubric for human review. Not a benchmark.

## 16. Limitations

- This project is intentionally conservative about evidence. It does not fabricate sources, vessel names, IMO numbers, or sanctions designations.
- It is a **decision-support skill**, not legal, compliance, sanctions, AML, or investment advice.
- It does not screen vessels, transactions, or counterparties. Operational sanctions or AML decisions require dedicated screening tools, primary OFAC/EU/UK list checks, and qualified compliance review.
- It does not retrieve sources, run validators, or expose an MCP server. For those, use [Agenda Intelligence MD](https://github.com/vassiliylakhonin/agenda-intelligence-md).
- This is an initial release. The honest status is in [`STATUS.md`](STATUS.md).
- No production usage record exists yet (see B2.5).

### What this skill has not been tested on

Stated honestly so readers can calibrate. These are gaps in observed evidence, not claims of weakness:

- **No labeled accuracy dataset.** Adversarial cases in [`evals/adversarial/`](evals/adversarial/) are author-designed traps, not a held-out test set. Pass/fail is judged manually against per-case criteria.
- **No multi-agent or long-horizon trials.** Behavior has been exercised in single-turn and short-multi-turn memo production; long autonomous research loops have not been measured.
- **No cross-model regression tracking.** Behavior has been observed primarily on Claude. The Codex variant exists but has not been systematically compared head-to-head against the same prompts; OpenClaw variant is deferred.
- **No live-source automation.** `live-source-backed` examples were produced with manual source retrieval. There is no integrated retrieval layer here; recency cannot be enforced automatically.
- **Limited non-English source coverage.** Arabic- and Farsi-language regulatory, central-bank, and state-media sources have not been systematically tested as inputs.
- **No real vessel-tracking or AIS data integration.** Maritime examples reason about patterns; they do not consume AIS feeds or vessel-ownership databases.

## 17. Roadmap

Directional, not committed. Items here are not implemented unless noted.

- **Signal archive:** initial Red Sea, OPEC+ and US-Iran diplomatic signals are live in [`signals/`](signals/).
- **Validation script (B1.5):** implemented as [`scripts/validate.py`](scripts/validate.py) and should pass before changes are merged.
- **Dark-fleet / sanctioned-oil flow example:** delivered 2026-05-15 as a `user-provided sources` skeleton packet ([`examples/user-provided-sources-dark-fleet-sanctioned-oil.md`](examples/user-provided-sources-dark-fleet-sanctioned-oil.md)). Upgrade to `live-source-backed` is still deferred pending AIS primary access (Kpler, TankerTrackers, or Windward).
- **OpenClaw skill variant:** deferred until there is an active OpenClaw use case; avoid creating a near-identical third wrapper.
- **Agent-eval delta (B2.2):** ✅ closed 2026-05-21. Three cases committed across distinct Gulf sub-domains: [`evals/agent-eval/2026-05-20-hormuz-shipping-insurer.md`](evals/agent-eval/2026-05-20-hormuz-shipping-insurer.md) (chokepoint underwriting, delta +6), [`evals/agent-eval/2026-05-21-dark-fleet-sanctioned-oil-mixed.md`](evals/agent-eval/2026-05-21-dark-fleet-sanctioned-oil-mixed.md) (refiner / dark-fleet / sanctioned-oil adjacency with `mixed` evidence-mode mapping, delta +6), [`evals/agent-eval/2026-05-21-gcc-correspondent-tiering.md`](evals/agent-eval/2026-05-21-gcc-correspondent-tiering.md) (Western respondent bank GCC correspondent tiering, delta +5.5). Self-scored structural deltas; not factual verification, not model-quality comparison, not aggregate benchmark.
- **Evidence-mode mapping (B2.3):** ✅ closed 2026-05-21. The dark-fleet / sanctioned-oil case maps upstream `live-source-backed` regulatory framework plus `user-provided sources` skeleton packet through Agenda Intelligence `analyze` as `mixed`, not `live_source_backed`.
- **Real-use evidence (B2.5):** still met via negative disclosure only — no public, attributable real-use record yet. One published practitioner use case would shift the portfolio from "credible artifact" to "validated in the field." Reach-outs welcome via the contact route below.
- **Practitioner review (B2.8, optional):** open to reviewers from sanctions compliance, energy trading, shipping insurance, Gulf banking, or Iran-watcher analyst backgrounds. Not a hard Bar 2 gate for agent-first validation — it is a trust layer for the practitioner audience.

If you'd like to influence the roadmap or contribute a review, open an issue.

## 18. Contact

Author: **Vassiliy Lakhonin** — Almaty, Kazakhstan (UTC+5).

- Portfolio: [vassiliylakhonin.github.io](https://vassiliylakhonin.github.io/)
- Analyst entry route: [vassiliylakhonin.github.io/for-analysts.html](https://vassiliylakhonin.github.io/for-analysts.html)
- Email: [vassiliy.lakhonin@gmail.com](mailto:vassiliy.lakhonin@gmail.com)
- LinkedIn: [linkedin.com/in/vassiliy-lakhonin](https://www.linkedin.com/in/vassiliy-lakhonin/)
- GitHub: [github.com/vassiliylakhonin](https://github.com/vassiliylakhonin)
- Issues and PRs on this repo are welcome.

For Bar 2 external-review collaboration (see [`STATUS.md`](STATUS.md) — sanctions compliance, energy trading, shipping insurance, Gulf banking, or Iran-watcher backgrounds), please open an issue or email with your background. For bespoke analysis under retainer: same channel, include decision context, geography and time horizon.

## Disclaimer

This repository is for informational and educational purposes only. It does not constitute investment, financial, legal, compliance, sanctions screening, or trading advice. It does not verify factual truth, predict outcomes, or replace professional judgment. Use at your own risk.

## License

MIT — see [LICENSE](LICENSE).
