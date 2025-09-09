from pymongo import AsyncMongoClient
from beanie import init_beanie
from infra.db.mongodb.models.subscriptions_model import SubscriptionsSession


async def init_mongodb(
    host: str,
    port: str,
    user_name: str,
    password: str,
):
    
    client = AsyncMongoClient(
        host=host,
        port=port,
        username=user_name,
        password=password,
    )
    
    await init_beanie(
        database=client["payment_db"],
        document_models=[
            SubscriptionsSession,
        ],
    )