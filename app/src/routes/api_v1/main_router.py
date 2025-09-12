from fastapi import APIRouter
from .get_object._router import router as get_object_router
from .management._router import router as management_router
from .payment._router import router as payment_router

ROUTE_PREFIX_VERSION_API = "/api_v1"

main_router_v1 = APIRouter()

main_router_v1.include_router(get_object_router, prefix=ROUTE_PREFIX_VERSION_API)
main_router_v1.include_router(management_router, prefix=ROUTE_PREFIX_VERSION_API)
main_router_v1.include_router(payment_router, prefix=ROUTE_PREFIX_VERSION_API)