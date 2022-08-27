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
async def get_trade(id: trade_id):
    return

@router.put('/trade/{trade_id}')
async def update_trade(id: trade_id):
    return

@router.delete('/trade/{trade_id}')
async def delete_journal(id:trade_id):
    return