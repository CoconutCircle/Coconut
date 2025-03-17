
from fastapi import APIRouter, HTTPException
from datetime import datetime as dt, timezone
import datetime
from jose import jwt
from app.schemas.users import UserCreate
from app.api.deps import SessionDep
from app.core.config import settings
from app.crud.users import create_user,get_user_by_email

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"


router = APIRouter()

def create_access_token(data: dict, expires_delta: datetime.timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = dt.now(timezone.utc) + expires_delta
    else:
        expire = dt.now(timezone.utc) + datetime.timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post("/signup")
async def signup(user: UserCreate, session: SessionDep):
    db_user = get_user_by_email(session=session,email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = create_user(session=session,user_create=user)
    access_token_expires = datetime.timedelta(minutes=15)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
    
    