import fastapi
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from db.db_setup import async_get_db, get_db
from schemas import contentblock_schemas
from services.crud.crud_contentblocks import contentblock

router = fastapi.APIRouter()


@router.post('/', response_model=contentblock_schemas.ContentBlock)
async def create(section: contentblock_schemas.ContentBlockCreate, db: AsyncSession = Depends(async_get_db)):
    return await contentblock.create(db=db, obj_in=section)


@router.get('/', response_model=list[contentblock_schemas.ContentBlock])
async def get_list_of_sections(db: AsyncSession = Depends(get_db)):
    return contentblock.get_multi(db=db)


@router.get('/{section_id}', response_model=contentblock_schemas.ContentBlock)
async def get_retrieve_section(id: int, db: AsyncSession = Depends(get_db)):
    return contentblock.get(db=db, id=id)


@router.put('/{section_id}', response_model=contentblock_schemas.ContentBlock)
async def update_section(id: int, obj_in: contentblock_schemas.ContentBlockUpdate, db: Session = Depends(get_db)):
    return contentblock.update(db=db, db_obj=contentblock.get(db=db, id=id), obj_in=obj_in)


@router.delete('/{section_id}', response_model=contentblock_schemas.ContentBlock)
async def delete(id: int, db: AsyncSession = Depends(async_get_db)):
    return await contentblock.remove(db=db, id=id)
