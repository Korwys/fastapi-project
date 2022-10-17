from db.models.courses import Course, StudentCourse
from schemas.studen_course_schemas import StudentCourseCreate, StudentCourseUpdate
from services.crud.base import CRUDBase


class CRUDStudentCourses(CRUDBase[StudentCourse, StudentCourseCreate, StudentCourseUpdate]):
    """Класс наследует все методы CREATE,READ,UPDATE,DELETE. Реализует CRUD операции над моделью StudenCourse"""
    ...


scourse = CRUDStudentCourses(StudentCourse)
