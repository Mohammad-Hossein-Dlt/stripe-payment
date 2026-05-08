import stripe

class DeleteCustomer:
        
    def execute(
        self,
        customer_id: str,
    ) -> dict:
        
        delete_customer = stripe.Customer.delete(customer_id)
        delete_status = delete_customer.deleted
            
        out_put: dict = {
            "request": "delete/customer",
            "id": customer_id,
            "status": delete_status,
        }
        
        return out_put

        