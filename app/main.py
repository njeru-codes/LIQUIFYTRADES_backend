from fastapi import FastAPI
from .routes import register

app = FastAPI()


app.include_router(register.router)

@app.get('/test')
async def test():
    return {'msg': 'API is online'}

