# Examples

Worked examples produced in the Gulf + Middle East Hybrid Intelligence skill style.

Every example declares its evidence mode and includes a limitation note. None of these are intelligence products. None are legal, compliance, sanctions, AML, or investment advice.

## Learning path

1. Start with [iran-sanctions-routing-exposure.md](iran-sanctions-routing-exposure.md) to see the reasoning-only structure for Iran sanctions adjacency.
2. Read [hormuz-shipping-disruption.md](hormuz-shipping-disruption.md) to see illustrative source-packet handling for maritime chokepoint risk.
3. Read [live-source-backed-ofac-iran-shipping-sanctions.md](live-source-backed-ofac-iran-shipping-sanctions.md) to see source-backed OFAC / Iran shipping-sector exposure.
4. Read [live-source-backed-gcc-correspondent-banking.md](live-source-backed-gcc-correspondent-banking.md) to see source-backed GCC correspondent-banking risk framing.
5. Read [user-provided-sources-sovereign-wealth-deployment.md](user-provided-sources-sovereign-wealth-deployment.md) to see the mode where the user's source packet is the evidence base.
6. Read [live-source-backed-bab-el-mandeb-red-sea-shipping.md](live-source-backed-bab-el-mandeb-red-sea-shipping.md) to see source-backed Bab-el-Mandeb / Red Sea shipping disruption framing for a war-risk underwriter or industrial charterer. **This example is the canonical demonstration of the Axis A / Axis B provenance-tag system** (`[primary]` / `[secondary]` / `[analyst-judgment]` + optional `[verify]` / `[stale-risk: YYYY-MM]`) defined in AGENTS.md.
7. Read [user-provided-sources-dark-fleet-sanctioned-oil.md](user-provided-sources-dark-fleet-sanctioned-oil.md) to see a `user-provided sources` skeleton-packet memo on dark-fleet and sanctioned-oil flow exposure for a refiner or trader — three deceptive-practice patterns (AIS manipulation, STS in opaque waters, flag-hopping / registry opacity), six transmission channels into the refiner / trader book, attestation-discipline framework under the G7 price cap, and Iran actor distinction applied. Packet: OFAC SDN search, OFAC Iran and Russia programs, US/UK Price Cap Coalition guidance, EU and Swiss SECO lists, IMO GISIS, IGP&I, FATF / MENAFATF.

| File | Mode | Topic |
|---|---|---|
| [live-source-backed-ofac-iran-shipping-sanctions.md](live-source-backed-ofac-iran-shipping-sanctions.md) | `live-source-backed` | OFAC Iran shipping-sector sanctions — exposure framing for a GCC-hub commodity trader. Primary sources: E.O. 13846, E.O. 13902, OFAC SDN list, OFAC Iran program page. Retrieved 2026-05-12. |
| [live-source-backed-gcc-correspondent-banking.md](live-source-backed-gcc-correspondent-banking.md) | `live-source-backed` | GCC correspondent banking exposure for a Western respondent bank. Primary sources: FATF UAE grey-listing/de-listing record, BIS CBS, MENAFATF assessments, CBUAE and SAMA AML frameworks. Retrieved 2026-05-12. |
| [live-source-backed-bab-el-mandeb-red-sea-shipping.md](live-source-backed-bab-el-mandeb-red-sea-shipping.md) | `live-source-backed` | Bab-el-Mandeb / Red Sea shipping disruption — pricing and routing exposure for a shipping insurer or industrial charterer. Combined Maritime Forces (CTF 153) and IMO primary pages retrieved 2026-05-15. UKMTO and Lloyd's JWC cited `[verify]` (retrieval failed). |
| [iran-sanctions-routing-exposure.md](iran-sanctions-routing-exposure.md) | `reasoning-only` | Iran sanctions adjacency for a European refiner sourcing Gulf crude |
| [hormuz-shipping-disruption.md](hormuz-shipping-disruption.md) | `illustrative source packet` | Hormuz disruption exposure framing for a shipping insurer |
| [user-provided-sources-sovereign-wealth-deployment.md](user-provided-sources-sovereign-wealth-deployment.md) | `user-provided sources` | Sovereign wealth deployment risk for a target company or co-investor receiving GCC SWF capital. Template with PIF / ADIA / Mubadala / QIA / KIA public mandate URLs. |
| [user-provided-sources-iraq-banking.md](user-provided-sources-iraq-banking.md) | `user-provided sources` | Iraq banking-sector exposure for a Western correspondent bank (template form) |
| [user-provided-sources-dark-fleet-sanctioned-oil.md](user-provided-sources-dark-fleet-sanctioned-oil.md) | `user-provided sources` | Dark-fleet / sanctioned-oil flow exposure for a refiner or trader — skeleton packet (OFAC, EU, UK OFSI, Swiss SECO, IMO, IGP&I, FATF/MENAFATF) + structural framing of three deceptive-practice patterns and six transmission channels; Iran actor distinction applied. |

## Deferred from initial release

The following preferred examples (per `AGENTS.md` "Examples") are not in the initial release. They are deferred with explicit reasons:

- **GCC correspondent banking exposure for a Western respondent bank** — ✅ added. See [live-source-backed-gcc-correspondent-banking.md](live-source-backed-gcc-correspondent-banking.md).
- **Sovereign wealth deployment risk for a target company or co-investor** — ✅ added. See [user-provided-sources-sovereign-wealth-deployment.md](user-provided-sources-sovereign-wealth-deployment.md).
- **Maritime chokepoint disruption (Bab-el-Mandeb / Red Sea) for a shipping insurer or industrial buyer** — ✅ added. See [live-source-backed-bab-el-mandeb-red-sea-shipping.md](live-source-backed-bab-el-mandeb-red-sea-shipping.md). Complements the illustrative-source-packet Hormuz example with `live-source-backed` Red Sea framing.
- **Dark-fleet / sanctioned-oil flow exposure for a refiner or trader** — ✅ added as a `user-provided sources` skeleton-packet memo. See [user-provided-sources-dark-fleet-sanctioned-oil.md](user-provided-sources-dark-fleet-sanctioned-oil.md). The skill does not retrieve live OFAC SDN, AIS, or G7 price-cap attestation state itself; the memo delivers the structural framing (three deceptive-practice patterns, six transmission channels, role-based implications, Iran actor distinction) and a packet of canonical mandate pages the user retrieves at point of decision to supply the binding evidence. AIS-derived observations and licensed maritime-intelligence inputs remain outside the skill's authority.

## `live-source-backed` mode

The first `live-source-backed` example is now included: [live-source-backed-ofac-iran-shipping-sanctions.md](live-source-backed-ofac-iran-shipping-sanctions.md). It cites primary OFAC and Treasury sources with a retrieval date of 2026-05-12. Re-verify primary sources (especially the SDN list) before operational use — the SDN list is updated without fixed schedule.

`docs/source-guide.md` contains a full re-verification horizons table covering all primary source types.

## How to read these examples

Each example follows the output structure in [`skills/claude/SKILL.md`](../skills/claude/SKILL.md): bottom line, scope, primary driver, mechanism, exposure map, actor incentives, role-based implications, trigger points, unknowns, confidence, what-would-change-the-judgment, limitation note.

Skip sections that do not apply to a specific question.
