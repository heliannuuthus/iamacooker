from agents import Runner
from fastapi import APIRouter, Body
from fastapi.responses import StreamingResponse
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
                logger.info(f"[howtocook] {event}")
                if event.type == "raw_response_event":
                    logger.info(f"[howtocook] {event.data.delta}")
                    yield event.data.delta
                elif event.type == "run_item_stream_event":
                    logger.info("[howtocook] run_item_stream_event")
                    yield event.item.to_json()
                elif event.type == "agent_updated_stream_event":
                    logger.info("[howtocook] agent updated")
                    yield event.new_agent.to_json()
                else:
                    logger.info(f"[howtocook] else {event}")
                    yield "ping"

    return StreamingResponse(output(), media_type="text/event-stream")
