from abc import ABC, abstractmethod
from app.src.domain.schemas.payment.subscription import SubscriptionModel

class ISubscriptionRepo(ABC):
    
    @abstractmethod
    async def insert_subscription(
        subscription: SubscriptionModel,
    ) -> SubscriptionModel:
    
        raise NotImplementedError
    
    @abstractmethod
    async def get_subscription(
        sub_id: str,
    ) -> SubscriptionModel:
    
        raise NotImplementedError
    
    @abstractmethod
    async def get_subscriptions() -> list[SubscriptionModel]:
        
        raise NotImplementedError
