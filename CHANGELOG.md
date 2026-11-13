# Changelog

## Unreleased

- Added the second implemented MCP tool, `compare_entity_records`: a field-overlap
  list for two caller-supplied entity records (names, addresses, phones, emails,
  websites, directors, shareholders, signatories, registered agents, registration
  numbers). Each record needs a label and a source; values are normalised and
  compared for exact equality, cross-field matches are checked among person-type
  fields, and near matches by token overlap appear only if the caller supplies a
  threshold. Output carries per-field notes on why shared addresses and agents
  are weak, and states that a match is not a same-network, reconstitution or
  sanctions finding and that no match is not evidence of no link. It consults no
  list and holds no data; output is marked `result_is_not_a_finding` with
  `human_review_required`.
- Added the first implemented MCP tool, `estimate_chokepoint_bypass`: deterministic
  route comparison (for example a Hormuz or Bab el-Mandeb route against a bypass)
  over caller-supplied figures. Every figure enters as a low/high range with a
  required caller-stated source; source-less, blank-source, inverted, negative,
  zero-speed or currency-less input is rejected, never defaulted. The tool returns
  per-route days, fuel and cost (fuel, optional charter hire, war-risk premium on a
  caller-stated insured value and transit count, other cost lines), and, when a
  baseline is named, widest-pairing deltas with an overlap flag. It holds no
  tariff, premium, fuel-price, distance or chokepoint-status data, does not rank or
  recommend routes, and expresses no likelihood; output is marked
  `result_is_not_a_finding` with `human_review_required`. The three screening tools
  remain `not_implemented`. Package version bumped 0.2.0 -> 0.3.0.
- Re-checked four currency-watch topics against live primary sources on 2026-11-10 (OFAC Iran designations and General Licenses; Red Sea / Bab-el-Mandeb; Hormuz; dark-fleet / STS), updated their verification routing (JMIC and MSCIO advisories, OFAC Alerts), and dated them. All other topics are now explicitly marked `[unverified]`; the catalogue review date is unchanged. No incident details, designations, or numbers are recorded in the watch file.
- Added per-archetype falsification conditions ("what would make this memo wrong") and three observable indicators with named sources to `docs/risk-archetypes.md`. Pattern-level guidance only; no claims about specific entities, vessels, or jurisdictions.
- Added a GTTA composition rule to `SKILL.md` (aligned with the Central Asia & Caspian skill): GTTA owns memo structure and shared confidence labels, this skill owns regional mechanism and evidence rules. Added a pointer to GTTA's forecast log for dated probabilistic judgments. Reworded the README "why this exists" claim from improving reasoning quality to making reasoning checkable; no lift over a strong prompt is shown. Documentation-only; no mode, schema, eval, or benchmark change. This is not Bar 3 progress.
- Correct current UK source routing and preserve unverified topic status.
- Align evidence modes, calibration, and regional reference loading.
- Restore substantive documentation checks and harden specialist evaluation.

All notable changes to this repository are documented here.

## Unreleased

- Removed the mock streaming engine and all claims of autonomous enforcement,
  continuous graph traversal, persistent memory, or no-human-review operation.
- Replaced the enforcement-shaped JSON schema with a non-enforcing reviewer
  recommendation contract that always requires human review.
- Added a transport-independent MCP fallback contract and a standard-library CI
  test proving unavailable tools return `not_implemented` and never clearance.
- Corrected MCP docstrings and documented the graph and memory files as proposed
  data shapes rather than implemented services.
- Moved the complete runtime-neutral analytical contract into the root `SKILL.md` and reduced the Claude and Codex files to additive overlays.
- Replaced the packaged Claude symlink with a composition adapter whose name matches its directory. The validator now enforces the root/overlay split, package identity, attachment order, and plugin-manifest parity.
- Added a structural Claude/Codex runtime-loading smoke record. It covers instruction loading and bounded safety behavior only; it is not a factuality or model-quality benchmark.
- Removed unsupported production-stack and retainer wording from the public README. OpenClaw remains deliberately deferred.
- Fixed a dead link to the author's site: the contact section listed `for-analysts.html`, which has returned 404 since the site was restructured. It now links the live case-study page for this skill.
- Corrected the repository name casing in `evals/README.md` (`Agenda-Intelligence-md` -> `agenda-intelligence-md`); it resolved only through a GitHub redirect.
- Extended `scripts/check_markdown_links.py` to fail on 404/410 for links to the author's own site, which previously went unchecked because every `http(s)://` target was skipped. Network errors and other statuses are reported without failing; `SKIP_SITE_LINK_CHECK=1` skips the network step.

- Conformed the repo to the Agent Plugins 1.0.0 layout: added a root `plugin.json` with the `$schema` identifier from <https://agent-plugins.org>. `.claude-plugin/plugin.json` is unchanged and still serves the Claude Code install path; the specification ignores that directory. `skills/gulf-middle-east/SKILL.md` already matched the spec's discovery rule. The manifest validates against the published Draft 2020-12 schema.

- Added an Agenda Intelligence v1.3 evidence-packet handoff, a runnable synthetic regional packet, a dependency-free CI validator, and ADR 0001. Reclassified the older `analyze` / memo-validation composition as compatibility behavior.

- Renamed the runtime-overlay directory `skills/{claude,codex}/` to `runtimes/{claude,codex}/` and updated every path reference (README, AGENTS, CLAUDE, CONTRIBUTING, STATUS, evals, examples, validator, CI workflow). `skills/` is now reserved for Claude Code plugin packaging, because plugin installs auto-discover every `skills/*/SKILL.md` as a separate skill and the overlay layout produced junk-named skills (`claude`, `codex`).
- Packaged the repo as an installable Claude Code plugin: added `.claude-plugin/plugin.json` and `skills/gulf-middle-east/SKILL.md` (a symlink to the canonical root `SKILL.md`). Installable via `/plugin marketplace add vassiliylakhonin/agenda-intelligence-md`, then `/plugin install gulf-middle-east@agenda-intelligence`.

- Clarified the repo's commercial role: Gulf + Middle East remains a regional specialist reasoning layer, while Gulf maritime / trade-finance readiness is only a backup Agenda Intelligence MD hypothesis. Added README/AGENTS guidance to avoid new buyer-facing surfaces or deployed workers without buyer evidence.
- Added the unified portfolio stack-map table to `README.md` section 7, with the vertical-specialist row bolded for this repo.
- Added a "Project maturity" callout under section 7 pointing readers to [STATUS.md](STATUS.md) (Bar 1 / Bar 2 framework) and [AGENTS.md](AGENTS.md) "Definition of done".
- Added `CONTEXT.md` (regional vocabulary: Iran-actor distinctions, chokepoint scope, sovereign wealth deployment terms, evidence-mode boundary versus the product shell).
- Added `.github/ISSUE_TEMPLATE/{bug_report,feature_request}.md` and `.github/pull_request_template.md` so contributors have a structured entry point.
- Added this CHANGELOG.
- Cross-referenced the portfolio-wide skill packaging convention in `AGENTS.md` "Relationship to the broader stack".
