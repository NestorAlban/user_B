import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import Body, Path
from fastapi import status
from fastapi import APIRouter
from typing import Any
from typing import Optional
from typing import Final
from datetime import datetime
from typing import Dict

from app.bp.delete_user_usercase import UserDeleter, DeleteUserParams


router = APIRouter()

GET_USER_ERROR_MESSAGE: Final = "ERROR IN users ENDPOINT"
USERS_ENDPOINT_SUMMARY: Final = "Delete User"
USERS_ENDPOINT_PATH: Final = "/user/delete_user"
SUCCESS_KEY: Final = "success"
USER_KEY: Final = "user"


class DeleteUserInput(BaseModel):
    id: int = Field(default=1)


class DeleteUserResponse(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    email: str = Field(...)
    is_active: Optional[bool] = Field()
    created_at: Optional[datetime] = Field()
    updated_at: Optional[datetime] = Field()


@router.delete(
    path=USERS_ENDPOINT_PATH,
    status_code=status.HTTP_200_OK,
    response_model=Dict[str, Any],
    summary=USERS_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def delete_user(id: int):
    success = False
    users_response = None
    try:
        user_getter = UserDeleter()
        user = user_getter.run(DeleteUserParams(id=id))
        if user:
            success = True
            users_response = DeleteUserResponse(**user.__dict__)
    except Exception as error:
        logging.error(GET_USER_ERROR_MESSAGE, error)
    return {SUCCESS_KEY: success, USER_KEY: users_response}
