import fastapi
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from db.db_setup import async_get_db, get_db
from db.models.courses import Section
from schemas import sections_schemas, users_schemas
from services.crud.crud_sections import sections
from services.security import get_current_user

router = fastapi.APIRouter()


@router.post('/', response_model=sections_schemas.Section)
async def create_section(section: sections_schemas.CreateSection, db: AsyncSession = Depends(async_get_db),
                         user: users_schemas.User = Depends(get_current_user)) -> Section:
    return await sections.create(db=db, obj_in=section)


@router.get('/', response_model=list[sections_schemas.Section])
async def fetch_list_of_sections(db: AsyncSession = Depends(get_db)) -> list[Section]:
    return sections.get_multi(db=db)


@router.get('/{section_id}', response_model=sections_schemas.Section)
async def fetch_section(id: int, db: AsyncSession = Depends(get_db)) -> Section:
    return sections.get(db=db, id=id)


@router.put('/{section_id}', response_model=sections_schemas.Section)
async def update_section(id: int, obj_in: sections_schemas.SectionUpdate, db: Session = Depends(get_db),
                         user: users_schemas.User = Depends(get_current_user)) -> Section:
    return sections.update(db=db, db_obj=sections.get(db=db, id=id), obj_in=obj_in)


@router.delete('/{section_id}', response_model=sections_schemas.Section)
async def delete_section(id: int, db: AsyncSession = Depends(async_get_db),
                         user: users_schemas.User = Depends(get_current_user)) -> JSONResponse:
    return await sections.remove(db=db, id=id)
