from ._router import router
from fastapi import HTTPException
from src.routes.http_response.responses import ResponseMessage
from src.usecases.product.get_all import GetProducts

@router.get(
    "/all",
    status_code=200,
    responses={
        **ResponseMessage.HTTP_200_OK("Products retrieved successfully", list),
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    },
    description="Get all products"
)
async def get_all():
    try:
        get_products_usecase = GetProducts()
        return get_products_usecase.execute()
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

        