# Examples

Worked examples produced in the Gulf + Middle East Hybrid Intelligence skill style.

Every example declares its evidence mode and includes a limitation note. None of these are intelligence products. None are legal, compliance, sanctions, AML, or investment advice.

## Current examples

| File | Mode | Topic |
|---|---|---|
| [live-source-backed-ofac-iran-shipping-sanctions.md](live-source-backed-ofac-iran-shipping-sanctions.md) | `live-source-backed` | OFAC Iran shipping-sector sanctions — exposure framing for a GCC-hub commodity trader. Primary sources: E.O. 13846, E.O. 13902, OFAC SDN list, OFAC Iran program page. Retrieved 2026-05-12. |
| [live-source-backed-gcc-correspondent-banking.md](live-source-backed-gcc-correspondent-banking.md) | `live-source-backed` | GCC correspondent banking exposure for a Western respondent bank. Primary sources: FATF UAE grey-listing/de-listing record, BIS CBS, MENAFATF assessments, CBUAE and SAMA AML frameworks. Retrieved 2026-05-12. |
| [iran-sanctions-routing-exposure.md](iran-sanctions-routing-exposure.md) | `reasoning-only` | Iran sanctions adjacency for a European refiner sourcing Gulf crude |
| [hormuz-shipping-disruption.md](hormuz-shipping-disruption.md) | `illustrative source packet` | Hormuz disruption exposure framing for a shipping insurer |
| [user-provided-sources-sovereign-wealth-deployment.md](user-provided-sources-sovereign-wealth-deployment.md) | `user-provided sources` | Sovereign wealth deployment risk for a target company or co-investor receiving GCC SWF capital. Template with PIF / ADIA / Mubadala / QIA / KIA public mandate URLs. |
| [user-provided-sources-iraq-banking.md](user-provided-sources-iraq-banking.md) | `user-provided sources` | Iraq banking-sector exposure for a Western correspondent bank (template form) |

## Deferred from initial release

The following preferred examples (per `AGENTS.md` "Examples") are not in the initial release. They are deferred with explicit reasons:

- **GCC correspondent banking exposure for a Western respondent bank** — ✅ added. See [live-source-backed-gcc-correspondent-banking.md](live-source-backed-gcc-correspondent-banking.md).
- **Sovereign wealth deployment risk for a target company or co-investor** — ✅ added. See [user-provided-sources-sovereign-wealth-deployment.md](user-provided-sources-sovereign-wealth-deployment.md).
- **Dark-fleet / sanctioned-oil flow exposure for a refiner or trader** — deferred. Requires `live-source-backed` mode with current OFAC vessel designations, AIS-derived patterns from primary maritime intelligence sources, and current G7 price-cap enforcement guidance. Not produced in `reasoning-only` mode because the value of this archetype depends on source-anchored vessel and flow data.

## `live-source-backed` mode

The first `live-source-backed` example is now included: [live-source-backed-ofac-iran-shipping-sanctions.md](live-source-backed-ofac-iran-shipping-sanctions.md). It cites primary OFAC and Treasury sources with a retrieval date of 2026-05-12. Re-verify primary sources (especially the SDN list) before operational use — the SDN list is updated without fixed schedule.

`docs/source-guide.md` contains a full re-verification horizons table covering all primary source types.

## How to read these examples

Each example follows the output structure in [`skills/claude/SKILL.md`](../skills/claude/SKILL.md): bottom line, scope, primary driver, mechanism, exposure map, actor incentives, role-based implications, trigger points, unknowns, confidence, what-would-change-the-judgment, limitation note.

Skip sections that do not apply to a specific question.
