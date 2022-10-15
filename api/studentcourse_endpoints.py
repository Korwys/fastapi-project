import fastapi
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from db.db_setup import async_get_db, get_db
from schemas import studen_course_schemas
from services.crud.crud_studentcourses import scourse

router = fastapi.APIRouter()


@router.post('/', response_model=studen_course_schemas.StudentCourse)
async def create(section: studen_course_schemas.StudentCourseCreate, db: AsyncSession = Depends(async_get_db)):
    return await scourse.create(db=db, obj_in=section)


@router.get('/', response_model=list[studen_course_schemas.StudentCourse])
async def get_list_of_sections(db: AsyncSession = Depends(get_db)):
    return scourse.get_multi(db=db)


@router.get('/{section_id}', response_model=studen_course_schemas.StudentCourse)
async def get_retrieve_section(id: int, db: AsyncSession = Depends(get_db)):
    return scourse.get(db=db, id=id)


@router.put('/{section_id}', response_model=studen_course_schemas.StudentCourse)
async def update_section(id: int, obj_in: studen_course_schemas.StudentCourseUpdate, db: Session = Depends(get_db)):
    return scourse.update(db=db, db_obj=scourse.get(db=db, id=id), obj_in=obj_in)


@router.delete('/{section_id}', response_model=studen_course_schemas.StudentCourse)
async def delete(id: int, db: AsyncSession = Depends(async_get_db)):
    return await scourse.remove(db=db, id=id)






