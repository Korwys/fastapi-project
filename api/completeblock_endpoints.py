import fastapi
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.db_setup import async_get_db, get_db
from schemas import completeblock_schemas
from services.crud.completeblocks import add_new_student, list_of_completeblocks, get_completedblock, \
    delete_completedblock, edit_completedblock

router = fastapi.APIRouter()


@router.post('/completedblock', response_model=completeblock_schemas.CompleteContentBlock)
async def add_student_in_completeblock(completeblock: completeblock_schemas.CreateCompleteContentBlock,
                                       db: AsyncSession = Depends(async_get_db)):
    return await add_new_student(db=db, completeblock=completeblock)


@router.get('/copletedblock', response_model=list[completeblock_schemas.CompleteContentBlock])
async def get_completeblocks(db: AsyncSession = Depends(get_db)):
    return await list_of_completeblocks(db=db)


@router.get('/completedblock/{completedblock_id}', response_model=completeblock_schemas.CompleteContentBlock)
async def get_retrieve_completedblock(completedblock_id: int, db: AsyncSession = Depends(async_get_db)):
    return await get_completedblock(completedblock_id=completedblock_id, db=db)


@router.delete('/completedblock/{completedblock_id}', response_model=completeblock_schemas.CompleteContentBlock)
async def delete_selected_completedblock(completedblock_id: int, db: AsyncSession = Depends(async_get_db)):
    return await delete_completedblock(completedblock_id=completedblock_id, db=db)


@router.put('/contentblocks/{contentblock_id}', response_model=completeblock_schemas.CompleteContentBlock)
async def edit_selected_completedblock(completedblock_id: int, block: completeblock_schemas.BaseCompleteContentBlock,
                                     db: AsyncSession = Depends(async_get_db)):
    return await edit_completedblock(completedblock_id=completedblock_id, block=block, db=db)
