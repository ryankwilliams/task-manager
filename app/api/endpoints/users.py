import uuid
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.api.common import get_db
from app.api.endpoints.types import User
from app.api.endpoints.types import UserCreate
from app.api.endpoints.types import UserCreateResponse
from app.db.crud import UsersDB

router: APIRouter = APIRouter()


@router.post("/")
def create(user_create: UserCreate, db: Session = Depends(get_db)) -> UserCreateResponse:
    user = User(**user_create.__dict__)
    user.user_id = uuid.uuid4().__str__()

    UsersDB(db).create_user(user=user)

    return UserCreateResponse(id=user.user_id)


@router.get("/")
def list_users(db: Session = Depends(get_db)) -> List[User]:
    db_users = UsersDB(db).get_all_users()

    users: List[User] = []

    for db_user in db_users:
        users.append(User(**db_user.__dict__))

    return users


@router.delete("/{user_id}")
def delete(user_id: str, db: Session = Depends(get_db)) -> None:
    UsersDB(db).delete_user(user_id=user_id)
