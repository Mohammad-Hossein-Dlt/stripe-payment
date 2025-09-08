from fastapi import APIRouter

router = APIRouter(
    prefix="/management",
    tags=["Manage customers and subscriptions"]
)