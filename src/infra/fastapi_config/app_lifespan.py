from fastapi import FastAPI
from infra.settings.settings import settings
from contextlib import asynccontextmanager
from infra.db.mongodb.client import init_mongodb
import stripe

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    stripe.api_key = settings.STRIPE_API_KEY
    
    await init_mongodb(
        settings.MONGODB_HOST,
        settings.MONGODB_PORT,
        settings.MONGODB_USERNAME,
        settings.MONGODB_PASSWORD,
    )
            
    yield    
