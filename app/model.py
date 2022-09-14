from .database import Base
from sqlalchemy import Column, Integer,String, Float
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.types import Date, Time
from sqlalchemy.orm import relationship



# Declare your database tables/models  here
class User(Base):
    __tablename__ ='user'
    id = Column(Integer, primary_key=True, nullable=False)
    email=Column(String, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text( 'NOW()') )

class Journal(Base):
    __tablename__ ='journal'
    id = Column(Integer, primary_key=True, nullable=False)
    date =Column(Date, nullable=False)
    user_id =Column(Integer, nullable=False)    #TODO: change to foreign key


class Trade(Base):
    __tablename__ = 'trade'
    id = Column(Integer, primary_key=True, nullable=False)
    journal_id = Column(Integer, nullable=False)    #TODO: change to foreign key
    user_id =Column(Integer, nullable=False)
    symbol=Column(String, nullable=False)
    open_time = Column(Time, nullable=False)
    close_time = Column( Time )     
    entry_price = Column(Float )
    close_price = Column(Float )
    stop_loss = Column(Float )
    take_profit = Column(Float )      
    notes=Column(String)




