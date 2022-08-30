from pydantic import BaseModel, EmailStr
from typing import Optional


class User(BaseModel):
    email: EmailStr 
    password: str
    class Config:
        orm_mode = True

class Journal(BaseModel):
    date: str
    user_id: Optional[str]=None

class Trade(BaseException):
    symbol: str
    open_time: str 
    close_time: str
    open_price: float
    close_price: float
    stop_loss: float
    take_profit: float
    date: str 
    notes: str
    journal_id: Optional[str] =None
    