import fastapi
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.db_setup import async_get_db, get_db
from schemas import courses_schemas
from services.crud.courses import new_course, list_of_courses, get_course, delete_course, edit_course

router = fastapi.APIRouter()


@router.post('/courses', response_model=courses_schemas.Course)
async def create_course(course: courses_schemas.CreateCourse, db: AsyncSession = Depends(async_get_db)):
    return await new_course(db=db, course=course)


@router.get('/courses', response_model=list[courses_schemas.Course])
async def get_courses(db: AsyncSession = Depends(get_db)):
    return await list_of_courses(db=db)


@router.get('/courses/{course_id}', response_model=courses_schemas.Course)
async def get_retrieve_course(course_id: int, db: AsyncSession = Depends(async_get_db)):
    return await get_course(course_id=course_id, db=db)


@router.delete('/courses/{course_id}', response_model=courses_schemas.Course)
async def delete_selected_course(course_id: int, db: AsyncSession = Depends(async_get_db)):
    return await delete_course(course_id=course_id, db=db)


@router.put('/courses/{course_id}', response_model=courses_schemas.CourseBase)
async def edit_selected_course(course_id: int, course: courses_schemas.CourseBase,
                               db: AsyncSession = Depends(async_get_db)):
    return await edit_course(course_id=course_id, course=course, db=db)
