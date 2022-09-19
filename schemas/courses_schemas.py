from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CourseBase(BaseModel):
    title: str | None
    description: str | None
    user_id: int | None


class CreateCourse(CourseBase):
    ...


class Course(CourseBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
