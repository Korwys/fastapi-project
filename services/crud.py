from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from db.models.courses import Course
from db.models.user import User
from schemas import courses_schemas
from schemas.users_schemas import CreateUser


async def create_new_user(db: AsyncSession, user: CreateUser):
    db_user = User(email=user.email, role=user.role)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def users_list(db: AsyncSession, skip: int = 0, limit: int = 5):
    return db.query(User).offset(skip).limit(limit).all()


async def single_user(db: AsyncSession, user_id: int):
    query = select(User).where(User.id == user_id)
    sel = await db.execute(query)
    return sel.scalar_one_or_none()


async def delete_select_user(db: AsyncSession, user_id: int):
    user = delete(User).where(User.id == user_id)
    await db.execute(user)
    await db.commit()
    return JSONResponse(content={'Message': 'User deleted'})


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
