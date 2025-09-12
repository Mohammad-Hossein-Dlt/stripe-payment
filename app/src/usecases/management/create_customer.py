import stripe
from faker import Faker

class CreateCustomer:
        
    def execute(
        self,
        customer_name: str | None = None,
        customer_email: str | None = None,
    ) -> dict:
        
        faker = Faker()
        
        name =  customer_name or faker.name()
        email =  customer_email or faker.email()
        
        customer = stripe.Customer.create(
            name=name,
            email=email,
            payment_method="pm_card_visa",
        )
        
        out_put: dict = {
            "customer_id": customer.id,
            "name": customer.name,
            "email": customer.email,
        }
        
        return out_put
