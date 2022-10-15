from db.models.courses import Course, StudentCourse
from schemas.studen_course_schemas import StudentCourseCreate, StudentCourseUpdate
from services.crud.base import CRUDBase


class CRUDStudentCourses(CRUDBase[StudentCourse, StudentCourseCreate, StudentCourseUpdate]):
    ...


scourse = CRUDStudentCourses(StudentCourse)
