import fastapi
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from db.db_setup import async_get_db, get_db
from db.models.courses import StudentCourse
from schemas import studen_course_schemas, users_schemas
from services.crud.crud_studentcourses import scourse
from services.security import get_current_user

router = fastapi.APIRouter()


@router.post('/', response_model=studen_course_schemas.StudentCourse)
async def create_studentcourse(section: studen_course_schemas.StudentCourseCreate,
                               db: AsyncSession = Depends(async_get_db),
                               user: users_schemas.User = Depends(get_current_user)) -> StudentCourse:
    return await scourse.create(db=db, obj_in=section)


@router.get('/', response_model=list[studen_course_schemas.StudentCourse])
async def fetch_list_of_studentcourses(db: AsyncSession = Depends(get_db),
                                       user: users_schemas.User = Depends(get_current_user)) -> list[StudentCourse]:
    return scourse.get_multi(db=db)


@router.get('/{studentcourse_id}', response_model=studen_course_schemas.StudentCourse)
async def fetch_studentcourse(id: int, db: AsyncSession = Depends(get_db),
                              user: users_schemas.User = Depends(get_current_user)) -> StudentCourse:
    return scourse.get(db=db, id=id)


@router.put('/{studentcourse_id}', response_model=studen_course_schemas.StudentCourse)
async def update_studentcourse(id: int, obj_in: studen_course_schemas.StudentCourseUpdate,
                               db: Session = Depends(get_db),
                               user: users_schemas.User = Depends(get_current_user)) -> StudentCourse:
    return scourse.update(db=db, db_obj=scourse.get(db=db, id=id), obj_in=obj_in)


@router.delete('/{studentcourse_id}', response_model=studen_course_schemas.StudentCourse)
async def delete_studentcourse(id: int, db: AsyncSession = Depends(async_get_db),
                               user: users_schemas.User = Depends(get_current_user)) -> JSONResponse:
    return await scourse.remove(db=db, id=id)
