from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import db_helper
from app.models.podcast_episode import PodcastEpisodeModel
from app.schemas.podcast_episode import (
    PodcastEpisode,
    PodcastEpisodeCreate,
    GenerationRequest,
)
from app.crud import podcast_episode as crud_podcast_episode
from app.services.llm import generate_alternative_llm

router = APIRouter(prefix="/episodes", tags=["Episodes"])


@router.get("/", response_model=list[PodcastEpisode])
async def get_episodes(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    """Get all episodes"""
    episodes = await crud_podcast_episode.get_all_episodes(session=session)
    return episodes if episodes else []


@router.post("/", response_model=PodcastEpisode, status_code=status.HTTP_201_CREATED)
async def create_episode(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    episode_create: PodcastEpisodeCreate,
):
    """Create a new episode"""
    return await crud_podcast_episode.create_episode(
        session=session,
        episode_create=episode_create,
    )


@router.post("/{episode_id}/generate_alternative")
async def generate_alternative_episode_field(
    episode_id: str,
    request: GenerationRequest,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    """Generate an alternative description or title for episode"""
    episode = await session.get(PodcastEpisodeModel, episode_id)
    if not episode:
        raise HTTPException(status_code=404, detail="Episode not found")

    field_value = getattr(episode, request.target)
    try:
        generated = generate_alternative_llm(request.prompt, field_value)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM API error: {str(e)}")

    return {
        "original_episode": {
            "title": episode.title,
            "description": episode.description,
            "host": episode.host,
        },
        "target": request.target,
        "prompt": request.prompt,
        "generated_alternative": generated.strip(),
    }
