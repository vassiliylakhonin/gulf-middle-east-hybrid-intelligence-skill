# Gulf + Middle East Hybrid Intelligence Skill

## 1. Positioning

**Gulf & Middle East specialist skill for AI agents working on Iran sanctions, GCC financial and energy hubs, maritime chokepoint risk, and regional geopolitical exposure.**

## 2. Problem

Generic LLMs produce broad commentary on the Gulf and Middle East: vague "tensions remain elevated", undifferentiated treatment of Iran-state versus IRGC-affiliated versus Iran-private commercial actors, no transmission mechanism, no exposure mapping, no actor-incentive analysis, no trigger points.

That output is not decision-useful for sanctions and AML teams, energy traders, shipping insurers, Gulf banking correspondents, sovereign wealth co-investors, or analysts with operational exposure to Iran sanctions, OFAC SDN risk, Hormuz / Bab-el-Mandeb chokepoints, or GCC financial flows. They need mechanism-first reasoning, explicit evidence boundaries, and role-based implications — not regional essays.

## 3. Try this prompt

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

## 4. What it does

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

## 5. What it is not

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

## 6. Relationship to Agenda Intelligence MD, Global Think Tank Analyst and Central Asia + Caspian Skill

This skill is one of several repos in a wider portfolio. Each has a distinct role; do not blur them.

- **Gulf + Middle East Hybrid Intelligence Skill** *(this repo)* — specialist Gulf, Iran, Iraq and maritime-chokepoint risk reasoning; Iran sanctions, GCC banking, sovereign wealth, energy market and shipping route analysis patterns.
- **Central Asia + Caspian Hybrid Intelligence Skill** — Central Asia / Caspian regional specialist; reference it when a flow crosses both regions (e.g., Iran-Caspian routes, Iraq-Kurdistan corridors, Russia-Iran-China tri-junction): https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill
- **Global Think Tank Analyst** — broader strategic-risk memo workflow, general policy-risk analysis, scenario and red-team memo modes: https://github.com/vassiliylakhonin/global-think-tank-analyst
- **Agenda Intelligence MD** — schemas, validation, evidence audit, scoring, CLI / MCP / CI tooling where implemented: https://github.com/vassiliylakhonin/Agenda-Intelligence-md

> Use this repo for specialist Gulf + Middle East reasoning. Use Global Think Tank Analyst for broader strategic-risk memo workflows. Use Agenda Intelligence MD to validate, score or audit outputs where that functionality is implemented.

This repo does **not** itself perform Agenda Intelligence MD validation, schema enforcement on outputs, or live source retrieval.

[docs/companion-patterns.md](docs/companion-patterns.md) describes structural patterns for using this skill alongside the other repos.

## 7. Quick usage

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

## 8. Before / after

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

## 9. Flagship examples

For a guided route through the examples, start with [examples/README.md](examples/README.md).

| File | Mode | Topic |
|---|---|---|
| [examples/live-source-backed-ofac-iran-shipping-sanctions.md](examples/live-source-backed-ofac-iran-shipping-sanctions.md) | `live-source-backed` | OFAC Iran shipping-sector sanctions — GCC-hub commodity trader exposure |
| [examples/live-source-backed-gcc-correspondent-banking.md](examples/live-source-backed-gcc-correspondent-banking.md) | `live-source-backed` | GCC correspondent banking — Western respondent bank exposure |
| [examples/user-provided-sources-sovereign-wealth-deployment.md](examples/user-provided-sources-sovereign-wealth-deployment.md) | `user-provided sources` | Sovereign wealth deployment risk for a target company or co-investor |
| [examples/iran-sanctions-routing-exposure.md](examples/iran-sanctions-routing-exposure.md) | `reasoning-only` | Iran sanctions adjacency for a European refiner sourcing Gulf crude |
| [examples/hormuz-shipping-disruption.md](examples/hormuz-shipping-disruption.md) | `illustrative source packet` | Hormuz disruption exposure for a shipping insurer |
| [examples/user-provided-sources-iraq-banking.md](examples/user-provided-sources-iraq-banking.md) | `user-provided sources` | Iraq banking-sector reform exposure for a correspondent bank (template) |
| Dark-fleet / sanctioned-oil flow | — | Deferred (requires live AIS primary sources) — see [examples/README.md](examples/README.md) |

## 10. Signal archive

[`signals/`](signals/) holds short public examples of the skill style: one regional event or structural condition, why it matters, a bounded assessment, and indicators to watch.

- [`signals/latest.md`](signals/latest.md) — single-file pointer to the latest signal
- [`signals/index.json`](signals/index.json) — machine-readable signal index
- [`signals/feed.json`](signals/feed.json) — JSON Feed for ingestion
- [`signals/TEMPLATE.md`](signals/TEMPLATE.md) — template for contributing a signal

These are public examples of skill output, not official intelligence or real-time data.

## 11. Skill files

- [`skills/claude/SKILL.md`](skills/claude/SKILL.md) — Claude variant with Projects setup, web search guidance for `live-source-backed` mode, extended-context `user-provided sources` workflows and tool-use discipline.
- [`skills/codex/SKILL.md`](skills/codex/SKILL.md) — Codex variant with agentic-loop output discipline, JSON output mode for Agenda Intelligence MD, and a multi-step pipeline integration pattern.
- OpenClaw is intentionally not provided yet. See `STATUS.md` for B2.4 reasoning.

## 12. Source guide

[`docs/source-guide.md`](docs/source-guide.md) lists primary and authoritative sources for Gulf + Middle East risk analysis: OFAC, BIS, EU Council, UK OFSI, MENAFATF, IEA, IMF, BIS banking statistics, central banks (SAMA, CBUAE, QCB, CBI Iran, CBI Iraq, CBL Lebanon), IMO, and tiered secondary sources (think tanks, energy and shipping reporters).

## 13. Risk archetypes

[`docs/risk-archetypes.md`](docs/risk-archetypes.md) catalogues recurring risk patterns: Iran sanctions adjacency, dark-fleet and ship-to-ship transfers, GCC correspondent-banking exposure, sovereign wealth deployment risk, maritime chokepoint disruption, sanctioned-oil flows, sanctioned-party post-designation reconstitution.

Patterns, not factual claims about any specific entity, vessel or jurisdiction. Operational use requires source-backed verification.

## 14. Review checklist

[`evals/checklist.md`](evals/checklist.md) — yes/no review pass over any memo produced with the skill. Aid for human reviewers, not an automated validator.

[`evals/failure-modes.md`](evals/failure-modes.md) — common ways Gulf / Middle East memos go wrong, with diagnostic cues.

[`evals/starter-rubric.md`](evals/starter-rubric.md) — starter scoring rubric for human review. Not a benchmark.

## 15. Limitations

- This project is intentionally conservative about evidence. It does not fabricate sources, vessel names, IMO numbers, or sanctions designations.
- It is a **decision-support skill**, not legal, compliance, sanctions, AML, or investment advice.
- It does not screen vessels, transactions, or counterparties. Operational sanctions or AML decisions require dedicated screening tools, primary OFAC/EU/UK list checks, and qualified compliance review.
- It does not retrieve sources, run validators, or expose an MCP server. For those, use [Agenda Intelligence MD](https://github.com/vassiliylakhonin/Agenda-Intelligence-md).
- This is an initial release. The honest status is in [`STATUS.md`](STATUS.md).
- No production usage record exists yet (see B2.5).

## 16. Roadmap

Directional, not committed. Items here are not implemented unless noted.

- **Signal archive:** initial Red Sea, OPEC+ and US-Iran diplomatic signals are live in [`signals/`](signals/).
- **Validation script (B1.5):** implemented as [`scripts/validate.py`](scripts/validate.py) and should pass before changes are merged.
- **Dark-fleet / sanctioned-oil flow example:** deferred pending live AIS primary sources from Kpler, TankerTrackers, or Windward.
- **OpenClaw skill variant:** deferred until there is an active OpenClaw use case; avoid creating a near-identical third wrapper.
- **External review (B2.2, B2.3, B2.7):** open to external reviewers from sanctions compliance, energy trading, shipping insurance, Gulf banking, or Iran-watcher analyst backgrounds. These criteria require humans outside the author's circle.

If you'd like to influence the roadmap or contribute a review, open an issue.

## License

MIT — see [LICENSE](LICENSE).
