from sys import prefix
from fastapi import FastAPI
from routers import service

app = FastAPI()
app.include_router(service.router, prefix='/services', tags=["service"])

@app.get("/")
def read_root():
    return {"Hello": "World"}