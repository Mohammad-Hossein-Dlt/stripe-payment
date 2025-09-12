from pymongo import AsyncMongoClient
from beanie import init_beanie
from app.src.infra.db.mongodb.collections.subscriptions_collection import SubscriptionsCollection

async def init_mongodb(
    host: str,
    port: str,
    user_name: str,
    password: str,
    db_name: str
):
    
    client = AsyncMongoClient(
        host=host,
        port=port,
        username=user_name,
        password=password,
    )
    
    await init_beanie(
        database=client[db_name],
        document_models=[
            SubscriptionsCollection,
        ],
    )