from repo.interface.Isubscription import ISubscriptionRepo
from domain.schemas.payment.subscription import Subscription
from infra.db.mongodb.collections.subscriptions_collection import SubscriptionsCollection

class SubscriptionMongodbRepo(ISubscriptionRepo):
    
    async def insert_subscription(
        self,
        subscription: Subscription,
    ) -> Subscription:
                
        existing_subscription = await self.get_subscription(subscription.sub_id)
        
        if existing_subscription:
            return existing_subscription
                
        new_subscription = SubscriptionsCollection(**subscription.model_dump())
        insert = await new_subscription.insert()
        
        return Subscription.model_validate(insert, from_attributes=True)

    async def get_subscription(
        self,
        sub_id: str,
    ) -> Subscription:
    
        subscription = await SubscriptionsCollection.find_one({"sub_id": sub_id})
        return subscription
    
    async def get_subscriptions(
        self,
    ) -> list[Subscription]:
        
        subscriptions = await SubscriptionsCollection.find_all().to_list()
        
        out_put = [Subscription.model_validate(subscription, from_attributes=True) for subscription in subscriptions]
        
        return out_put
