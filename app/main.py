from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.api.episode import router as episode_router
from app.api.rss import router as rss_router
from app.config import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.dispose()


main_app = FastAPI(title="Podcast API", lifespan=lifespan)
main_app.include_router(episode_router)
main_app.include_router(rss_router)
