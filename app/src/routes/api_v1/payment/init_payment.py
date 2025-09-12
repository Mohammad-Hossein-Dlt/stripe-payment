from ._router import router
from fastapi import Request, HTTPException
from app.src.routes.http_response.responses import ResponseMessage
from app.src.usecases.get_object.get_customers import GetCustomers
from app.src.usecases.get_object.get_products import GetProducts
from app.src.infra.fastapi_config.template_engine import templates

@router.get(
    "/init-payment",
    status_code=201,
    responses={
        **ResponseMessage.HTTP_201_CREATED("Payment page initialized successfully", dict),
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    },
    description="Initialize payment with assigning email and price of the product. If the email is not assigned here, it will be assigned on the payment page"
)
async def init_payment(
    request: Request,
):
    
    try:
        get_customers_usecase = GetCustomers()
        customers = get_customers_usecase.execute()
        
        get_products_usecase = GetProducts()
        product = get_products_usecase.execute()
        
        return templates.TemplateResponse("init_payment.html", {"request": request, "products": product, "customers": customers})
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
    