from beanie import Document
from app.src.domain.schemas.payment.subscription import SubscriptionModel

class SubscriptionsCollection(SubscriptionModel, Document):
    
    class Settings:
        name = "Subscriptions"
