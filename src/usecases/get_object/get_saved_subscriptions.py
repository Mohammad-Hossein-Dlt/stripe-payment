from repo.interface.Isubscription import ISubscriptionRepo

class GetSavedSubscriptions:
    
    def __init__(
        self,
        sub_repo: ISubscriptionRepo,
    ):    

        self.sub_repo = sub_repo
        
    async def execute(
        self,
    ) -> list:
        
        subscriptions = await self.sub_repo.get_subscriptions()
                
        return subscriptions