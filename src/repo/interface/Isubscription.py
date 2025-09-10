from abc import ABC, abstractmethod
from domain.schemas.payment.subscription import Subscription

class ISubscriptionRepo(ABC):
    
    @abstractmethod
    async def insert_subscription(
        subscription: Subscription,
    ) -> Subscription:
    
        raise NotImplementedError
    
    @abstractmethod
    async def get_subscription(
        sub_id: str,
    ) -> Subscription:
    
        raise NotImplementedError
    
    @abstractmethod
    async def get_subscriptions() -> list[Subscription]:
        
        raise NotImplementedError
