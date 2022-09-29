import fastapi
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.db_setup import async_get_db, get_db
from schemas import sections_schemas
from services.crud.sections import new_section, section_list, get_section, delete_section

router = fastapi.APIRouter()


@router.post('/sections', response_model=sections_schemas.Section)
async def create_section(section: sections_schemas.CreateSection, db: AsyncSession = Depends(async_get_db)):
    return await new_section(db=db, section=section)


@router.get('/sections', response_model=list[sections_schemas.Section])
async def get_list_of_sections(db: AsyncSession = Depends(get_db)):
    return await section_list(db=db)


@router.get('/sections/{section_id}', response_model=sections_schemas.Section)
async def get_retrieve_section(section_id: int, db: AsyncSession = Depends(async_get_db)):
    return await get_section(section_id=section_id, db=db)


@router.delete('/sections/{section_id}', response_model=sections_schemas.Section)
async def delete_selected_course(section_id: int, db: AsyncSession = Depends(async_get_db)):
    return await delete_section(section_id=section_id, db=db)
