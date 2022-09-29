from sqlalchemy import delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from starlette.responses import JSONResponse

from db.models.courses import Course
from schemas import courses_schemas


async def new_course(db: AsyncSession, course: courses_schemas.CreateCourse):
    db_course = Course(title=course.title, description=course.description, user_id=course.user_id)
    db.add(db_course)
    await db.commit()
    await db.refresh(db_course)
    return db_course


async def list_of_courses(db: AsyncSession):
    return db.query(Course).all()


async def get_course(db: AsyncSession, course_id: int):
    course = await db.execute(select(Course).where(Course.id == course_id))
    return course.scalar_one_or_none()


async def delete_course(course_id: int, db: AsyncSession):
    course = delete(Course).where(Course.id == course_id)
    await db.execute(course)
    await db.commit()
    return JSONResponse(status_code=200, content={'Message': 'Course deleted'})


async def edit_course(course_id: int, course: courses_schemas.CourseBase, db: AsyncSession):
    obj_in = course.dict(exclude_unset=True)
    course_update = update(Course).where(Course.id == course_id).values(**obj_in)
    await db.execute(course_update)
    await db.commit()
    return course
