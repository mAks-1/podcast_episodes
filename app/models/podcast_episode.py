from uuid import uuid4

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base

class PodcastEpisodeModel(Base):
    __tablename__ = "episodes"

    podcast_episode_id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid4()), index=True
    )
    title: Mapped[str] = mapped_column(unique=False, nullable=False)
    description: Mapped[str] = mapped_column(unique=False, nullable=False)
    host: Mapped[str] = mapped_column(unique=False, nullable=False)
