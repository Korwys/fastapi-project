from pydantic import BaseModel


class BaseStudentCourse(BaseModel):
    student_id: int | None
    course_id: int | None


class CreateStudentCourse(BaseStudentCourse):
    ...


class StudentCourse(BaseStudentCourse):
    id: int

    class Config:
        orm_mode = True
