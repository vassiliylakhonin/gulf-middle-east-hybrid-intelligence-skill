# Repository conventions

Contributor-facing conventions for this repo: how the README is structured, what examples must carry, how evaluation docs must be labelled, and what to run before finalizing a change.

Referenced from `AGENTS.md`. Bar 1 criterion B1.1 refers to the "README priorities" section below.

## README priorities

README should make value clear in 30 seconds.

Recommended structure:
1. One-line positioning
2. Problem
3. Try this prompt
4. What it does
5. What it is not
6. Relationship to Agenda Intelligence MD, Global Think Tank Analyst, and Central Asia + Caspian Skill
7. Quick usage
8. Before / after
9. Flagship examples and examples learning path
10. Signal archive
11. Skill files
12. Source guide
13. Risk archetypes
14. Review checklist
15. Limitations
16. Roadmap

## Examples

Examples should be concrete and role-relevant.

Preferred examples:
- Iran sanctions adjacency for an energy buyer
- maritime chokepoint disruption (Hormuz / Bab-el-Mandeb) for a shipping insurer or industrial buyer
- Gulf correspondent banking exposure for a Western respondent bank
- sovereign wealth deployment risk for a target company or co-investor
- dark-fleet / sanctioned-oil flow exposure for a refiner or trader
- Iraq banking-sector reform exposure for a fintech or correspondent bank

Every example must include evidence mode and limitation note.

Examples should be navigable as a learning path, not only as a flat file list. Keep `examples/README.md` aligned with the flagship examples section in `README.md`.

## Evaluation docs

Use honest labels:
- review checklist
- starter rubric
- failure modes

Do not call it a benchmark unless benchmark cases and results actually exist.

## Validation

If validation scripts exist, run them before finalizing changes.

Prefer additive improvements.
Do not introduce heavy dependencies unless necessary.
