from fastapi import APIRouter
from ..schemas import CreateUser


router = APIRouter()


@router.post('/register')
async def create(user: CreateUser ):
    return user