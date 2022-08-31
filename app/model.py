from .database import Base
from sqlalchemy import Column, Integer,String, Float, Boolean, Table
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.types import Date,ARRAY
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
    date =Column(String, nullable=False)        #TODO: change datatype to date
    user_id =Column(Integer, nullable=False)    #TODO: change to foreign key


class Trade(Base):
    __tablename__ = 'trade'
    id = Column(Integer, primary_key=True, nullable=False)
    journal_id = Column(Integer, nullable=False)    #TODO: change to foreign key
    symbol=Column(String, nullable=False)
    open_time = Column(Integer)     #TODO replace with time datatype
    close_time = Column(Integer )       #TODO replace with time datatype
    entry_price = Column(Integer )      #TODO change to float or double
    close_price = Column(Integer )      #TODO change to float or double
    stop_loss = Column(Integer )        #TODO change to float or double
    take_profit = Column(Integer )      #TODO change to float or double
    notes=Column(String)




