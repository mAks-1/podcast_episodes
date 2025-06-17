from typing import Sequence, TYPE_CHECKING

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.podcast_episode import PodcastEpisodeModel
from app.schemas.podcast_episode import PodcastEpisodeCreate


async def get_all_episodes(
    session: AsyncSession,
) -> Sequence[PodcastEpisodeModel]:
    """Get all episodes"""
    stmt = select(PodcastEpisodeModel).order_by(PodcastEpisodeModel.podcast_episode_id)
    result = await session.execute(stmt)
    episodes = result.scalars().all()
    return episodes

async def create_episode(
    session: AsyncSession,
    episode_create: PodcastEpisodeCreate,
) -> PodcastEpisodeModel:
    """Create new episode"""
    episode = PodcastEpisodeModel(**episode_create.model_dump())
    session.add(episode)
    await session.commit()
    return episode