from datetime import datetime

from pydantic import BaseModel


class BaseUser(BaseModel):
    email: str
    role: int


class CreateUser(BaseUser):
    ...


class User(BaseUser):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
