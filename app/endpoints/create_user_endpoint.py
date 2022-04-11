import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter

from typing import Final
from typing import Dict
from app.bp.create_users_usecase import UserCreator

from app.models.user import User
from app.bp.create_users_usecase import UserCreatorParams


router = APIRouter()

CREATE_USER_ERROR_MESSAGE: Final = "ERROR IN create_user ENDPOINT"
CREATE_USER_ENDPOINT_SUMMARY: Final = "Create a new User"
CREATE_USER_ENDPOINT_PATH: Final = "/create_user"
SUCCESS_KEY: Final = "success"
USER_KEY: Final = "user"


class CreateUserInput(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    email: str = Field(...)


@router.post(
    path=CREATE_USER_ENDPOINT_PATH,
    status_code=status.HTTP_201_CREATED,
    summary=CREATE_USER_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def create_user(new_user_data: CreateUserInput):
    success = False
    user = None
    try:
        user_creator = UserCreator()
        user = user_creator.run(
            UserCreatorParams(id=new_user_data.id, name=new_user_data.name, email=new_user_data.email)
        )
        success = True
    except Exception as error:
        logging.error(CREATE_USER_ERROR_MESSAGE, error)
    return {SUCCESS_KEY: success, USER_KEY: user}
