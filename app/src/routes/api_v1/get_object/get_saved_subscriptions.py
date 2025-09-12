from ._router import router
from fastapi import Depends, HTTPException
from app.src.routes.http_response.responses import ResponseMessage
from app.src.repo.interface.Isubscription import ISubscriptionRepo
from app.src.routes.depends.subscription_repo_depend import get_subscription_repo
from app.src.usecases.get_object.get_saved_subscriptions import GetSavedSubscriptions

@router.get(
    "/get-saved-subscriptions",
    status_code=200,
    responses={
        **ResponseMessage.HTTP_200_OK("Products retrieved successfully", list),
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    },
    description="Get all saved subscriptions from database"
)
async def get_saved_subscriptions(
    sub_repo: ISubscriptionRepo = Depends(get_subscription_repo),
):
    try:
        get_products_usecase = GetSavedSubscriptions(sub_repo)
        return await get_products_usecase.execute()
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

        