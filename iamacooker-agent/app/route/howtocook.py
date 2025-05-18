from agents import Runner
from fastapi import APIRouter, Body
from fastapi.responses import StreamingResponse
from openai.types.responses import ResponseTextDeltaEvent
from pydantic import BaseModel

from app.agent import howtocook_agent
from app.agent.mcp import howtocook_mcp
from app.internal import get_logger

logger = get_logger(__name__)


class HowToCookRequest(BaseModel):
    input: str


router = APIRouter()


@router.post("/howtocook")
async def howtocook(request: HowToCookRequest = Body(...)):
    logger.info(f"[howtocook] 今天吃什么: {request.input}")
    agent = howtocook_agent()

    async def output():
        async with howtocook_mcp() as mcp_server:
            agent.mcp_servers.append(mcp_server)
            async for event in Runner.run_streamed(
                starting_agent=agent, input=request.input
            ).stream_events():
                if event.type == "raw_response_event" and isinstance(
                    event.data, ResponseTextDeltaEvent
                ):
                    logger.info(f"[howtocook] {event.data.delta}")
                    yield event.data.delta
                elif event.type == "run_item_stream_event":
                    logger.info("[howtocook] run_item_stream_event")
                elif event.type == "agent_updated_stream_event":
                    logger.info("[howtocook] agent updated")
                else:
                    logger.info(f"[howtocook] else {event}")

    return StreamingResponse(output(), media_type="text/event-stream")
