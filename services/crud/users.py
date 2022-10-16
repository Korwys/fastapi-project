from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from starlette.responses import JSONResponse

from db.models.users import User
from schemas.users_schemas import UserCreate


async def create_new_user(db: AsyncSession, user: UserCreate):
    db_user = User(email=user.email, password = user.password, role=user.role)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def users_list(db: AsyncSession, skip: int = 0, limit: int = 5):
    return db.query(User).offset(skip).limit(limit).all()


async def single_user(db: AsyncSession, user_id: int):
    query = select(User).where(User.id == user_id)
    sel = await db.execute(query)
    return sel.scalar_one_or_none()


async def delete_select_user(db: AsyncSession, user_id: int):
    user = delete(User).where(User.id == user_id)
    await db.execute(user)
    await db.commit()
    return JSONResponse(status_code=200, content={'Message': 'User deleted'})
