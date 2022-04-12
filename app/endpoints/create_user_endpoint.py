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
from typing import Optional
from datetime import datetime

router = APIRouter()

CREATE_USER_ERROR_MESSAGE: Final = "ERROR IN create_user ENDPOINT"
CREATE_USER_ENDPOINT_SUMMARY: Final = "Create a new User"
CREATE_USER_ENDPOINT_PATH: Final = "/create_user"
SUCCESS_KEY: Final = "success"
USER_KEY: Final = "user"


class CreateUserInput(BaseModel):
    name: str = Field(default="Example")
    email: str = Field(default="example@email.com")


class CreateUserResponse(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    email: str = Field(...)
    is_active: Optional[bool] = Field()
    created_at: Optional[datetime] = Field()
    updated_at: Optional[datetime] = Field()


@router.post(
    path=CREATE_USER_ENDPOINT_PATH,
    status_code=status.HTTP_201_CREATED,
    summary=CREATE_USER_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def create_user(new_user_data: CreateUserInput):
    success = False
    user_r = None
    try:
        user_creator = UserCreator()
        user = user_creator.run(UserCreatorParams(
            name=new_user_data.name, 
            email=new_user_data.email
        ))
        # print(f"user E:{user}")
        success = True
        user_r = CreateUserResponse.construct(
            id=user.id,
            name=user.name,
            email=user.email,
            is_active=user.is_active,
            created_at=user.created_at,
            updated_at=user.updated_at,
        ).dict(by_alias=True)
    except Exception as error:
        logging.error(CREATE_USER_ERROR_MESSAGE, error)
    return {SUCCESS_KEY: success, USER_KEY: user_r}
