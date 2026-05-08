from src.repo.interface.Isubscription import ISubscriptionRepo
from src.domain.schemas.payment.subscription import SubscriptionModel

class GetSubscriptions:
    
    def __init__(
        self,
        sub_repo: ISubscriptionRepo,
    ):    

        self.sub_repo = sub_repo
        
    async def execute(
        self,
    ) -> list:
        
        subscriptions: list[SubscriptionModel] = await self.sub_repo.get_all()  
        return [ sub.model_dump(mode="json") for sub in subscriptions ]