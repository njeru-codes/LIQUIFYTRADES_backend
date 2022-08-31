from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import model, utils
from ..database import get_db
from sqlalchemy.orm import Session
from ..auth import create_access_token

router = APIRouter()



@router.post("/login",  status_code=status.HTTP_200_OK)
async def login( db: Session=Depends(get_db), user_credentials: OAuth2PasswordRequestForm=Depends()  ):
    user = db.query( model.User).filter( model.User.email== user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"{user_credentials.username} email does not exists")
    if not utils.verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='wrong password')
    
    access_token = create_access_token( data={"user_id": user.id})
    return { "access_token": access_token, "token_type": "bearer"}
    