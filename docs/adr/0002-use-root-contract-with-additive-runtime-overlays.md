# Use one root contract with additive runtime overlays

Status: accepted, 2026-08-24

## Context

The root `SKILL.md` was a short selector, while the Claude and Codex files each copied a full analytical contract. The copies had already diverged: Claude carried regional logic, mode selection, recommendation rules, and definition-of-success sections that Codex did not; Codex carried JSON and agent-loop sections that Claude did not.

The packaged file at `skills/gulf-middle-east/SKILL.md` was a symlink to the selector. A Claude Code 2.1.233 smoke test therefore loaded only the selector, not `runtimes/claude/SKILL.md`. The bare `/gulf-middle-east` command returned `Unknown command`; only the namespaced command resolved. The Agent Skills reference validator also rejected the package because the directory `gulf-middle-east` did not match the root frontmatter name `gulf-middle-east-hybrid-intelligence`.

Claude Code plugin skills can use `${CLAUDE_PLUGIN_ROOT}` to reference resources elsewhere in a plugin. The command-name and substitution behavior is documented in the [official Claude Code skills documentation](https://code.claude.com/docs/en/skills).

## Decision

The root `SKILL.md` is the complete runtime-neutral analytical contract and the only copy of common behavior.

Runtime files are additive:

- Claude adds conditional retrieval, document-use, confidence-ceiling, and stale-risk rules.
- Codex adds agent-loop, evidence-packet JSON, file-output, and validation-chaining rules.
- OpenClaw remains deferred because there is no active use case. Other runtimes can use the complete root contract without an overlay.

`skills/gulf-middle-east/SKILL.md` is a regular Claude Code composition adapter. Its package name matches its directory. It attaches exactly two files in this order:

1. `${CLAUDE_PLUGIN_ROOT}/SKILL.md`
2. `${CLAUDE_PLUGIN_ROOT}/runtimes/claude/SKILL.md`

`scripts/validate.py` enforces root completeness, overlay allowlists, package identity, composition references and order, root-description parity, and plugin-manifest parity.

## Consequences

- A Claude plugin invocation loads the common contract and Claude overlay. The bare `/gulf-middle-east` command resolves in the tested Claude Code version.
- Codex retains its structured-output and validation-chain behavior without maintaining a second common contract.
- The standard Agent Skills validator accepts the packaged skill.
- OpenClaw remains an explicit gap rather than an untested wrapper.
- The structural smoke test is recorded in [`../../evals/2026-08-24-runtime-loading-smoke.md`](../../evals/2026-08-24-runtime-loading-smoke.md).
- This change does not verify facts, measure model quality, establish adoption, or create buyer evidence.
