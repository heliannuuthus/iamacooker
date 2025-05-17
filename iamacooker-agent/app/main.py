from fastapi import FastAPI

from app.agent import init_agent_config
from app.internal import get_logger
from app.route import howtocook_router

logger = get_logger(__name__)
init_agent_config()


app = FastAPI()

app.include_router(howtocook_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=18000, reload=True)
