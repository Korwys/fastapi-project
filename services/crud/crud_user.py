from sqlalchemy.ext.asyncio import AsyncSession

from db.models.users import User
from schemas.users_schemas import UserCreate, UserUpdate
from services.crud.base import CRUDBase
from services.security import create_hashed_user_password


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    """Класс наследует все методы CREATE,READ,UPDATE,DELETE. Реализует CRUD операции над моделью User"""

    def create(self, db: AsyncSession, obj_in: UserCreate):
        new_data = obj_in.dict()
        new_data.pop('password')
        db_obj = User(**new_data)
        db_obj.password = create_hashed_user_password(obj_in.password)
        db.add(db_obj)
        db.commit()
        return db_obj


user = CRUDUser(User)
