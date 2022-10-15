import fastapi
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from db.db_setup import async_get_db, get_db
from schemas import completeblock_schemas
from services.crud.crud_completeblocks import completedcb

router = fastapi.APIRouter()


@router.post('/', response_model=completeblock_schemas.CompletedContentBlock)
async def create(section: completeblock_schemas.CompletedContentBlockCreate, db: AsyncSession = Depends(async_get_db)):
    return await completedcb.create(db=db, obj_in=section)


@router.get('/', response_model=list[completeblock_schemas.CompletedContentBlock])
async def get_list_of_sections(db: AsyncSession = Depends(get_db)):
    return completedcb.get_multi(db=db)


@router.get('/{section_id}', response_model=completeblock_schemas.CompletedContentBlock)
async def get_retrieve_section(id: int, db: AsyncSession = Depends(get_db)):
    return completedcb.get(db=db, id=id)


@router.put('/{section_id}', response_model=completeblock_schemas.CompletedContentBlock)
async def update_section(id: int, obj_in: completeblock_schemas.CompletedContentBlockUpdate, db: Session = Depends(get_db)):
    return completedcb.update(db=db, db_obj=completedcb.get(db=db, id=id), obj_in=obj_in)


@router.delete('/{section_id}', response_model=completeblock_schemas.CompletedContentBlock)
async def delete(id: int, db: AsyncSession = Depends(async_get_db)):
    return await completedcb.remove(db=db, id=id)
