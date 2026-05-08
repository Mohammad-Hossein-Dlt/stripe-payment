from .app_context import AppContext
from src.infra.settings.settings import settings
from src.infra.bootstrap.database import init_database_client, terminate_database_client
import stripe

class AppContextManager:
        
    @classmethod
    def init_context(cls):
        
        AppContext.stripe_api_key = settings.STRIPE_API_KEY
        stripe.api_key = settings.STRIPE_API_KEY
        
    @classmethod
    async def lazy_init_context(cls):
        
        print("Starting up...")
        
        # if settings.DB_STACK == "mongo_db":
        #     AppContext.db_client = await init_database_client(settings.MONGODB)
            
    @classmethod
    async def terminate_context(cls):
        
        print("Shutting down...")
        
        await terminate_database_client(AppContext.db_client)
        
AppContextManager.init_context()