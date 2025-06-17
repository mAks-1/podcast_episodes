# Podcast Episodes API

**Podcast Episodes** — This is a FastAPI service for managing podcast episodes with database storage,
migrations via Alembic, and integration with LLM for generating alternative titles/descriptions.

---

## Features

- CRUD operations on episodes 
- Async work via SQLAlchemy + asyncpg
- Database migrations with Alembic
- Alternative text generation via LLM API (e.g. OpenRouter)

---

## Installation

```commandline
git clone https://github.com/mAks-1/podcast_episodes.git
cd podcast_episodes
docker-compose up -d
```

## Migrations:
### In docker container execute to create migrations:
```commandline
alembic revision --autogenerate -m "initial"
alembic upgrade head
```

### To apply migrations:
```commandline
alembic upgrade head
```

### To downgrade migrations:
```commandline
alembic downgrade base
```

## To stop:
```commandline
docker compose down
```

