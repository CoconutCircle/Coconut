#!/bin/sh

cd app/
alembic upgrade head
alembic revision --autogenerate
alembic upgrade head 
cd ..

uvicorn app.main:app --host 0.0.0.0 --port 8000