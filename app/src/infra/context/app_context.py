from typing import ClassVar
from src.infra.schemas.database.sqlalchemy import SqlalchemyClient
from src.infra.schemas.database.mongodb import MongodbClient

class AppContext(type):
        
    stripe_api_key: ClassVar[str] = None
    db_client: ClassVar[SqlalchemyClient | MongodbClient] = None
