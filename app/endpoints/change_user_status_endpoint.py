import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter

from typing import Final
from typing import Dict
from app.bp.change_user_status_usecase import UserStatus

from app.models.user import User

router = APIRouter()

UPDATE_USER_STATUS_ERROR_MESSAGE: Final = "ERROR IN update_status ENDPOINT"
UPDATE_USER_STATUS_ENDPOINT_SUMMARY: Final = "Update User status"
UPDATE_USER_STATUS_ENDPOINT_PATH: Final = "/user/{id}/update_status"
SUCCESS_KEY: Final = "success"


class UpdateUserInput(BaseModel):
    id: int = Field(...)
    name: str = Field(default="Example")
    email: str = Field(default="example@email.com")
    is_active: bool = Field(default=True)


@router.delete(
    path=UPDATE_USER_STATUS_ENDPOINT_PATH,
    response_model=Dict[str, bool],
    status_code=status.HTTP_200_OK,
    summary=UPDATE_USER_STATUS_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def update_user_status(new_user_data):
    success = False
    try:
        user_creator = UserStatus()
        success = user_creator.run(
            User(id=new_user_data.id, is_active=new_user_data.is_active, updated_at=new_user_data.updated_at)
        )
    except Exception as error:
        logging.error(UPDATE_USER_STATUS_ERROR_MESSAGE, error)
    return {SUCCESS_KEY: success}
