import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter

from typing import Final
from typing import Dict
from app.bp.change_user_status_usecase import (
    UserStatus, 
    UserStatusModParams
)
from typing import Optional
from datetime import datetime

from app.models.user import User

router = APIRouter()

UPDATE_USER_STATUS_ERROR_MESSAGE: Final = "ERROR IN update_status ENDPOINT"
UPDATE_USER_STATUS_ENDPOINT_SUMMARY: Final = "Update User status"
UPDATE_USER_STATUS_ENDPOINT_PATH: Final = "/user/{id}/update_status"
SUCCESS_KEY: Final = "success"
USER_KEY: Final = "user"


class UpdateUserStatusInput(BaseModel):
    id: int = Field(...)
    is_active: bool = Field(default = True)

class GetUsersResponse(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    email: str = Field(...)
    is_active: Optional[bool] = Field()
    created_at: Optional[datetime] = Field()
    updated_at: Optional[datetime] = Field()

@router.delete(
    path=UPDATE_USER_STATUS_ENDPOINT_PATH,
    status_code=status.HTTP_200_OK,
    summary=UPDATE_USER_STATUS_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def update_user_status(new_user_data: UpdateUserStatusInput):
    success = False
    users_response = []
    try:
        user_status_update = UserStatus()
        users = user_status_update.run(
            UserStatusModParams(
                id=new_user_data.id,
                is_active=new_user_data.is_active
            )
        )
        success = True
        users_response = [
            GetUsersResponse(**user.__dict__) for user in users
        ]
    except Exception as error:
        logging.error(UPDATE_USER_STATUS_ERROR_MESSAGE, error)
    return {SUCCESS_KEY: success, USER_KEY: users_response}

