import fastapi
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from db.db_setup import get_db, async_get_db
from schemas import user
from services.crud import create_new_user, users_list, single_user, delete_select_user

router = fastapi.APIRouter()


@router.post("/user", response_model=user.User)
async def create_user(user: user.CreateUser, db: AsyncSession = Depends(async_get_db)):
    return await create_new_user(db=db, user=user)


@router.get('/users', response_model=list[user.User])
async def get_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 5):
    return await users_list(db, skip=skip, limit=limit)


@router.get('/users/{user_id}', response_model=user.User)
async def get_single_user(user_id: int, db: AsyncSession = Depends(async_get_db)):
    return await single_user(user_id=user_id, db=db)


@router.delete('/users/{user_id}')
async def delete_user(user_id: int, db: AsyncSession = Depends(async_get_db)):
    return await delete_select_user(user_id=user_id, db=db)