"""MCP server for the Gulf and Middle East skill.

The three screening tools are declared so the transport and tool surface can
be exercised, and each one refuses instead of answering. The implemented tools
are deterministic and data-free: `estimate_chokepoint_bypass` combines
caller-supplied figures, each with a caller-stated source. Neither adds data or
produces a finding.

The first version of this file returned `{"status": "clear", "confidence": 0.95}`
for any entity name it was given, and AGENTS.md points an agent at this file to
"expose tools to the agent". A fabricated clearance is worse than no tool: an
agent has no way to tell it apart from a real screening result. Until a tool is
backed by an actual source, it must say so.
"""

from mcp.server.mcpserver import MCPServer

from .chokepoint import estimate_bypass_json
from .contract import unimplemented_response

mcp = MCPServer("gulf-middle-east-compliance-server", version="0.3.0")


def _unimplemented(tool: str, needs: str, **echo: object) -> str:
    return unimplemented_response(tool, needs, **echo)


@mcp.tool()
def query_regional_sanctions(entity_name: str) -> str:
    """Screen an entity against regional sanctions lists. Not yet implemented.

    Returns status ``not_implemented``. Do not read the response as a clearance.
    """
    return _unimplemented(
        "query_regional_sanctions",
        "a sanctions list source (OFAC SDN, EU consolidated, UK OFSI, or UN)",
        entity=entity_name,
    )


@mcp.tool()
def analyze_graph_relationships(node_id: str, depth: int = 2) -> str:
    """Traverse the regional knowledge graph. Not yet implemented.

    Returns status ``not_implemented``. An empty edge list is not evidence of
    an absence of connections.
    """
    return _unimplemented(
        "analyze_graph_relationships",
        "an ownership or control graph to traverse",
        node=node_id,
        depth=depth,
    )


@mcp.tool()
def retrieve_memory_context(client_id: str) -> str:
    """Retrieve a client's recorded risk appetite and past verdicts. Not yet implemented.

    Returns status ``not_implemented``. Absence of escalations here does not mean
    a client has none.
    """
    return _unimplemented(
        "retrieve_memory_context",
        "a persisted client record store",
        client=client_id,
    )


@mcp.tool()
def estimate_chokepoint_bypass(scenario: dict) -> str:
    """Compare route days, fuel and cost from caller-supplied figures.

    ``scenario`` is a JSON object: ``currency`` and ``routes`` (name,
    distance_nm, speed_knots, fuel_tonnes_per_sea_day, fuel_price_per_tonne,
    and optional waiting_days, idle_fuel_tonnes_per_day, hire_per_day,
    war_risk of premium percent, insured value and a transit count, and
    other_costs), plus an optional ``baseline_route`` name. Every figure is
    ``{"low": ..., "high": ..., "source": ...}``; a figure without a source
    is rejected, never defaulted. The tool holds no tariff, premium, fuel,
    distance or chokepoint-status data, does not rank or recommend routes,
    and returns low/high ranges and deltas against the baseline. The result
    is arithmetic on the caller's inputs, not a finding about any route.
    """
    return estimate_bypass_json(scenario)


def main() -> None:
    """Console-script entry point declared in ``pyproject.toml``."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
