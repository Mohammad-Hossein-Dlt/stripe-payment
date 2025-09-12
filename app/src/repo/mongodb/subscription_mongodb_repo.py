from app.src.repo.interface.Isubscription import ISubscriptionRepo
from app.src.domain.schemas.payment.subscription import SubscriptionModel
from app.src.infra.db.mongodb.collections.subscriptions_collection import SubscriptionsCollection

class SubscriptionMongodbRepo(ISubscriptionRepo):
    
    async def insert_subscription(
        self,
        subscription: SubscriptionModel,
    ) -> SubscriptionModel:
                
        existing_subscription = await self.get_subscription(subscription.sub_id)
        
        if existing_subscription:
            return existing_subscription
                
        new_subscription = SubscriptionsCollection(**subscription.model_dump())
        insert = await new_subscription.insert()
        
        return SubscriptionModel.model_validate(insert, from_attributes=True)

    async def get_subscription(
        self,
        sub_id: str,
    ) -> SubscriptionModel:
    
        subscription = await SubscriptionsCollection.find_one({"sub_id": sub_id})
        return subscription
    
    async def get_subscriptions(
        self,
    ) -> list[SubscriptionModel]:
        
        subscriptions = await SubscriptionsCollection.find_all().to_list()
        
        out_put = [SubscriptionModel.model_validate(subscription, from_attributes=True) for subscription in subscriptions]
        
        return out_put
