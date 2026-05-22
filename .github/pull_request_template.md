## Summary

What changed and why?

## Checklist

- [ ] `python3 scripts/validate.py` passes locally (CI enforces this on `main`)
- [ ] If `taxonomy.json` or example tags changed, `python3 scripts/render-readme.py` re-run and README diff committed
- [ ] Required README strings preserved: companion repo links, "no production usage record exists yet" / "no real-use evidence" disclosure
- [ ] STATUS.md still reflects honest Bar 1 / Bar 2 status; if criteria moved, evidence is recorded
- [ ] Examples state evidence mode (`live-source-backed`, `user-provided sources`, `illustrative source packet`, or `reasoning-only`) and carry retrieval dates where required
- [ ] Per-claim provenance tags (Axis A/B) applied in body prose AND in any new tables (table-cell discipline per `AGENTS.md`)
- [ ] Iran-state / IRGC-affiliated / Iran-private commercial actor distinction preserved wherever Iran content appears
- [ ] No fabricated vessel names, IMO numbers, sanctions designations, or chokepoint-incident attributions
- [ ] CA-Caspian-specific content deferred to the [Central Asia + Caspian skill](https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill); no duplication
- [ ] No new infrastructure (MCP server, CLI, schemas, additional validators) — that belongs in [agenda-intelligence-md](https://github.com/vassiliylakhonin/agenda-intelligence-md)
- [ ] CHANGELOG entry added when user-facing behavior changed

## Risks

Any reliability, safety, or trust impact from this change?
