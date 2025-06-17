from typing import Sequence, TYPE_CHECKING

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.podcast_episode import PodcastEpisodeModel


async def get_all_episodes(
    session: AsyncSession,
) -> Sequence[PodcastEpisodeModel]:
    stmt = select(PodcastEpisodeModel).order_by(PodcastEpisodeModel.podcast_episode_id)
    result = await session.execute(stmt)
    episodes = result.scalars().all()
    return episodes