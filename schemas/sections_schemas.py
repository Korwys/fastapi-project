from datetime import datetime

from pydantic import BaseModel


class BaseSection(BaseModel):
    title: str
    description: str
    course_id: int


class CreateSection(BaseSection):
    ...


class SectionUpdate(BaseSection):
    title: str


class SectionInDBBase(BaseSection):
    id: int
    course_id: int

    class Config:
        orm_mode = True


class Section(SectionInDBBase):
    pass
