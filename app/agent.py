from agents import Agent, ModelSettings, gen_trace_id, trace
from agents.mcp import MCPServerStreamableHttp


def build_agent(mcp_server: MCPServerStreamableHttp) -> Agent:
    return Agent(
        name="HowToCook Assistant",
        instructions="Use the tools to achieve the task",
        mcp_servers=[mcp_server],
        model_settings=ModelSettings(tool_choice="required"),
    )


async def main():
    async with MCPServerStreamableHttp(
        host="127.0.0.1", port=18200, path="/mcp"
    ) as mcp_server:
        trace_id = gen_trace_id()
        with trace(workflow_name="Streamable HTTP Example", trace_id=trace_id):
            print(
                f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}\n"
            )
            await build_agent(mcp_server)


if __name__ == "__main__":
    main()
