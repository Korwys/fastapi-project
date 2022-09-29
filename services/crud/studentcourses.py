from sqlalchemy import delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from starlette.responses import JSONResponse

from db.models.courses import Course, StudentCourse
from schemas import courses_schemas, studen_course_schemas


async def new_student(db: AsyncSession, course: studen_course_schemas.CreateStudentCourse):
    db_course = StudentCourse(student_id=course.student_id, course_id=course.course_id)
    db.add(db_course)
    await db.commit()
    await db.refresh(db_course)
    return db_course


async def list_of_student_on_courses(db: AsyncSession):
    return db.query(StudentCourse).all()


async def select_student(db: AsyncSession, student_id: int):
    student_info = await db.execute(select(StudentCourse).where(StudentCourse.student_id == student_id))
    return student_info.scalar_one_or_none()


async def delete_selected_student(student_id: int, db: AsyncSession):
    studentcourse = delete(StudentCourse).where(StudentCourse.student_id == student_id)
    await db.execute(studentcourse)
    await db.commit()
    return JSONResponse(status_code=200, content={'Message': 'Info deleted'})


async def edit_studentcourse_info(student_id: int, course: studen_course_schemas.BaseStudentCourse, db: AsyncSession):
    obj_in = course.dict(exclude_unset=True)
    course_update = update(StudentCourse).where(StudentCourse.student_id == student_id).values(**obj_in)
    await db.execute(course_update)
    await db.commit()
    return course
