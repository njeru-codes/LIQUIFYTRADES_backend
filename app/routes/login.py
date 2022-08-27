from fastapi import APIRouter
from ..schemas import User

router = APIRouter()



@router.post('/login')
async def login(user: User):
    return user 