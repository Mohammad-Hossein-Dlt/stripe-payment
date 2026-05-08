from ._router import router
from fastapi import Depends, HTTPException
from src.routes.http_response.responses import ResponseMessage
from src.repo.interface.Isubscription import ISubscriptionRepo
from src.routes.depends.repo_depend import subscription_depend
from src.usecases.subscription.get_all import GetSubscriptions

@router.get(
    "/all",
    status_code=200,
    responses={
        **ResponseMessage.HTTP_200_OK("Products retrieved successfully", list),
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    },
    description="Get all saved subscriptions from database"
)
async def get_all(
    sub_repo: ISubscriptionRepo = Depends(subscription_depend),
):
    try:
        get_products_usecase = GetSubscriptions(sub_repo)
        return await get_products_usecase.execute()
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

        