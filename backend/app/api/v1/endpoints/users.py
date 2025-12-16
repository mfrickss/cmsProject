from typing import Annotated
from fastapi import APIRouter, Depends
from app.schemas.user import UserOut
from app.models.user import User
from app.api.deps import get_current_user

router = APIRouter()

@router.get("/me", response_model=UserOut)
def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    """Retorna os dados do utilizador logado."""
    return current_user