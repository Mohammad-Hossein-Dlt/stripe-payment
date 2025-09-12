from ._router import router
from fastapi import Depends, HTTPException
from fastapi.responses import RedirectResponse
from app.src.routes.http_response.responses import ResponseMessage
from app.src.routes.depends.get_app_ports_depend import get_app_ports_depend
from app.src.usecases.payment.create_checkout_session import CreateCheckoutSession

@router.post(
    "/create-checkout-session",
    status_code=200,
    responses={
        **ResponseMessage.HTTP_200_OK("Checkout session created successfully"),
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    },
    description="Create payment link with assigning email and price of the product. If the email is not assigned here, it will be assigned on the payment page",
)
async def create_checkout_session(
    price_id: str,
    email: str | None = None,
    app_ports: tuple[int, int] = Depends(get_app_ports_depend)
) -> RedirectResponse:
    try:
        create_checkout_session_usecase = CreateCheckoutSession(app_ports[0])
        url = create_checkout_session_usecase.execute(price_id, email)
        return RedirectResponse(url=url, status_code=303)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
   