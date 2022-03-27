import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter
from typing import List
from typing import Final

from app.bp.create_users_usecase import UserCreator

from app.database.queries import NAME_KEY
from app.database.queries import MAIL_KEY
from app.database.queries import STATUS_KEY
from app.database.queries import CREATED_KEY
from app.database.queries import UPDATED_KEY
from app.models.user import User


router = APIRouter()

GET_USER_ERROR_MESSAGE: Final = "ERROR IN users ENDPOINT"
USERS_ENDPOINT_SUMMARY: Final = "Register a new User"
USERS_ENDPOINT_PATH: Final = "/register_users"


class GetUsersResponse(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    email: str = Field(...)
    is_active: str = Field()
    created_at: str = Field()
    updated_at: str = Field()


@router.post(
    path=USERS_ENDPOINT_PATH,
    response_model=List[GetUsersResponse],
    status_code=status.HTTP_201_CREATED,
    summary=USERS_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def create_user(new_user_data: User):
    users_response = []
    try:
        user_data = new_user_data.dict()
        user_getter = UserCreator()

        users = new_user_data.dict()
        user_data[NAME_KEY] = str(user_data[NAME_KEY])
        user_data[MAIL_KEY] = str(user_data[MAIL_KEY])
        user_data[STATUS_KEY] = str(user_data[STATUS_KEY])
        user_data[CREATED_KEY] = str(user_data[CREATED_KEY])
        user_data[UPDATED_KEY] = str(user_data[UPDATED_KEY])
        users = (user_data[NAME_KEY], user_data[MAIL_KEY], user_data[STATUS_KEY])
        print(users, "1")
        print("=====================================================")
        users = user_getter.run()
        print(users, "1")
        print("=====================================================")
        users_response = [GetUsersResponse(**user.dict()) for user in users]
        # users_response = [GetUsersResponse(
        #     id=user.id,
        #     name=user.name,
        #     email=user.email,
        #     is_active=user.is_active,
        #     created_at=user.created_at,
        #     updated_at=user.updated_at
        # ) for user in users]
    except Exception as error:
        logging.error(GET_USER_ERROR_MESSAGE, error)
    return users_response
