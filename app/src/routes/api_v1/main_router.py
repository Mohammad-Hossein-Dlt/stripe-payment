from fastapi import APIRouter
from .product._router import router as product_router
from .customer._router import router as customer_router
from .subscription._router import router as subscription_router
from .payment._router import router as payment_router

ROUTE_PREFIX_VERSION_API = "/api_v1"

main_router_v1 = APIRouter()

main_router_v1.include_router(product_router, prefix=ROUTE_PREFIX_VERSION_API)
main_router_v1.include_router(customer_router, prefix=ROUTE_PREFIX_VERSION_API)
main_router_v1.include_router(subscription_router, prefix=ROUTE_PREFIX_VERSION_API)
main_router_v1.include_router(payment_router, prefix=ROUTE_PREFIX_VERSION_API)