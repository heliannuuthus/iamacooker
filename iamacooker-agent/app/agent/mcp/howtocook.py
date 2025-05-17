from datetime import timedelta

from agents.mcp import MCPServerStreamableHttp


def mcp() -> MCPServerStreamableHttp:
    return MCPServerStreamableHttp(
        name="HowToCook MCP Assistant",
        params={
            "url": "http://127.0.0.1:18200/mcp",
            "headers": {},
            "timeout": timedelta(seconds=5),
        },
    )
