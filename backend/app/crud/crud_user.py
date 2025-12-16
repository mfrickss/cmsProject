from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase

class CRUDUser(CRUDBase[User]):
    def __init__(self):
        super().__init__(User)

    def get_by_email(self, db: Session, email: str) -> User | None:
        """Busca um usuário pelo email."""
        return db.query(self.model).filter(self.model.email == email).first()
    
    def create_user(self, db: Session, user: UserCreate) -> User: 
        """Cria um novo usuário com senha hasheada."""

        hashed_password = get_password_hash(user.password)

        db_user = User(
            email=user.email,
            name=user.name,
            age=user.age,
            hashed_password=hashed_password
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user
    
    def authenticate(self, db: Session, email: str, password: str) -> User | None:
        """Autentica o usuário verificando email e senha."""

        user = self.get_by_email(db, email)

        if not User:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        
        return user
    
crud_user = CRUDUser()