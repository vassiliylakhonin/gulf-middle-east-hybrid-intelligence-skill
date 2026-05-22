@AGENTS.md

# Claude Code working rules

AGENTS.md is the canonical project contract: identity, scope (incl. Iran-state / IRGC-affiliated / Iran-private commercial actor distinctions), evidence rules, retrieved-content trust, per-claim provenance tags (Axis A/B + table-cell discipline), currency triggers, linguistic faithfulness, three-value response logic (with explicit Stop-and-request triggers), README priorities, examples, and the Bar 1 / Bar 2 Definition of Done with honest current status. Follow it. Do not re-derive or restate those rules — apply them.

This file (CLAUDE.md) contains only Claude-Code-specific working rules for this repo, on top of the global `~/.claude/CLAUDE.md`.

## See also (project-specific anchors)

- [README.md](README.md) — public positioning per AGENTS.md "README priorities".
- [STATUS.md](STATUS.md) — current Bar 1 / Bar 2 status. Update truthfully; do not advance without verifiable evidence.
- [CONTRIBUTING.md](CONTRIBUTING.md) — local validator workflow and CI invariants enforced on `main`.
- [scripts/validate.py](scripts/validate.py) — authoritative structural and honesty checks.
- [docs/cold-start-interview.md](docs/cold-start-interview.md) + [templates/practice-profile.md](templates/practice-profile.md) — preflight for profile-expecting workflows.
- [docs/currency-watch.md](docs/currency-watch.md) — fast-moving topics that need re-verification.
- [docs/source-guide.md](docs/source-guide.md) — regional source tiers and freshness horizons.
- [evals/failure-modes.md](evals/failure-modes.md) — known canon-failure modes (incl. table-cell tag drift).
- Sibling vertical: [central-asia-caspian-hybrid-intelligence-skill](https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill) — reference when a flow crosses both regions; do not duplicate.

## Project-specific paths to inspect

In addition to the global pre-edit checklist:
- `skills/claude/SKILL.md` and `skills/codex/SKILL.md`
- examples/ (14-section flagship structure)
- docs/ (especially `source-guide.md`, `cold-start-interview.md`, `currency-watch.md`)
- evals/
- signals/ if present
- scripts/validate.py and scripts/render-readme.py
- templates/
- .github/workflows/validate.yml

## Validator before push

CI (`.github/workflows/validate.yml`) runs file-presence checks and the skill validator. Mirror locally:

```
python3 scripts/validate.py
```

The validator enforces hardcoded structural and honesty invariants (section counts, headings, safety gates, signals/examples consistency). If it fails locally, CI on `main` will fail too. Run it after any change to README, AGENTS, SKILL files, examples, evals, signals, or docs.

If the README is regenerated from a template, also run `python3 scripts/render-readme.py`.

## Working style in this repo

Small, reviewable changes. Do not rewrite the project unless I explicitly ask.

Do not add new infrastructure (MCP server, CLI, schemas, additional validators) — that belongs in Agenda Intelligence MD. See AGENTS.md "Relationship to the broader stack".

When updating STATUS.md or Bar 2 criteria in AGENTS.md, the rule from AGENTS.md "Definition of done" applies: do not pretend a bar is cleared if it is not, and do not advance status without verifiable evidence.

When working on Iran-related content, preserve the Iran-state / IRGC-affiliated / Iran-private commercial actor distinction — collapsing them is a Stop-and-request trigger per AGENTS.md.
