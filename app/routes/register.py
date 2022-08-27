from fastapi import APIRouter
from ..schemas import User


router = APIRouter()


@router.post('/register')
async def create(user: User ):
    #check email if exists
    #register user
    #send email validation link & welcome message  to address
    return user