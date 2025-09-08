from abc import ABC, abstractmethod
from domain.schemas.payment.subscription import Subscription

class ISubscriptionRepo(ABC):
    
    @abstractmethod
    async def insert_subscription(self, subscription: Subscription) -> Subscription:
        raise NotImplementedError
    
    @abstractmethod
    async def get_subscription(self, sub_id: str) -> Subscription:
        raise NotImplementedError
    
    @abstractmethod
    async def get_subscriptions(self) -> list[Subscription]:
        raise NotImplementedError
