from fastapi import HTTPException
from routes.api_v1.get_object._router import router
from routes.http_response.responses import ResponseMessage
from usecases.get_object.get_products import GetProducts

@router.get(
    "/get-products",
    status_code=200,
    responses={
        **ResponseMessage.HTTP_200_OK("Products retrieved successfully", list),
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    },
    description="Get all products"
)
async def get_products():
    try:
        get_products_usecase = GetProducts()
        return get_products_usecase.execute()
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

        