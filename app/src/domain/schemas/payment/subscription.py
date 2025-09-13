from bson import ObjectId
from pydantic import BaseModel, ConfigDict, Field, model_validator
from beanie import PydanticObjectId

class SubscriptionModel(BaseModel):
    id: PydanticObjectId = Field(default_factory=ObjectId)
    sub_id: str
    customer_id: str
    customer_email: str
    customer_name: str
    
    model_config = ConfigDict(
        extra='ignore',
    )
    
    @model_validator(mode="before")
    def map_id(cls, values: dict) -> dict:

        if "_id" in values:
            values["id"] = values.pop("_id")
        return values