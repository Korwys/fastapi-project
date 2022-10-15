from pydantic import BaseModel


class StudentCourseBase(BaseModel):
    student_id: int | None
    course_id: int | None


class StudentCourseCreate(StudentCourseBase):
    ...


class StudentCourseUpdate(StudentCourseBase):
    ...


class StudentCourseInDBBase(StudentCourseBase):
    id: int

    class Config:
        orm_mode = True


class StudentCourse(StudentCourseInDBBase):
    pass
