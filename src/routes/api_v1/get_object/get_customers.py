from fastapi import HTTPException
from routes.api_v1.get_object._router import router
from routes.http_response.responses import ResponseMessage
from usecases.get_object.get_customers import GetCustomers

@router.get(
    "/get-customers",
    status_code=200,
    responses={
        **ResponseMessage.HTTP_200_OK("Customers retrieved successfully", list),
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    },
    description="Get all customers"
)
async def get_customers():
    try:
        get_customers_usecase = GetCustomers()
        return get_customers_usecase.execute()
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

        