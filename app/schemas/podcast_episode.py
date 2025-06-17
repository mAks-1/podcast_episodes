from typing import Literal

from pydantic import BaseModel, Field


class PodcastEpisodeCreate(BaseModel):
    title: str
    description: str
    host: str


class PodcastEpisode(PodcastEpisodeCreate):
    podcast_episode_id: str

    class Config:
        orm_mode = True


class GenerationRequest(BaseModel):
    target: Literal["title", "description"]
    prompt: str = Field(..., description="Rewrite the title for a younger audience")
