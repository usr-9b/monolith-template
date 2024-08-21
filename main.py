import uvicorn

from app import routers
from app.database import engine, Base
from app.config import settings

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging


logging.basicConfig(level=logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("Creating tables in database")
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    yield
    logging.info("Bye!")


app = FastAPI(
    title="Project API",
    description="The Best API for my Best Frontend",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.fastapi.fastapi_origins,
    allow_credentials=False,
    allow_methods=["POST", "GET"],
    allow_headers=[
        "x-token",
        "Content-Type",
    ],
)

for router in routers.all_routers:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        app,
        host=settings.fastapi.fastapi_host,
        port=settings.fastapi.fastapi_port,
        root_path=settings.fastapi.fastapi_path,
    )
