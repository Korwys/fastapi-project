from db.models.courses import Course
from schemas.courses_schemas import CourseUpdate, CourseCreate
from services.crud.base import CRUDBase


class CRUDCourses(CRUDBase[Course, CourseCreate, CourseUpdate]):
    """Класс наследует все методы CREATE,READ,UPDATE,DELETE. Реализует CRUD операции над моделью Course"""
    ...


course = CRUDCourses(Course)
