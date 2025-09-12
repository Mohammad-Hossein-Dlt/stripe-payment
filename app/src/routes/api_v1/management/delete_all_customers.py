from ._router import router
from fastapi import HTTPException
from app.src.routes.http_response.responses import ResponseMessage
from app.src.usecases.management.delete_all_customers import DeleteAllCustomers

@router.delete(
    "/delete-all-customers",
    status_code=200,
    responses={
        **ResponseMessage.HTTP_200_OK("All customers deleted successfully", dict),
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    },
    description="Delete all customers with their subscription. use for testing purposes only",
)
async def delete_all_customers():
    try:
        delete_all_customers_usecase = DeleteAllCustomers()
        return delete_all_customers_usecase.execute()
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

        

    