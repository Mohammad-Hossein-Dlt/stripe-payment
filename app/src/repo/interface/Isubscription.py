from abc import ABC, abstractmethod
from src.domain.schemas.payment.subscription import SubscriptionModel

class ISubscriptionRepo(ABC):
    
    @abstractmethod
    async def create(
        subscription: SubscriptionModel,
    ) -> SubscriptionModel:
    
        raise NotImplementedError
    
    @abstractmethod
    async def get_by_id(
        sub_id: str,
    ) -> SubscriptionModel:
    
        raise NotImplementedError
    
    @abstractmethod
    async def get_all() -> list[SubscriptionModel]:
        
        raise NotImplementedError
