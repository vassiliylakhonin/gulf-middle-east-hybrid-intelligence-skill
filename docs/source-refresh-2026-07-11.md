# Source refresh — 2026-07-11

## Scope

Reviewed the three `examples/live-source-backed-*.md` files. The pass checked every cited URL for reachability and re-read the current primary pages that carry time-sensitive sanctions, AML/CFT, maritime-risk, and oil-market context.

This is a source-maintenance pass, not sanctions screening, vessel screening, legal advice, or factual verification of named counterparties. No named entity or vessel status was assessed.

## Confirmed primary surfaces

- OFAC Iran program, enforcement, FAQ, General License, and SDN-list pages remained reachable. Entity-level status still requires point-of-decision screening.
- [MENAFATF second-round evaluation reports](https://www.menafatf.org/mutual-evaluations-follow/evaluation-reports-2) replaced the removed `/mutual-evaluation` path.
- [SAMA in-force AML/CTF guidance](https://rulebook.sama.gov.sa/en/guidance-anti-money-laundering-and-combating-terrorist-financing) replaced the retired RulesInstructions path.
- [LMA JWC listed areas](https://lmalloyds.com/specialist-areas/underwriting/listed-areas/) and the [June 2026 IEA OMR](https://www.iea.org/reports/oil-market-report-june-2026) were retrieved and added to the Red Sea example.
- CMF, IMO, BIS consolidated banking statistics, CBUAE, and FATF source roles remain appropriate. Some sites return automated-client `403`; that is an access limitation, not evidence that the source was removed.

## Remaining limits

- UKMTO returned `403` in this session. Operational incident or advisory claims remain `[verify]`.
- The refresh does not convert the dark-fleet skeleton into a live-source-backed example; AIS and vessel-identity evidence remain absent.
- Historical retrieval dates remain unchanged unless the underlying source was actually re-read on 2026-07-11.
