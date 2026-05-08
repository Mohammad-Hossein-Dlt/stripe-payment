from ._router import router
from fastapi import HTTPException
from src.routes.http_response.responses import ResponseMessage
from src.usecases.customer.get_all import GetCustomers

@router.get(
    "/all",
    status_code=200,
    responses={
        **ResponseMessage.HTTP_200_OK("Customers retrieved successfully", list),
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    },
    description="Get all customers"
)
async def get_all():
    try:
        get_customers_usecase = GetCustomers()
        return get_customers_usecase.execute()
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

        