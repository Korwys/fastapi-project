import fastapi
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.db_setup import async_get_db, get_db
from schemas import contentblock_schemas
from services.crud.contentblocks import new_contentblock, list_of_contentblocks, get_contentblock, delete_contentblock, \
    edit_contentblock

router = fastapi.APIRouter()


@router.post('/contentblocks', response_model=contentblock_schemas.ContentBlock)
async def create_contentblock(contentblock: contentblock_schemas.CreateContentBlock,
                              db: AsyncSession = Depends(async_get_db)):
    return await new_contentblock(db=db, contentblock=contentblock)


@router.get('/contentblocks', response_model=list[contentblock_schemas.ContentBlock])
async def get_courses(db: AsyncSession = Depends(get_db)):
    return await list_of_contentblocks(db=db)


@router.get('/contentblocks/{contentblock_id}', response_model=contentblock_schemas.ContentBlock)
async def get_retrieve_contentblock(contentblock_id: int, db: AsyncSession = Depends(async_get_db)):
    return await get_contentblock(contentblock_id=contentblock_id, db=db)


@router.delete('/contentblocks/{contentblock_id}', response_model=contentblock_schemas.ContentBlock)
async def delete_selected_contentblock(contentblock_id: int, db: AsyncSession = Depends(async_get_db)):
    return await delete_contentblock(contentblock_id=contentblock_id, db=db)


@router.put('/contentblocks/{contentblock_id}', response_model=contentblock_schemas.ContentBlock)
async def edit_selected_contentblock(contentblock_id: int, contentblock: contentblock_schemas.BaseContentBlock,
                                     db: AsyncSession = Depends(async_get_db)):
    return await edit_contentblock(contentblock_id=contentblock_id, contentblock=contentblock, db=db)
