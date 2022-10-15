from datetime import datetime
from pydantic import BaseModel


class CourseBase(BaseModel):
    title: str | None
    description: str | None
    user_id: int | None


class CourseCreate(CourseBase):
    ...


class CourseUpdate(CourseBase):
    title: str


class CourseInDBBase(CourseBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class Course(CourseInDBBase):
    pass
