import os

import httpx
from dotenv import load_dotenv
from httpx import Timeout
from openai import AsyncOpenAI

from app.internal.loggging import get_logger

logger = get_logger(__name__)

load_dotenv()

_ASYNC_OPENAI_CLIENT = None


def get_async_openai_client() -> AsyncOpenAI:
    global _ASYNC_OPENAI_CLIENT
    if _ASYNC_OPENAI_CLIENT is None:
        logger.info("init async openai client")
        _ASYNC_OPENAI_CLIENT = AsyncOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_BASE_URL"),
            http_client=httpx.AsyncClient(timeout=Timeout(timeout=300.0)),
            max_retries=3,
            timeout=Timeout(timeout=300.0),
        )
    return _ASYNC_OPENAI_CLIENT
