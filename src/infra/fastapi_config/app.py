from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from infra.fastapi_config.app_lifespan import lifespan

templates = Jinja2Templates(directory="src/templates")

app: FastAPI = FastAPI(
    lifespan=lifespan,
)