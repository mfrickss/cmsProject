from sqlalchemy.orm import Session
from passlib.context import CryptContext
from . import models, schemas

pwd_context = CryptContext(schemes=["bcrypy"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_user_by_email(db: Session, email: str) -> models.User | None:
    """
    Busca um usuário no banco de dados pelo email.
    
    - db.query(models.User): Cria um 'SELECT * FROM users...'
    - .filter(models.User.email == email): Adiciona o 'WHERE email = ...'
    - .first(): Executa a query e retorna o primeiro resultado (ou None)
    """
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    """
    Cria um novo usuário no banco de dados.
    """
    # 1. **FAZ O HASH DA SENHA**
    hashed_password_from_passlib = get_password_hash(user.password)

    # 2. Cria a instância do modelo SQLAlchemy
    db_user = models.User(
        email=user.email,
        name=user.name,
        age=user.age,
        hashed_password=hashed_password_from_passlib
        # 'is_active' usará o valor default=True do seu models.py
    )


    # 3. db.add(): Adiciona o objeto 'db_user' à sessão.
    #  Não foi salvo no banco ainda.
    db.add(db_user)

    # 4. db.commit(): "Fecha a compra". Executa o INSERT no banco de dados.
    db.commit()

    # 5. db.refresh(): Atualiza o objeto 'db_user' com os dados do banco.
    #    Isso é útil para pegar o 'id' que o banco acabou de gerar.
    db.refresh(db_user)

    return db_user