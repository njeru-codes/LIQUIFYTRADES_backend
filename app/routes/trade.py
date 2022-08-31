from fastapi import APIRouter
from ..schemas import Trade

router = APIRouter()


@router.get('/trade')
async def get_trades():
    return

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