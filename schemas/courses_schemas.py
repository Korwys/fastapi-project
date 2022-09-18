from datetime import datetime

from pydantic import BaseModel


class CourseBase(BaseModel):
    title: str
    description: str | None
    user_id: int


class CreateCourse(CourseBase):
    ...


class Course(CourseBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
