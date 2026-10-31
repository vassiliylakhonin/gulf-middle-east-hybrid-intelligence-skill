# Gulf & Middle East Intelligence Skill

A reusable regional reasoning skill for AI agents preparing decision memos on Gulf and Middle East exposure.

Use it when a general policy memo misses the region's mechanisms: Iran/GCC and Iraq exposure, correspondent banking, ownership, sovereign capital, energy flows, and shipping chokepoints such as the Hormuz, Bab el-Mandeb, and Red Sea routes.

This is a reasoning skill and a structured decision framework, not a live intelligence feed. The included experimental MCP server is a skeleton: every tool returns `not_implemented`. It does not retrieve live intelligence, screen counterparties, or issue clearances.

## Why this exists

Regional geopolitical and sanctions questions are often distorted by generic intelligence prompts. This skill gives an agent a tighter operating model for Gulf and Middle East analysis:

- region-specific mechanisms and risk archetypes
- explicit separation of facts, inference, assumptions, and source conflicts
- clear comparison of alternatives and escalation conditions
- evidence-aware output that can be checked by a deterministic verifier

It is designed to improve the quality of strategic reasoning, not to replace human judgment or legal review.

## What this project includes

- a reusable reasoning contract in [SKILL.md](SKILL.md)
- optional runtime overlays for [Claude](runtimes/claude/SKILL.md) and [Codex](runtimes/codex/SKILL.md)
- worked examples and source-backed patterns in [examples/README.md](examples/README.md)
- an evidence handoff to [Agenda Intelligence MD](https://github.com/vassiliylakhonin/agenda-intelligence-md) for deterministic checks
- regional structure and guardrails for strategic analysis tasks

## Choose a starting point

| Your task | Worked example | Evidence to inspect |
| --- | --- | --- |
| Maritime route disruption | [Open example](examples/hormuz-shipping-disruption.md) | Illustrative alternatives and assumptions |
| GCC correspondent banking | [Open example](examples/live-source-backed-gcc-correspondent-banking.md) | A dated source-backed example |
| Iraq banking source pack | [Open example](examples/user-provided-sources-iraq-banking.md) | Claims tied to supplied sources |

## Start with the skill

1. Load the canonical [SKILL.md](SKILL.md).
2. Add the matching runtime overlay: [Claude](runtimes/claude/SKILL.md) or [Codex](runtimes/codex/SKILL.md).
3. For a recurring practice, use the [cold-start interview](docs/cold-start-interview.md) to establish decision context and practice profile.
4. Give the agent a concrete decision brief.

Example prompt:

```text
Use Gulf & Middle East Intelligence Skill.
Question: What evidence would justify changing a shipping route?
Decision: proceed with a limited pilot, change the plan, or wait.
Audience: risk committee.
Geography: GCC, Iran, and the relevant maritime route.
Time horizon: next 90 days.
Evidence mode: reasoning-only; this is a hypothetical case.
Separate facts from assumptions, compare alternatives, and identify
missing evidence and escalation conditions.
```

For sourced analysis, choose `live-source-backed`, `user-provided sources`, or `illustrative source packet` explicitly. Supply the source packet or authorize collection. Preserve source dates and disclose unresolved source conflicts.

See [regional logic](docs/regional-logic.md), [source guide](docs/source-guide.md), and [analysis contract](docs/analysis-contract.md). The [currency watch](docs/currency-watch.md) is a supporting regional lens for financial exposure analysis.

## Place in the system

| Repository | Responsibility |
| --- | --- |
| [Global Think Tank Analyst](https://github.com/vassiliylakhonin/global-think-tank-analyst) | General decision-memo method and executable artifact toolkit |
| This skill | Regional mechanisms, sources, and uncertainty |
| [Central Asia & Caspian](https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill) | Complementary reasoning for exposure crossing the regional boundary |
| [Agenda Intelligence MD](https://github.com/vassiliylakhonin/agenda-intelligence-md) | Deterministic checks on supplied claim/source records |

The [companion patterns](docs/companion-patterns.md) explain how this skill is composed with related skills. Loading the skills alone does not invoke a verifier or authorize an external action. Evidence-packet checks assess declared support and consistency; they do not validate real-world facts on their own.

## Examples

Start with the [example guide](examples/README.md), then inspect a case that matches your evidence mode:

| Example | What to inspect |
| --- | --- |
| [Hormuz disruption](examples/hormuz-shipping-disruption.md) | Illustrative packet and shipping alternatives |
| [GCC banking](examples/live-source-backed-gcc-correspondent-banking.md) | Dated primary-source evidence |
| [Iraq banking packet](examples/user-provided-sources-iraq-banking.md) | Supplied sources and bounded conclusions |
| [Conflicting oil trackers](examples/source-conflict-iran-crude-export-trackers.md) | Unresolved disagreement in an illustrative packet |

The current set contains 9 flagship examples: 1 `reasoning-only`, 2 `illustrative source packet`, 3 `live-source-backed`, and 3 `user-provided sources`. 6 of 9 (67%) are source-anchored.

Source-backed examples are historical snapshots. Recheck current primary sources before reuse. Example counts describe coverage, not validated analytical performance.

## What this is not

This project does not:

- provide live regional intelligence feeds
- screen counterparties or sanctions exposure automatically
- certify legal, regulatory, or sanctions compliance
- authorize external action or payment decisions
- substitute for a human reviewer in operational decisions

The skill is a structured reasoning and evidence-handling layer. The actual decision remains with a human or an authorized process.

## Validation and limits

The repository records its artifact and structural evaluation work, while substantive regional reasoning lift remains unproven. The next [specialist-lift evaluation](evals/specialist-lift/README.md) tracks the relevant quality frontier.

There is no public, attributable real-use record. No production-usage, adoption, or benchmark numbers are claimed. [STATUS.md](STATUS.md) preserves the evaluation record and the limits of self-checking.

Human review is required before operational use. The skill does not provide legal advice, sanctions clearance, or payment enforcement. The [guardrails](docs/guardrails.md) define these boundaries and review expectations.

## Documentation and contribution

- [SKILL.md](SKILL.md): canonical instructions and reasoning contract
- [Evidence-packet handoff](docs/evidence-packet-handoff.md): the primary verification contract
- [Public signal examples](signals/README.md): [latest](signals/latest.md), [archive index](signals/index.json), and [JSON Feed](signals/feed.json)
- [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md): contribution workflow and repository constraints

Run the repository validator before submitting changes:

```bash
python3 scripts/validate.py
```

The skill package and examples remain the primary interface. The Python MCP skeleton is retained for development and does not deliver analytical findings.

## License

[MIT license](LICENSE).
