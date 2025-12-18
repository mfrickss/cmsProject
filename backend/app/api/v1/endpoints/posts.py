from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Annotated
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_user
from app.models.user import User
from app.schemas.post import PostCreate, PostOut
from app.crud.crud_post import crud_post

router = APIRouter()

@router.get("/", response_model=List[PostOut])
def read_posts(
    db: Annotated[Session, Depends(get_db)],
    skip: int = 0,
    limit: int = 100
):
    """
    Lista todos os posts.
    Qualquer pessoa(logada ou não) pode ver.
    """
    posts = crud_post.get_all(db, skip=skip, limit=limit)
    return posts

@router.post("/", response_model=PostOut)
def create_post(
    db: Annotated[Session, Depends(get_db)],
    post_in: PostCreate,
    current_user: Annotated[User, Depends(get_current_user)]
):
    """
    Cria um novo post,
    Requer autenticação
    O post é automaticamente associado ao utilizador logado.
    """

    return crud_post.create_with_owner(
        db=db,
        obj_in=post_in,
        owner_id=current_user.id
    )

@router.delete("/{id}", response_model=PostOut)
def delete_post(
    *,
    db: Annotated[Session, Depends(get_current_user)],
    id: int, 
    current_user: Annotated[User, Depends(get_current_user)]
):
    """
    Apaga um post pelo ID.
    Somente o dono pode apagar.
    """
    post = crud_post.get(db=db, id=id)

    if not post:
        raise HTTPException(status_code=404, detail="Post não encontrado.")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Você não tem permissão para apagar esse post")

    crud_post.delete(db=db, id=id)

    return post
    