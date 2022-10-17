import fastapi
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from db.db_setup import async_get_db, get_db
from db.models.courses import CompletedContentBlock
from schemas import completeblock_schemas, users_schemas
from services.crud.crud_completeblocks import completedcb
from services.security import get_current_user

router = fastapi.APIRouter()


@router.post('/', response_model=completeblock_schemas.CompletedContentBlock)
async def create_completeblock(section: completeblock_schemas.CompletedContentBlockCreate,
                               db: AsyncSession = Depends(async_get_db),
                               user: users_schemas.User = Depends(get_current_user)) -> CompletedContentBlock:
    return await completedcb.create(db=db, obj_in=section)


@router.get('/', response_model=list[completeblock_schemas.CompletedContentBlock])
async def fetch_list_of_completeblocks(db: AsyncSession = Depends(get_db),
                                       user: users_schemas.User = Depends(get_current_user)) \
        -> list[CompletedContentBlock]:
    return completedcb.get_multi(db=db)


@router.get('/{completedblock_id}', response_model=completeblock_schemas.CompletedContentBlock)
async def fetch_retrieve_completeblock(id: int, db: AsyncSession = Depends(get_db),
                                       user: users_schemas.User = Depends(get_current_user)) -> CompletedContentBlock:
    return completedcb.get(db=db, id=id)


@router.put('/{completedblock_id}', response_model=completeblock_schemas.CompletedContentBlock)
async def update_completeblock(id: int, obj_in: completeblock_schemas.CompletedContentBlockUpdate,
                               db: Session = Depends(get_db),
                               user: users_schemas.User = Depends(get_current_user)) -> CompletedContentBlock:
    return completedcb.update(db=db, db_obj=completedcb.get(db=db, id=id), obj_in=obj_in)


@router.delete('/{completedblock_id}', response_model=completeblock_schemas.CompletedContentBlock)
async def delete_completeblock(id: int, db: AsyncSession = Depends(async_get_db),
                               user: users_schemas.User = Depends(get_current_user)) -> JSONResponse:
    return await completedcb.remove(db=db, id=id)
