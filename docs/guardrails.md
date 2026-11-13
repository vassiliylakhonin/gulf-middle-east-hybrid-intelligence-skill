# Review Guardrails

1. Never convert a missing source, graph edge, or memory record into a clearance.
2. Current sanctions, ownership, vessel, regulatory, and enforcement claims require
   verification against current primary sources.
3. The skill may recommend continuing review, requesting evidence, escalating to
   a human, or stopping pending review. It does not approve transactions or
   execute enforcement actions.
4. A confidence or sufficiency score describes the supplied evidence only; it is
   not a probability of legality, safety, or absence from a sanctions list.
5. MCP tools that return `not_implemented` have produced no finding.
6. An `estimate_chokepoint_bypass` result is arithmetic on caller-supplied
   figures, each with a caller-stated source; it is not a finding about any
   chokepoint, route or war-risk premium, it does not rank or recommend routes,
   and the tool holds no tariff, premium, fuel or distance data.
7. A `compare_entity_records` result lists field values that two caller-supplied
   records share. A shared address, agent, phone or officer is common among
   unrelated firms; the list is not a finding that two entities are the same
   network, that one reconstituted the other, or that either is sanctioned, and
   no match is not evidence of no link. The tool consults no sanctions list.
