import datetime
from fastapi import APIRouter, HTTPException

from datetime import datetime as dt, timezone
from jose import jwt
from app.api.deps import SessionDep
from app.core.config import settings
from app.crud import users
from app.models import User
from app.schemas.users import Token
import google.oauth2.id_token
from google.auth.transport import requests as google_requests

router = APIRouter()

# Secret key to encode and decode JWT tokens
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 300
CLIENT_ID = settings.CLIENT_ID



# Function to create access token
def create_access_token(data: dict, expires_delta: datetime.timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = dt.now(timezone.utc) + expires_delta
    else:
        expire = dt.now(timezone.utc) + datetime.timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)    
    return encoded_jwt


@router.post('/', description="send id_token from google auth in payload")
async def auth(id_token:Token,session: SessionDep):
    google_token = id_token.id_token
    if not google_token:
        raise HTTPException(status_code=400, detail="Token not provided")
    try:
        id_info = google.oauth2.id_token.verify_oauth2_token(google_token, google_requests.Request(), CLIENT_ID)
        user_email = id_info.get('email')
            
        
        user = users.get_user_by_email(
        session=session, email=user_email)
        if not user:
            user = User(email=user_email)
            session.add(user)
            session.commit()
            session.refresh(user)
        
        
        access_token_expires = datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.inst_email, "is_onboarded": user.is_onboarded}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer",  "is_onboarded":user.is_onboarded}
    except ValueError as e:
        raise HTTPException(status_code=400, detail="Invalid token")

