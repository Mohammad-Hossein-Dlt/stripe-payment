import stripe

class GetProducts:
        
    def execute(self) -> list:
        
        get_products = stripe.Product.list()
                
        out_put: list = []

        for product in get_products.data:
            
            get_prices = stripe.Price.list(product=product.id)
            
            prices = []
            
            for price in get_prices.data:
                prices.append(
                    {
                        "id": price.id,
                        "nickname": price.nickname,
                        "currency": price.currency,
                        "unit_amount": price.unit_amount // 100 if price.currency == "usd" else price.unit_amount,
                        "product": price.product,
                        "active": price.active,
                    }
                )
                
            out_put.append(
                {
                    "id": product.id, 
                    "name": product.name,
                    "active": product.active,
                    "prices": prices,
                },
            )
                
        return out_put