from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import register, login, journal, trade
from . import model
from .database import engine


#creates tables/models in the database
model.Base.metadata.create_all(bind=engine)

app = FastAPI()

#CORS
origins = [
    "https://heroku.app.com",   #TODO insert frontend domains
    ]    

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(register.router)
app.include_router(login.router)
app.include_router(journal.router)
app.include_router(trade.router)

@app.get('/test')
async def test():
    return {'msg': 'API is online'}

