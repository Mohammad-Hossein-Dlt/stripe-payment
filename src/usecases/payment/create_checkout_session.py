import stripe

class CreateCheckoutSession:
        
    def execute(
        self,
        price_id: str,
        customer_email: str | None = None,
    ) -> str:
        
        checkout = stripe.checkout.Session.create(
            payment_method_types=["card"],
            mode="subscription",
            line_items=[
                {
                    "price": price_id,
                    "quantity": 1,
                },
            ],
            customer_email=customer_email,
            success_url="http://localhost:8000/api_v1/payment/success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url="http://localhost:8000/api_v1/payment/cancel",
        )
        
        return checkout.url