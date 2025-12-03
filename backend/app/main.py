from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone
from typing import Annotated
from . import database, models, schemas, crud, auth


app = FastAPI(title="Meu CMS")

@app.get("/")
def read_root():
    return {"Hello": "World", "message": "API do sexo está rodando!"}

@app.post("/register")
def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")
    
    return crud.create_user(db=db, user=user)

@app.post("/token", response_model=schemas.Token)
def login_for_acess_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        db: Session = Depends(database.get_db)
):
    """
    Endpoint de Login (OAuth2 standard).
    Recebe 'username' e 'password' num formulário.
    Retorna o Token JWT se as credenciais forem válidas.
    """

    user = crud.get_user_by_email(db=db, email=form_data.username)

    if not user or not crud.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Nome de Usuário ou Senha incorreto.",
            headers={"WWW.Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_acess_token(
        data={"sub": user.email},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me", response_model=schemas.UserOut)
def read_users_me(current_user: Annotated[models.User, Depends(auth.get_current_user)]):
    """
    Retorna os dados do utilizador logado.
    Só funciona se o request tiver o cabeçalho 'Authorization: Bearer <token>'
    """
    return current_user