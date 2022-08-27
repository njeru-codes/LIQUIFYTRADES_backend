from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import register, login
from . import model
from .database import engine


#creates tables/models in the database
model.Base.metadata.create_all(bind=engine)

app = FastAPI()

#CORS
origins = [
    "https://heroku.app.com",
    ] #place your domain names here 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(register.router)
app.include_router(login.router)

@app.get('/test')
async def test():
    return {'msg': 'API is online'}

