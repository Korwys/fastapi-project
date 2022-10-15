from db.models.courses import Course
from schemas.courses_schemas import CourseUpdate, CourseCreate
from services.crud.base import CRUDBase


class CRUDCourses(CRUDBase[Course, CourseCreate, CourseUpdate]):
    ...


course = CRUDCourses(Course)
