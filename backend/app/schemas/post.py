from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from app.schemas.user import UserOut

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class PostOut(PostBase):
    id: int
    owner_id: int
    owner: UserOut

    model_config = ConfigDict(from_attributes=True)