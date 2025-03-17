## Env Setup

```bash
poetry install

```

```bash
poetry shell
```

## DB migrations

```bash
alembic revision --autogenerate
```

```bash
alembic upgrade head
```

## Dev Server

```bash
fastapi dev app/main.py
```

## Env Example
```
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_SERVER=
POSTGRES_PORT=5432
POSTGRES_DB=
POSTGRES_TEST_DB=

FRONTEND_URL=
SECRET_KEY=
CLIENT_SECRET=
CLIENT_ID=
```

## ENV EXPORT
```bash
export $(grep -v '^#' .env | xargs)
```