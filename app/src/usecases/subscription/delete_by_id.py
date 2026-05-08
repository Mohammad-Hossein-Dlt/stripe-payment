import stripe

class DeleteSubscription:
        
    def execute(
        self,
        subscription_id: str,
    ) -> dict:
        
        delete_subscription = stripe.Subscription.delete(subscription_id)
        delete_status = True if delete_subscription.status == "canceled" else False
  
        out_put: dict = {
            "request": "delete/subscription",
            "id": subscription_id,
            "status": delete_status,
        }
        
        return out_put

        