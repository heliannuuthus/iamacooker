from app.internal import get_openai_client
from app.internal.loggging import get_logger

from .howtocook import agent as howtocook_agent

logger = get_logger(__name__)


def init_agent_config():
    from agents import enable_verbose_stdout_logging, set_default_openai_client

    enable_verbose_stdout_logging()
    set_default_openai_client(get_openai_client())
