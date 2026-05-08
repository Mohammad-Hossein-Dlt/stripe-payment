import stripe

class GetProducts:
        
    def execute(
        self,
    ) -> list:
        
        get_products = stripe.Product.list()
                
        products: list = []

        for product_object in get_products.data:
            
            get_prices = stripe.Price.list(product=product_object.id)
            
            prices = []
            
            for price_object in get_prices.data:
                prices.append(
                    {
                        "id": price_object.id,
                        "nickname": price_object.nickname,
                        "currency": price_object.currency,
                        "unit_amount": price_object.unit_amount // 100 if price_object.currency == "usd" else price_object.unit_amount,
                        "product": price_object.product,
                        "active": price_object.active,
                    }
                )
                
            products.append(
                {
                    "id": product_object.id, 
                    "name": product_object.name,
                    "active": product_object.active,
                    "prices": prices,
                },
            )
                
        return products