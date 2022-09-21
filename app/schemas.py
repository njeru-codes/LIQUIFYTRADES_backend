from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, time


class User(BaseModel):
    email: EmailStr 
    password: str
    class Config:
        orm_mode = True

class Journal(BaseModel):
    date: date
    user_id: Optional[str]=None
    class Config:
        orm_mode = True

class Trade(BaseModel):
    user_id: Optional[str] = None
    symbol: str
    open_time: time 
    close_time: time
    entry_price: float
    close_price: float
    stop_loss: float
    take_profit: float
    date: date 
    notes: str  #TODO :trim input
    journal_id: str
    class Config:
        orm_mode = True

    

    