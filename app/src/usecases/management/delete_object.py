import stripe

class DeleteObject:
        
    def execute(
        self,
        object_id: str,
    ) -> dict:
        
        pairs = {
            "cus_": "customer",
            "sub_": "subscription",
        }
        
        request_type = ""
        delete_status = None
        
        for i in pairs:
            if object_id.startswith(i):
                request_type = pairs[i]
        
        if request_type == "customer":
            delete_customer = stripe.Customer.delete(object_id)
            delete_status = delete_customer.deleted
        
        elif request_type == "subscription":
            delete_subscription = stripe.Subscription.delete(object_id)
            delete_status = True if delete_subscription.status == "canceled" else False
  
        out_put: dict = {
            "request": request_type+"/delete",
            "id": object_id,
            "status": delete_status,
        }
        
        return out_put

        