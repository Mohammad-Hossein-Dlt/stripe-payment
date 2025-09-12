from fastapi import APIRouter

router = APIRouter(
    prefix="/get_object",
    tags=["Get customers ans products"]
)