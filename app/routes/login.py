from fastapi import APIRouter, Depends, HTTPException, status
from ..schemas import User
from .. import model, utils
from ..database import get_db
from sqlalchemy.orm import Session
from ..auth import create_access_token

router = APIRouter()



@router.post('/login')
async def login(user: User, db: Session=Depends(get_db)):
    user_db = db.query( model.User).filter( model.User.email== user.email).first()
    print(user_db)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"{user.email} email does not exists")
    if not utils.verify_password( user.password, user_db.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='wrong password')
    
    access_token = create_access_token( data={"user_id": user_db.id})
    return { "access_token": access_token, "token_type": "bearer"}
    