from pydantic import BaseModel, ConfigDict
from beanie import PydanticObjectId

class Subscription(BaseModel):
    id: PydanticObjectId | None = None
    sub_id: str | None = None
    customer_id: str | None = None
    customer_email: str | None = None
    customer_name: str | None = None
    
    model_config = ConfigDict(
        extra='ignore',
    )