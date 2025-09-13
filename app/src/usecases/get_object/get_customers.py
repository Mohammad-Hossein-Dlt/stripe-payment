import stripe

class GetCustomers:
        
    def execute(
        self,
    ) -> list:
        
        get_customers = stripe.Customer.list()
        
        customers: list = []

        for customer_object in get_customers.data:
            
            customers.append(
                {
                    "id": customer_object.id, 
                    "email": customer_object.email,
                    "name": customer_object.name,
                },
            )
   
        return customers