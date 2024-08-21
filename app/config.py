from typing import List
from pydantic import BaseModel
from pydantic_settings import BaseSettings


class FastApiSettings(BaseModel):
    fastapi_host: str = "0.0.0.0"
    fastapi_path: str = ""
    fastapi_port: int = 8000
    fastapi_origins: List[str] = [
        "http://localhost",
        "http://127.0.0.1",
        "http://localhost:4321",
        "http://localhost:8000",
    ]


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://root:root@postgres:5432/app"
    fastapi: FastApiSettings = FastApiSettings()


settings: Settings = Settings()
