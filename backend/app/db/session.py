from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session 
from sqlalchemy.ext.declarative import declarative_base
from typing import Generator


from app.core.config import settings


try:
    engine = create_engine(
        settings.DATABASE_URL,
        echo=False,
        pool_pre_ping=True
    )

    SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
    Base = declarative_base()

except Exception as e:
    print(f"Erro ao conectar ao banco: {e}")
    raise

def get_db() -> Generator[Session, None, None]:
    """Dependency para obter a sessão do db."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
