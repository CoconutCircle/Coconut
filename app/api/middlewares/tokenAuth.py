from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from typing import Optional
from app.core.config import settings

app = FastAPI()

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"

# Define the HTTPBearer instance
security = HTTPBearer()

def get_current_user(authorization: HTTPAuthorizationCredentials = Depends(security)):
    try:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        token = authorization.credentials
        
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
     
        return {"email": email} # Return user email or user object if needed
    except JWTError:
        raise credentials_exception
    