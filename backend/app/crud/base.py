from sqlalchemy.orm import Session
from typing import TypeVar, Generic, Type, Optional, List

T = TypeVar('T')

class CRUDBase(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model
    
    def get(self, db: Session, id: int) -> Optional[T]:
        return db.query(self.model).filter(self.model.id == id).first()
    
    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[T]:
        return db.query(self.model).offset(skip).limit(limit).all()
    
    def crate(self, db: Session, obj_in: dict) -> T:
        db_obj = self.model(**obj_in)
        db.add(db_obj)
        db.commit()
        db.refresh()
        return db_obj
    
    def update(self, db: Session, db_obj: T, obj_in: dict) -> T:
        update_data = obj_in if isinstance(obj_in, dict) else obj_in.dict(exclude_unset=True)

        for field in update_data:
            setattr(db_obj, field, update_data[field])

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        return db_obj
    
    def delete(self, db: Session, id: int) -> None:
        obj = db.query(self.model).filter(self.model.id == id).first()
        if obj :
            db.delete(obj)
            db.commit()