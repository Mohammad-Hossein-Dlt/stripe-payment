from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.src.infra.settings.settings import settings
from app.src.infra.db.mongodb.client import init_mongodb
from .app_state import AppStates, set_app_state
import stripe

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    stripe.api_key = settings.STRIPE_API_KEY
    
    await init_mongodb(
        settings.MONGO_HOST,
        settings.MONGO_PORT,
        settings.MONGO_INITDB_ROOT_USERNAME,
        settings.MONGO_INITDB_ROOT_PASSWORD,
        settings.MONGO_INITDB_DATABASE,
    )
    
    set_app_state(app, AppStates.EXTERNAL_FASTAPI_PORT, settings.EXTERNAL_FASTAPI_PORT)
    set_app_state(app, AppStates.INTERNAL_FASTAPI_PORT, settings.INTERNAL_FASTAPI_PORT)
            
    yield    
