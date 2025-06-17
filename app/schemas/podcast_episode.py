from pydantic import BaseModel


class PodcastEpisodeCreate(BaseModel):
    title: str
    description: str
    host: str


class PodcastEpisode(PodcastEpisodeCreate):
    podcast_episode_id: str

    class Config:
        orm_mode = True
