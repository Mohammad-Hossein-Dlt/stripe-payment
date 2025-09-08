from domain.schemas.payment.subscription import Subscription
from repo.interface.Isubscription import ISubscriptionRepo
import stripe

class SuccessPayment:

    def __init__(
        self,
        sub_repo: ISubscriptionRepo,
    ):    
        self.sub_repo = sub_repo
        
    async def execute(
        self,
        session_id: str,
    ) -> dict:
        
        new_customer = stripe.checkout.Session.retrieve(
            id=session_id,
        )

        subscription = Subscription(
            sub_id=new_customer["subscription"],
            customer_id=new_customer["customer"],
            customer_email=new_customer["customer_details"]["email"],
            customer_name=new_customer["customer_details"]["name"],
        )
                
        inserted_subscription = await self.sub_repo.insert_subscription(subscription)
                
        return inserted_subscription.model_dump()
    
