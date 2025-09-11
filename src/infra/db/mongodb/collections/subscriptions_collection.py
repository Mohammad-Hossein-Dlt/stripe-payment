from beanie import Document

class SubscriptionsCollection(Document):
    sub_id: str
    customer_id: str
    customer_email: str
    customer_name: str

    class Settings:
        name = "Subscriptions"
