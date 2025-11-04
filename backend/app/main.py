from fastapi import FastAPI
app = FastAPI(title="Meu CMS API")

@app.get("/")
def read_root():
    return {"Hello": "World", "message": "API está rodando!"}