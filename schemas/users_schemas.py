from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    # is_active: Optional[bool] = True
    # is_superuser: Optional[bool] = False


class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    ...


class UserInDBBAse(UserBase):
    class Config:
        orm_mode = True


class User(UserInDBBAse):
    ...
