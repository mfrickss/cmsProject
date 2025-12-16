from datetime import timedelta
from typing import Annotated

from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session 

from app.db.session import get_db
from app.schemas.token import Token
from app.schemas.user import UserCreate, UserBase, UserOut
from app.core.config import settings
from app.core.security import create_access_token
from app.crud.crud_user import crud_user
from app.api.deps import get_current_user

router = APIRouter(tags=["auth"])

@router.post("/register", response_model=UserOut)
def register(
    user: UserCreate,
    db: Annotated[Session, Depends(get_db)]
):
    """Registra um novo usuário."""
    db_user = crud_user.get_by_email(db, email=user.email)
    if db_user: 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="E-mail já cadastrado."
        )
    
    return crud_user.create_user(db=db, user=user)

@router.post("/token", response_model=Token)
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[Session, Depends(get_db)]
):
    """
    Endpoint de login.
    Recebe 'username' e 'password' num forms.
    Retorna token se credênciais válidas.
    """

    user = crud_user.authenticate(db=db, email=form_data.username, password=form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Nome de Usuário ou Senha incorreto.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email},
        expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me", response_model=UserOut)
def read_users_me(
    current_user: Annotated[UserOut, Depends(get_current_user)]
):
    """Retorna os dados do utilizador logado."""
    return current_user
