# Gulf + Middle East risk archetypes

A reference catalogue of risk archetypes that recur in Gulf, Iran, Iraq, and maritime-chokepoint analysis. Use them as **patterns** to structure reasoning, not as factual claims about any specific entity, vessel, or jurisdiction. Operational use requires source-backed verification.

For each archetype: mechanism → typical indicators → evidence needed → common false positives → watch-next triggers → role-based mitigation questions.

---

## 1. Iran sanctions adjacency

- **Mechanism:** counterparty is not designated but is owned, controlled by, or substantively linked to a designated Iran-state, IRGC-affiliated, or Iran-sanctioned entity (50%-rule equivalents and control tests).
- **Typical indicators:** shared addresses, directors, phone numbers; immediate post-designation incorporation of successor entities; UAE/Oman/Turkey free-zone entities with no operational footprint and Iranian beneficial owners.
- **Evidence needed:** corporate registry data, transactional records, network-graph analysis, primary OFAC SDN List checks.
- **False positives:** coincidental name overlap, common service-provider addresses, legitimate Iranian diaspora business.
- **Watch-next triggers:** OFAC enforcement actions naming Gulf-jurisdiction entities; new SDN List additions; FATF/MENAFATF mutual evaluation findings.
- **Mitigation questions (role-based):** sanctions compliance — EDD on UAE/Oman/Turkey free-zone counterparties with Iran-nexus indicators; AML — corridor- and BO-level monitoring; investor — concentration of revenue or counterparties in Iran-adjacent flows.

## 2. Dark-fleet and ship-to-ship (STS) transfers

- **Mechanism:** sanctioned or restricted oil (Iranian, Russian, Venezuelan) is moved via a parallel tanker fleet that disables or spoofs AIS, conducts STS transfers in international waters, swaps documentation, and delivers to permissive buyers (often Chinese teapot refiners, Indian refiners during permissive windows).
- **Typical indicators:** vessels with frequent flag changes, ownership through opaque single-vessel companies in Marshall Islands or similar registries, AIS gaps in Persian Gulf or eastern Mediterranean STS zones, mismatched cargo manifests.
- **Evidence needed:** AIS data (Kpler, TankerTrackers, Lloyd's List Intelligence), classification society records, flag-state registries, cargo manifests where available, OFAC vessel designations.
- **False positives:** legitimate AIS gaps in coverage areas, routine STS for blending or lightering, normal flag changes for fleet management.
- **Watch-next triggers:** OFAC vessel designations; new G7 price-cap enforcement guidance; flag-state crackdowns; insurance-club expulsions.
- **Mitigation questions:** energy trader — counterparty refiner due diligence and cargo provenance; shipping insurer — vessel-history screening; bank — trade-finance LC scrutiny on Gulf-origin cargoes.

## 3. GCC correspondent banking exposure

- **Mechanism:** Western tier-1 banks face enforcement risk on GCC respondent banks that handle Iran-linked, IRGC-linked, or sanctioned-cargo flows. De-risking pressures lead to narrowing correspondent relationships, longer settlement times, and disruption to legitimate trade-finance flows.
- **Typical indicators:** rising rejection rates on USD wire transfers, increased KYC requests on Gulf-origin payments, narrowing list of acceptable Gulf respondents, sudden requests for enhanced documentation on routine trade flows.
- **Evidence needed:** respondent-bank communications, settlement and rejection metrics, public enforcement actions, BIS consolidated banking statistics.
- **False positives:** routine periodic reviews, system migrations, individual-customer issues unrelated to sanctions.
- **Watch-next triggers:** OFAC enforcement actions against Gulf-jurisdiction banks; new circumvention guidance; FATF/MENAFATF grey-list moves; central-bank consultations on de-risking.
- **Mitigation questions:** correspondent bank — diversification across acceptable respondents; respondent bank — enhanced sanctions-compliance demonstration to retain correspondents; corporate treasurer — payment-rail redundancy planning.

## 4. Sovereign wealth deployment risk

- **Mechanism:** Gulf sovereign wealth funds (PIF, ADIA, Mubadala, QIA, KIA) deploy capital with strategic objectives that may diverge from financial returns: industrial policy (PIF Vision 2030 megaprojects), geopolitical influence, reputation management. Co-investors and target companies face governance, transparency, and reputational risk distinct from typical institutional capital.
- **Typical indicators:** governance terms favoring sovereign-wealth control rights beyond economic stake; mandate ambiguity (financial return vs. strategic deployment); board composition tilted to royal-family commercial network rather than independent directors; reputational events around the sponsoring state affecting the portfolio.
- **Evidence needed:** investment terms (where disclosed), fund mandate publications, IMF Article IV references to sovereign wealth governance, news on sponsoring-state political events.
- **False positives:** standard institutional governance terms; sovereign-wealth investment in established asset classes with no strategic overlay.
- **Watch-next triggers:** sponsoring-state political incidents (Khashoggi-class events, succession dynamics); fund leadership changes; mandate-redirection announcements; macro pressure on sponsoring-state oil revenues forcing repatriation.
- **Mitigation questions:** target company — control-rights and exit clauses; co-investor — alignment of mandate; portfolio-LP — concentration limits and reputational-event handling.

## 5. Maritime chokepoint disruption (Hormuz, Bab-el-Mandeb)

- **Mechanism:** Hormuz, Bab-el-Mandeb, and the Red Sea / Suez approaches are concentrated chokepoints for global oil and LNG flows. Disruption (Iranian harassment, mining incidents, Houthi anti-ship missile and drone attacks, vessel seizures) raises war-risk insurance premiums, forces routing diversion (Cape of Good Hope), and creates corridor-specific oil-price corridors rather than point forecasts.
- **Typical indicators:** war-risk insurance premium changes; tanker-traffic deviations visible in AIS aggregate data; reroute decisions by major shipping lines (Maersk, MSC, CMA CGM) and tanker operators; freight-rate spikes; insurance-club advisories.
- **Evidence needed:** IEA/EIA monthly reports for supply impact; IMO incident reports; war-risk insurance market data; AIS aggregate traffic data; carrier announcements.
- **False positives:** routine fleet repositioning, weather-related reroutes, single-incident misreads as pattern.
- **Watch-next triggers:** new named closure or seizure incident; ceasefire status changes; Houthi attack pattern shifts; US Fifth Fleet posture changes.
- **Mitigation questions:** energy buyer — corridor-aware hedge structure rather than point hedge; shipping insurer — war-risk underwriting and exposure aggregation; refiner — alternative-corridor cargo lining; LNG buyer — Cape diversion cost modeling.

## 6. Sanctioned-oil flow concentration

- **Mechanism:** Iranian and other sanctioned oil flows concentrate in a small number of buyers (China teapot refiners, occasional Indian refiners, Syrian flows), payment rails (often non-USD), and financial intermediaries. Disruption of any one node can shift flow patterns rapidly. Buyer-side enforcement risk is the dominant transmission channel.
- **Typical indicators:** sudden volume changes in Chinese crude imports of "Malaysian", "Omani", or "blends" (often documentation cover for Iranian origin); refinery utilization patterns at known buyer facilities; OFAC enforcement actions on buyer-side facilitators.
- **Evidence needed:** Kpler/Vortexa flow data; Chinese customs disaggregated data where available; OFAC enforcement and FAQ guidance.
- **False positives:** legitimate origin-country crude flows; mislabeled but not sanctioned blends.
- **Watch-next triggers:** OFAC enforcement against Chinese teapot facilitators; payment-rail enforcement (e.g., yuan-clearing or hawala-network actions); buyer-side capacity changes.
- **Mitigation questions:** trader — provenance documentation depth; refiner — cargo-class compliance audit; bank — trade-finance LC scrutiny on permissive-jurisdiction cargoes.

## 7. Sanctioned-party post-designation reconstitution

- **Mechanism:** designated entities are reconstituted under successor names, often with the same beneficial ownership and operational footprint, immediately after designation. Common in IRGC-affiliated commercial networks and certain Hezbollah-linked Lebanese entities.
- **Typical indicators:** new entity incorporated within days/weeks of a designation; same address, directors, or phone numbers; assets transferred to the successor before sanctions enforcement freezes them.
- **Evidence needed:** corporate registry data, OFAC enforcement filings, leaked or open corporate datasets.
- **False positives:** unrelated incorporation activity, legitimate post-designation restructuring.
- **Watch-next triggers:** OFAC successor-entity designations; corporate-registry rule changes in UAE/Lebanon/Turkey; FATF/MENAFATF guidance on post-designation reconstitution.
- **Mitigation questions:** sanctions compliance — successor-entity screening rules; bank — periodic re-screening cadence after designations; legal counsel — 50%-rule control test review.

---

These archetypes are patterns. They do not constitute claims about any specific entity, vessel, family, or jurisdiction. Operational use requires source-backed verification against primary sources listed in [`source-guide.md`](source-guide.md).
