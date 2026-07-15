# Use the evidence-packet handoff as the primary Agenda seam

Status: accepted — 2026-07-15

## Context

The specialist produces regional reasoning and may still participate in the older Agenda Intelligence `analyze` workflow. Agenda Intelligence MD v1.3.0 now leads with a smaller `claims[] + sources[]` evidence-packet contract. The older memo-schema, scoring, and MCP contracts remain available for compatibility.

## Decision

The primary composition seam is an evidence-packet handoff containing externally checkable factual and quantitative claims plus caller-supplied source text. Regional assessments, scenarios, assumptions, and analyst judgments remain in the specialist memo. The older strategic-intelligence contracts are compatibility paths.

## Consequences

- Gulf and Middle East mechanism logic stays in this authoring source.
- Agenda Intelligence can lint packet completeness without claiming sanctions, vessel, ownership, or factual verification.
- Existing `analyze` agent-evals remain historical compatibility evidence rather than validation of the current linter.
- The handoff shape is documented and guarded in CI without vendoring Agenda Intelligence's schema.
