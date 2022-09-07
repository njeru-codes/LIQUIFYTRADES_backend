from fastapi import APIRouter, Depends, status
from ..schemas import Trade
from ..auth import get_current_user

router = APIRouter()


@router.get('/trade')
async def get_trades( user_id:int = Depends(get_current_user) ):
    return user_id

@router.post('/trade')
async def create_trade(trade: Trade):
    return trade

@router.get('/trade/{trade_id}')
async def get_trade(trade_id:int ):
    return

@router.put('/trade/{trade_id}')
async def update_trade(trade_id:int ):
    return

@router.delete('/trade/{trade_id}')
async def delete_journal(trade_id:int ):
    return