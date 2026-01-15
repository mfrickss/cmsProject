from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.post import Post
from app.schemas.post import PostCreate

class CRUDPost(CRUDBase[Post]):
    def create_with_owner(self, db: Session, *, obj_in: PostCreate, owner_id: int) -> Post:
        # Converte o schema Pydantic para um dicionário
        obj_in_data = obj_in.model_dump() 
        
        # Cria o objeto do banco, misturando os dados do post com o ID do dono
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        
        return db_obj

crud_post = CRUDPost(Post)