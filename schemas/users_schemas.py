from datetime import datetime

from pydantic import BaseModel, EmailStr

from db.models.users import Role


class UserBase(BaseModel):
    email: EmailStr
    password: str


class UserCreate(UserBase):
    ...


class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
