from fastapi import FastAPI
from app.connectors.db import create_db_and_tables

app = FastAPI(
    title="Coconut Backend",
)

@app.on_event("startup")
async def startup_event():
    create_db_and_tables()

@app.get("/")
def index():
    return {"message": "Hello world!"}
