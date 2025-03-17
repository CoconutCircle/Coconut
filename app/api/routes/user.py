
from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime as dt, timezone
from app.api.deps import SessionDep
from app.core.config import settings
from app.crud.users import get_user_by_email
from app.models.users import User
from app.api.middlewares.token_authorization import get_current_user

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"


router = APIRouter()


@router.get("/profile")
async def getProfile(session: SessionDep, current_user: str = Depends(get_current_user))->User:
    user = get_user_by_email(
        session=session, email=current_user['email'])
    return user
    
    
    