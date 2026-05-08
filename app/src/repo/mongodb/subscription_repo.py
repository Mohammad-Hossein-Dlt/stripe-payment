from src.repo.interface.Isubscription import ISubscriptionRepo
from src.domain.schemas.payment.subscription import SubscriptionModel
from src.infra.database.mongodb.collections.subscription_collection import SubscriptionsCollection
from src.infra.exceptions.exceptions import EntityNotFoundError

class SubscriptionMongodbRepo(ISubscriptionRepo):
    
    async def create(
        self,
        subscription: SubscriptionModel,
    ) -> SubscriptionModel:
        
        try:
            existing_subscription = await self.get_by_id(subscription.sub_id)
            if existing_subscription:
                return existing_subscription
            new_subscription = SubscriptionsCollection.insert(
                SubscriptionsCollection(**subscription.model_dump_for_db(dump_for="create")),
            )
            return SubscriptionModel.model_validate(new_subscription, from_attributes=True)
        except:
            raise

    async def get_by_id(
        self,
        sub_id: str,
    ) -> SubscriptionModel:
        
        try:
            subscription = await SubscriptionsCollection.find_one(
                SubscriptionsCollection.sub_id == sub_id,
            )
            return SubscriptionModel.model_validate(subscription, from_attributes=True)
        except:
            raise EntityNotFoundError(status_code=404, message="Subscription not found")  
        
    async def get_all(
        self,
    ) -> list[SubscriptionModel]:
        
        try:
            subscriptions = await SubscriptionsCollection.find_all().to_list()            
            return [ SubscriptionModel.model_validate(sub, from_attributes=True) for sub in subscriptions ]
        except:
            raise EntityNotFoundError(status_code=404, message="There are no subscriptions")