from fastapi import FastAPI
from api.v1.router import api_router

app = FastAPI(title="CMS")

@app.get("/")
def read_root():
    return {"Hello": "World", "message": "API Rodando!"}

app.include_router(api_router)