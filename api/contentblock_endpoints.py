import fastapi
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from db.db_setup import async_get_db, get_db
from db.models.courses import ContentBlock
from schemas import contentblock_schemas, users_schemas
from services.crud.crud_contentblocks import contentblock
from services.security import get_current_user

router = fastapi.APIRouter()


@router.post('/', response_model=contentblock_schemas.ContentBlock)
async def create_contentblock(section: contentblock_schemas.ContentBlockCreate,
                              db: AsyncSession = Depends(async_get_db),
                              user: users_schemas.User = Depends(get_current_user)) -> ContentBlock:
    return await contentblock.create(db=db, obj_in=section)


@router.get('/', response_model=list[contentblock_schemas.ContentBlock])
async def fetch_list_of_contentblocks(db: AsyncSession = Depends(get_db),
                                      user: users_schemas.User = Depends(get_current_user)) -> list[ContentBlock]:
    return contentblock.get_multi(db=db)


@router.get('/{contentblock_id}', response_model=contentblock_schemas.ContentBlock)
async def fetch_contentblock(id: int, db: AsyncSession = Depends(get_db),
                             user: users_schemas.User = Depends(get_current_user)) -> ContentBlock:
    return contentblock.get(db=db, id=id)


@router.put('/{contentblock_id}', response_model=contentblock_schemas.ContentBlock)
async def update_contentblock(id: int, obj_in: contentblock_schemas.ContentBlockUpdate, db: Session = Depends(get_db),
                              user: users_schemas.User = Depends(get_current_user)) -> ContentBlock:
    return contentblock.update(db=db, db_obj=contentblock.get(db=db, id=id), obj_in=obj_in)


@router.delete('/{contentblock_id}', response_model=contentblock_schemas.ContentBlock)
async def delete_contentblock(id: int, db: AsyncSession = Depends(async_get_db),
                              user: users_schemas.User = Depends(get_current_user)) -> JSONResponse:
    return await contentblock.remove(db=db, id=id)
