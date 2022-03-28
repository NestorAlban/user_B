import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter

from typing import Final
from typing import Dict
from app.bp.update_users_usercase import UserUpdate

from app.models.user import User


router = APIRouter()

UPDATE_USER_ERROR_MESSAGE: Final = "ERROR IN update_user ENDPOINT"
UPDATE_USER_ENDPOINT_SUMMARY: Final = "Update a new User"
UPDATE_USER_ENDPOINT_PATH: Final = "/user/{id}/update_user"
SUCCESS_KEY: Final = "success"


class UpdateUserInput(BaseModel):
    id: int = Field(...)
    name: str = Field(default="Example")
    email: str = Field(default="example@email.com")
    is_active: bool = Field(default=True)


@router.put(
    path=UPDATE_USER_ENDPOINT_PATH,
    response_model=Dict[str, bool],
    status_code=status.HTTP_200_OK,
    summary=UPDATE_USER_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def update_user(new_user_data: User):
    success = False
    try:
        user_creator = UserUpdate()
        success = user_creator.run(
            User(
                id=new_user_data.id,
                name=new_user_data.name,
                email=new_user_data.email,
                updated_at=new_user_data.updated_at,
            )
        )
    except Exception as error:
        logging.error(UPDATE_USER_ERROR_MESSAGE, error)
    return {SUCCESS_KEY: success}
