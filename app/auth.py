from jose import jwt, JWTError
from datetime import datetime , timedelta
from fastapi import HTTPException, Depends,  status
from fastapi.security import OAuth2PasswordBearer
from os import environ

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")     #TODO recheck functionality


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta( minutes=90000000 )      #TODO store exp_minutes in env vars
    to_encode.update( {"exp": expire } )
    return jwt.encode(to_encode, environ.get('SECRET_KEY'), algorithm='HS256' )


def verify_access_token(token: str, credentials_exception):
    try:
        payload =jwt.decode(token, environ.get('SECRET_KEY') )
        user_id:str = payload.get("user_id")
        if id is None: 
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return user_id

def get_current_user(token :str=Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,
    detail= "could not validate credentials", headers={"WWW-Authenticate": "Bearer "})
    return verify_access_token(token, credentials_exception)