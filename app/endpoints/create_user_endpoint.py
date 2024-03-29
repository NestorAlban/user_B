import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter
from typing import Final
from typing import Optional
from datetime import datetime

from app.bp.create_users_usecase import UserCreator
from app.bp.create_users_usecase import UserCreatorParams


router = APIRouter()

CREATE_USER_ERROR_MESSAGE: Final = "ERROR IN create_user ENDPOINT"
CREATE_USER_ENDPOINT_SUMMARY: Final = "Create a new User"
CREATE_USER_ENDPOINT_PATH: Final = "/create_user"
SUCCESS_KEY: Final = "success"
USER_KEY: Final = "user"


class CreateUserInput(BaseModel):
    name: str = Field(default = "Example")
    email: str = Field(default = "example@email.com")


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
    user_response = None
    try:
        user_creator = UserCreator()
        name = new_user_data.name.strip()
        email = new_user_data.email.strip()

        if len(name) != 0 and len(email) != 0:
            user = user_creator.run(UserCreatorParams(
                name=name, 
                email=email)
            )
            if user:
                user_response = CreateUserResponse.construct(
                    id=user.id,
                    name=user.name,
                    email=user.email,
                    is_active=user.is_active,
                    created_at=user.created_at,
                    updated_at=user.updated_at,
                ).dict(by_alias=True)
                success = True
    except Exception as error:
        logging.error(CREATE_USER_ERROR_MESSAGE, error)
    return {SUCCESS_KEY: success, USER_KEY: user_response}
