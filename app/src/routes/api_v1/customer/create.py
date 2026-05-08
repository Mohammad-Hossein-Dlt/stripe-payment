from ._router import router
from fastapi import Query
from fastapi import HTTPException
from src.routes.http_response.responses import ResponseMessage
from src.usecases.customer.create import CreateCustomer

@router.post(
    "/",
    status_code=201,
    responses={
        **ResponseMessage.HTTP_201_CREATED("Customer created successfully", dict),
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    },
    description="Create customer with retrieved name and email or mock data"
)
async def create(
    name: str | None = Query(None),
    email: str | None = Query(None),
):
    try:
        create_customer_usecase = CreateCustomer()
        return create_customer_usecase.execute(name, email)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

        