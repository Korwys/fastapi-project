import fastapi
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from db.db_setup import async_get_db, get_db
from schemas import courses_schemas
from services.crud.crud_courses import course

router = fastapi.APIRouter()


@router.post('/', response_model=courses_schemas.Course)
async def create(section: courses_schemas.CourseCreate, db: AsyncSession = Depends(async_get_db)):
    return await course.create(db=db, obj_in=section)


@router.get('/', response_model=list[courses_schemas.Course])
async def get_list_of_sections(db: AsyncSession = Depends(get_db)):
    return course.get_multi(db=db)


@router.get('/{section_id}', response_model=courses_schemas.Course)
async def get_retrieve_section(id: int, db: AsyncSession = Depends(get_db)):
    return course.get(db=db, id=id)


@router.put('/{section_id}', response_model=courses_schemas.Course)
async def update_section(id: int, obj_in: courses_schemas.CourseUpdate, db: Session = Depends(get_db)):
    return course.update(db=db, db_obj=course.get(db=db, id=id), obj_in=obj_in)


@router.delete('/{section_id}', response_model=courses_schemas.Course)
async def delete(id: int, db: AsyncSession = Depends(async_get_db)):
    return await course.remove(db=db, id=id)





