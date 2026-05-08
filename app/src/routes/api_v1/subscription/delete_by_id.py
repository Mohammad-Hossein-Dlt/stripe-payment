from ._router import router
from fastapi import Query
from fastapi.exceptions import HTTPException
from src.routes.http_response.responses import ResponseMessage
from src.usecases.subscription.delete_by_id import DeleteSubscription

@router.delete(
    "/",
    status_code=200,
    responses={
        **ResponseMessage.HTTP_200_OK("Object deleted successfully", dict),
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    },
    description="Delete customer or subscription with id",
)
async def delete_by_id(
    subscription_id: str = Query(...),
):
    try:
        delete_item_usecase = DeleteSubscription()
        return delete_item_usecase.execute(subscription_id)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
        

    