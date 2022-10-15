import fastapi
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from db.db_setup import async_get_db, get_db
from schemas import sections_schemas
from services.crud.crud_sections import sections

router = fastapi.APIRouter()


@router.post('/', response_model=sections_schemas.Section)
async def create(section: sections_schemas.CreateSection, db: AsyncSession = Depends(async_get_db)):
    return await sections.create(db=db, obj_in=section)


@router.get('/', response_model=list[sections_schemas.Section])
async def get_list_of_sections(db: AsyncSession = Depends(get_db)):
    return sections.get_multi(db=db)


@router.get('/{section_id}', response_model=sections_schemas.Section)
async def get_retrieve_section(id: int, db: AsyncSession = Depends(get_db)):
    return sections.get(db=db, id=id)


@router.put('/{section_id}', response_model=sections_schemas.Section)
async def update_section(id: int, obj_in: sections_schemas.SectionUpdate, db: Session = Depends(get_db)):
    return sections.update(db=db, db_obj=sections.get(db=db, id=id), obj_in=obj_in)


@router.delete('/{section_id}', response_model=sections_schemas.Section)
async def delete(id: int, db: AsyncSession = Depends(async_get_db)):
    return await sections.remove(db=db, id=id)
