from datetime import datetime

from pydantic import BaseModel


class BaseSection(BaseModel):
    title: str
    description: str
    course_id: int


class CreateSection(BaseSection):
    ...


class Section(BaseSection):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
