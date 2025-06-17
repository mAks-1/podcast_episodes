from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.config import db_helper
from app.models.podcast_episode import PodcastEpisodeModel
from app.schemas.podcast_episode import PodcastEpisode, PodcastEpisodeCreate
from app.crud import podcast_episode as crud_podcast_episode

router = APIRouter(prefix="/episodes", tags=["Episodes"])


@router.get("/", response_model=list[PodcastEpisode])
async def get_episodes(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    episodes = await crud_podcast_episode.get_all_episodes(session=session)
    return episodes if episodes else []


@router.post("/", response_model=PodcastEpisode, status_code=status.HTTP_201_CREATED)
async def create_episode(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    episode_create: PodcastEpisodeCreate,
):
    return await crud_podcast_episode.create_episode(
        session=session,
        episode_create=episode_create,
    )
