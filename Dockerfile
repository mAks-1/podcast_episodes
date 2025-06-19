FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN apt-get update && apt-get install -y gcc libpq-dev \
  && pip install poetry \
  && poetry config virtualenvs.create false \
  && poetry install --no-root

COPY . .

CMD ["uvicorn", "app.main:main_app", "--host", "0.0.0.0", "--port", "8000"]
