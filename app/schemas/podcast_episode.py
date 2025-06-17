from pydantic import BaseModel

class PodcastEpisodeCreate(BaseModel):
    title: str
    description: str
    host: str

class PodcastEpisode(PodcastEpisodeCreate):
    id: int

    class Config:
        orm_mode = True
