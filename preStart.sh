#!/bin/sh
export $(grep -v '^#'.env | xargs)

alembic upgrade head

uvicorn app.main:app --host 0.0.0.0 --port 8000