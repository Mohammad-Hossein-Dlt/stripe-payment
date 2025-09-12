from app.src.repo.interface.Isubscription import ISubscriptionRepo
from app.src.repo.mongodb.subscription_mongodb_repo import SubscriptionMongodbRepo

def get_subscription_repo() -> ISubscriptionRepo:
    return SubscriptionMongodbRepo()
