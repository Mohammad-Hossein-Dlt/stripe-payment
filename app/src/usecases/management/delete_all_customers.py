import stripe

class DeleteAllCustomers:
        
    def execute(
        self,
    ) -> dict:
        
        customers = stripe.Customer.list()
        
        for customer in customers.data:
            stripe.Customer.delete(customer.id)
            
        out_put: dict = {
            "request": "customers/delete_all",
            "status": True,
        }
        
        return out_put
