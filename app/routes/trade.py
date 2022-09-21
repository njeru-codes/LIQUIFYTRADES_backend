from fastapi import APIRouter, Depends, status, HTTPException
from ..schemas import Trade
from ..database import get_db
from .. import model
from sqlalchemy.orm import Session
from ..auth import get_current_user

router = APIRouter()


@router.get('/trade')
async def get_trades( db: Session=Depends(get_db), user_id:int =Depends(get_current_user) ):
    trades = db.query(model.Trade).filter(model.user_id == user_id).all()
    return trades

@router.post('/trade')
async def create_trade(trade: Trade, db: Session=Depends(get_db),  user_id:int =Depends(get_current_user) ):
    trade.user_id == user_id
    new_trade = model.Trade( **trade.dict() )
    db.add( new_trade)  
    db.commit()
    db.refresh(new_trade)
    return new_trade


@router.get('/trade/{trade_id}')
async def get_trade(trade_id:int, db: Session=Depends(get_db), user_id:int =Depends(get_current_user) ):
    trade = db.query(model.Trade).filter(model.Trade.user_id == user_id, model.Trade.id == trade_id)
    if not trade:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'trade with id {trade_id} does not exist')
    return trade

@router.put('/trade/{trade_id}')    #TODO edit update trade route
async def update_trade(trade_id:int , db: Session=Depends(get_db), user_id:int =Depends(get_current_user)):
    return f'trade with id {trade_id} was updated ' 

@router.delete('/trade/{trade_id}')
async def delete_journal(trade_id:int , db: Session=Depends(get_db),  user_id:int =Depends(get_current_user)):
    trade = db.query(model.Trade).filter(model.Trade.id = trade_id)
    if not trade:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'trade with id {trade_id} does not exist')

    if trade.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'trade with id {trade_id} does not exist')
    
    #delete trade from DB
    db.delete( model.Trade).filter( model.Trade.id= trade_id)
    return {f"trade with id {trade_id} deleted"}

