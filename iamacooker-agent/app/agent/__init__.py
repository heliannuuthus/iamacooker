from .howtocook import agent as howtocook_agent


def init_agent_config():
    import os

    import httpx
    from agents import set_default_openai_client
    from dotenv import load_dotenv
    from httpx import Timeout
    from openai import AsyncOpenAI

    load_dotenv()

    set_default_openai_client(
        AsyncOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_BASE_URL"),
            http_client=httpx.AsyncClient(timeout=Timeout(timeout=300.0)),
            max_retries=3,
            timeout=Timeout(timeout=300.0),
        ),
    )
