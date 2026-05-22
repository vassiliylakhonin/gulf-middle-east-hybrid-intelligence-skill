# Contributing

Contributions welcome. Before opening a PR, read [`AGENTS.md`](AGENTS.md) (project identity, scope, evidence and safety rules) and [`STATUS.md`](STATUS.md) (what's cleared, what isn't, what's deferred).

## Local environment

Requirements: Python 3.8+. No additional packages needed — the validator uses the standard library.

Run the validator from the repo root:

```bash
python3 scripts/validate.py
```

CI runs this on every push. Run it locally before opening a PR — a red CI on `main` is the only feedback you will get otherwise. Read [`scripts/validate.py`](scripts/validate.py) directly for the authoritative list of constraints.

## Development workflow

1. Create a branch from `main`.
2. Edit the relevant files: skill files under `skills/`, `AGENTS.md`, `llms.txt`, examples, signals.
3. Run `python3 scripts/validate.py` — all checks must pass.
4. Keep changes scoped and explain the decision value in the PR.
5. Open a PR with before/after where positioning or skill behavior changed.

## Required artifacts for a vertical specialist skill

This repo and its sibling [Central Asia + Caspian](https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill) follow the same minimum file set. Keep the topology aligned.

**Root files (required, file-presence checked by `scripts/validate.py`):**
- `README.md` — public positioning per AGENTS.md "README priorities"
- `AGENTS.md` — canonical project contract (identity, scope, evidence rules, Definition of Done)
- `CLAUDE.md` — Claude Code working rules (inherits AGENTS.md)
- `SKILL.md` — runtime skill contract
- `STATUS.md` — honest Bar 1 / Bar 2 status
- `CONTRIBUTING.md` — this file
- `LICENSE`
- `SECURITY.md`
- `llms.txt` — orientation for LLMs and agent indexers
- `.gitignore`

**Directories (required):**
- `skills/{claude,codex}/SKILL.md` — runtime variants per platform; OpenClaw deferred with a reason in STATUS.md (B2.4)
- `examples/` — flagship memos; every non-`README.md` file must declare an `Evidence mode:`
- `evals/` — must contain `checklist.md`, `failure-modes.md`, `starter-rubric.md`; `evals/agent-eval/` holds Bar 2 cases
- `docs/` — must contain `source-guide.md`, `regional-logic.md`, `risk-archetypes.md`
- `templates/` — at minimum `practice-profile.md`
- `scripts/` — at minimum `validate.py`
- `.github/workflows/validate.yml`

**Gulf-specific additions** (not present in CA-Caspian):
- `signals/` — public signal archive with `latest.md`, `index.json`, `feed.json`, `TEMPLATE.md` (atomic 4-file consistency enforced by validator)
- `taxonomy.json` — drives the auto-generated archetype block in README (run `scripts/render-readme.py` after edits)

`scripts/validate.py` is the authoritative list. Run it after any structural change.

## Where things live

- [`AGENTS.md`](AGENTS.md) — project identity, honesty, evidence, naming rules.
- [`SKILL.md`](SKILL.md) and [`skills/`](skills/) — runtime skill behavior for different runtimes.
- [`examples/`](examples/) — illustrative memos. Always state evidence mode.
- [`evals/`](evals/) — human review checklist, failure modes, starter rubric.
- [`signals/`](signals/) — public signal examples; contribute via [`signals/TEMPLATE.md`](signals/TEMPLATE.md).
- [`scripts/`](scripts/) — validator and readme renderer; see inline docstrings.

## Adding a signal

Signals require four files to be updated atomically in the same commit. CI enforces this — a partial update will fail.

1. Create `signals/<slug>.md` from [`signals/TEMPLATE.md`](signals/TEMPLATE.md).
2. Add an entry to `signals/index.json`.
3. Add an entry to `signals/feed.json`.
4. Replace `signals/latest.md` with the new signal.

`python3 scripts/validate.py` checks consistency across all four files.

## Adding an example

For each new or renamed example:

1. Declare evidence mode (`live-source-backed`, `user-provided sources`, `illustrative source packet`, `reasoning-only`). Do not fabricate citations, sanctions designations, vessel names, IMO numbers, prices, or dates.
2. Add a row to the main examples table in `README.md` (section "Flagship examples") in the same PR.
3. Update `examples/README.md` in the same PR.
4. If the example belongs to an existing archetype in `taxonomy.json`, add it there and regenerate the taxonomy section: `python3 scripts/render-readme.py`.
5. The README mode-count summary and `STATUS.md` source-anchored ratio must match the new actual count — update both if needed.

For `live-source-backed` and `user-provided sources` examples: include a `Retrieval date: YYYY-MM-DD`.

## Content rules

- Separate facts, assessments, assumptions, scenarios, and unknowns.
- Preserve evidence-mode labels and uncertainty language.
- Do not fabricate citations, dates, policy changes, sanctions details, incidents, or metrics.
- For docs: keep mechanism-first reasoning. Avoid generic Middle East commentary.
- For external reviews of examples or rubric applications: include your name/role and attribution. Anonymous reviews don't count toward Bar 2.

The full content contract lives in [AGENTS.md](AGENTS.md). [CLAUDE.md](CLAUDE.md) inherits from it for Claude Code sessions.

## Project boundaries

This repo is a domain skill, not an infrastructure product. Do not add or imply:

- MCP server functionality
- CLI tooling
- schemas or validators beyond `scripts/validate.py`
- runtime infrastructure
- live intelligence collection
- factuality verification guarantees
- legal, sanctions, investment, or security advice
- production-grade monitoring guarantees

Validation, schemas, scoring and audit tooling belong in [Agenda Intelligence MD](https://github.com/vassiliylakhonin/agenda-intelligence-md). Cross-region Central Asia / AML content belongs in [Central Asia + Caspian Hybrid Intelligence Skill](https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill).

## PR checklist

- [ ] `python3 scripts/validate.py` passes locally
- [ ] If a signal was added: all four signal files updated atomically (`signals/<slug>.md`, `index.json`, `feed.json`, `latest.md`)
- [ ] If an example was added or renamed: `README.md` flagship table, `examples/README.md`, and README mode-count summary updated in the same PR; `taxonomy.json` updated and `render-readme.py` run if archetype applies
- [ ] No claims of external verification, validation, MCP, CLI, or CI checks unless truly implemented in this repo
- [ ] No exaggerated language ("revolutionary", "production-grade", "guarantees correctness", "fully autonomous")
- [ ] Behavior or positioning change noted in commit message or PR description

## Contact

Author: Vassiliy Lakhonin · [vassiliylakhonin.github.io](https://vassiliylakhonin.github.io/)

For questions about positioning, the broader Agenda Intelligence portfolio, or potential review collaboration, open an issue or use the contact path on the portfolio site.
