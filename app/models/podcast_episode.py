from sqlalchemy import Column, Integer, String
from app.models.base import Base

class PodcastEpisode(Base):
    __tablename__ = "episodes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    host = Column(String, nullable=False)
