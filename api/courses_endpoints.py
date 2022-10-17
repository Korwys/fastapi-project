import fastapi
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from db.db_setup import async_get_db, get_db
from db.models.courses import Course
from schemas import courses_schemas, users_schemas
from services.crud.crud_courses import course
from services.security import get_current_user

router = fastapi.APIRouter()


@router.post('/', response_model=courses_schemas.Course)
async def create_course(section: courses_schemas.CourseCreate, db: AsyncSession = Depends(async_get_db),
                        user: users_schemas.User = Depends(get_current_user)) -> Course:
    return await course.create(db=db, obj_in=section)


@router.get('/', response_model=list[courses_schemas.Course])
async def fetch_list_of_course(db: AsyncSession = Depends(get_db)) -> list[Course]:
    return course.get_multi(db=db)


@router.get('/{course_id}', response_model=courses_schemas.Course)
async def fetch_course(id: int, db: AsyncSession = Depends(get_db)) -> Course:
    return course.get(db=db, id=id)


@router.put('/{course_id}', response_model=courses_schemas.Course)
async def update_course(id: int, obj_in: courses_schemas.CourseUpdate, db: Session = Depends(get_db),
                         user: users_schemas.User = Depends(get_current_user)) -> Course:
    return course.update(db=db, db_obj=course.get(db=db, id=id), obj_in=obj_in)


@router.delete('/{course_id}', response_model=courses_schemas.Course)
async def delete_course(id: int, db: AsyncSession = Depends(async_get_db),
                 user: users_schemas.User = Depends(get_current_user)) -> JSONResponse:
    return await course.remove(db=db, id=id)
