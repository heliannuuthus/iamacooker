from agents import Agent, ModelSettings


def agent() -> Agent:
    return Agent(
        name="HowToCook Agent",
        instructions="You are a helpful assistant that can help with cooking.",
        model_settings=ModelSettings(tool_choice="required"),
    )
