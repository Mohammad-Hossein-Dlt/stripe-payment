from src.domain.schemas.payment.subscription import SubscriptionModel
from beanie import Document, PydanticObjectId, before_event, Update
from datetime import datetime, timezone

class SubscriptionsCollection(SubscriptionModel, Document):

    id: PydanticObjectId = None
    sub_id: str
    customer_id: str
    customer_email: str
    customer_name: str
    
    class Settings:
        name = "Subscription"

    @before_event(Update)
    def set_updated_at(self):
        self.updated_at = datetime.now(timezone.utc)