from fastapi import HTTPException
from routes.api_v1.management._router import router
from routes.http_response.responses import ResponseMessage
from usecases.management.create_customer import CreateCustomer

@router.post(
    "/create-customer",
    status_code=201,
    responses={
        **ResponseMessage.HTTP_201_CREATED("Customer created successfully", dict),
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    },
    description="Create customer with retrieved name and email or mock data"
)
async def create_customer(
    name: str | None = None,
    email: str | None = None,
):
    try:
        create_customer_usecase = CreateCustomer()
        return create_customer_usecase.execute(name, email)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

        