import fastapi
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import Json
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from db.db_setup import get_db, async_get_db
from db.models.users import User
from schemas import users_schemas, acess_token
from services.crud.crud_user import user
from services.security import verify_user_password, create_token

router = fastapi.APIRouter()


@router.post("/singup", response_model=users_schemas.User)
async def create_user(obj_in: users_schemas.UserCreate, db: AsyncSession = Depends(async_get_db)) -> User:
    new_user = user.create(db=db, obj_in=obj_in)
    return new_user


@router.post('/login', response_model=acess_token.Token)
def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()) -> Json:
    user_email = db.query(User).where(User.email == form_data.username)
    if not user_email:
        raise HTTPException(status_code=401, detail='Bad credentials')
    user_password = verify_user_password(db=db, user_credentials=form_data)
    if not user_password:
        raise HTTPException(status_code=401, detail='Bad credentials')

    return {
        "access_token": create_token(sub=form_data.username),
        "token_type": "bearer"
    }
