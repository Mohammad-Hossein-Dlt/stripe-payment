from fastapi import FastAPI
from infra.fastapi_config.app_lifespan import lifespan

app: FastAPI = FastAPI(
    lifespan=lifespan,
)