from fastapi import FastAPI
from app.api.v1.router import api_router

app = FastAPI(title="ricks.nexus")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # <--- 1. Importe isso

app = FastAPI()

# 2. Configure a lista de origens permitidas
origins = [
    "http://localhost:5173", # O endereço do seu React
    "http://localhost:3000",
]

# 3. Adicione o Middleware no App
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Libera GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],
)

# ... resto das suas rotas ...

@app.get("/")
def read_root():
    return {"Hello": "World", "message": "API Rodando!"}

app.include_router(api_router)