import stripe

class GetCustomers:
        
    def execute(
        self,
    ) -> list:
        
        get_customers = stripe.Customer.list()
        
        customers: list = []

        for customer in get_customers.data:
            
            customers.append(
                {
                    "id": customer.id, 
                    "email": customer.email,
                    "name": customer.name,
                },
            )
   
        return customers