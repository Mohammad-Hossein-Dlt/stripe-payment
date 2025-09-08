from fastapi import Request, Depends, HTTPException
from routes.api_v1.payment._router import router
from routes.http_response.responses import ResponseMessage
from repo.interface.Isubscription import ISubscriptionRepo
from routes.depends.subscription_repo_depend import get_subscription_repo
from usecases.payment.success import SuccessPayment
from infra.fastapi_config.app import templates

@router.get(
    "/success",
    status_code=200,
    responses={
        **ResponseMessage.HTTP_200_OK("Payment successful and subscription created and stored in the database"),
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    },
    description="Handle successful payment webhook(callback) and display subscription details and store them in the database"
)
async def success_payment(
    request: Request,
    session_id: str = None,
    sub_repo: ISubscriptionRepo = Depends(get_subscription_repo),
):
    try:
        success_payment_usecase = SuccessPayment(sub_repo)
        subscription = await success_payment_usecase.execute(session_id)
        return templates.TemplateResponse("success_payment.html", {"request": request, "subscription": subscription})
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))


