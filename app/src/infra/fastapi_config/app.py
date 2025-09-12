from fastapi import FastAPI
from app.src.infra.fastapi_config.app_lifespan import lifespan

app: FastAPI = FastAPI(
    lifespan=lifespan,
)