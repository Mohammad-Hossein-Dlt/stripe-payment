from src.repo.interface.Isubscription import ISubscriptionRepo
from src.repo.mongodb.subscription_repo import SubscriptionMongodbRepo

def subscription_depend() -> ISubscriptionRepo:
    return SubscriptionMongodbRepo()
