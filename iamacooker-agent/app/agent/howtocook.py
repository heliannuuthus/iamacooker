from agents import Agent, ModelSettings, OpenAIChatCompletionsModel

from app.internal import get_openai_client


def agent() -> Agent:
    return Agent(
        name="HowToCook Agent",
        model=OpenAIChatCompletionsModel(
            model="qwen-plus-latest",
            openai_client=get_openai_client(),
        ),
        instructions="You are a helpful assistant that can help with cooking.",
        model_settings=ModelSettings(
            tool_choice="required",
        ),
    )
