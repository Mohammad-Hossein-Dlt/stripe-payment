from fastapi.exceptions import HTTPException
from routes.api_v1.management._router import router
from routes.http_response.responses import ResponseMessage
from usecases.management.delete_object import DeleteObject

@router.delete(
    "/delete-object",
    status_code=200,
    responses={
        **ResponseMessage.HTTP_200_OK("Object deleted successfully", dict),
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    },
    description="Delete customer or subscription with id",
)
async def delete_object(
    object_id: str,
):
    try:
        delete_item_usecase = DeleteObject()
        return delete_item_usecase.execute(object_id)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
        

    