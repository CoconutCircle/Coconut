from fastapi import APIRouter
from app.api.routes.user import router as user_router
from app.api.routes.auth import router as auth_router


api_router = APIRouter()
api_router.include_router(auth_router, prefix="/auth", tags=["Auth"])
api_router.include_router(user_router, prefix="/user", tags=["User"])