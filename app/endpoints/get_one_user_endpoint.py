import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import Path
from fastapi import status
from fastapi import APIRouter
from typing import Dict
from typing import Optional
from typing import Final
from typing import Any

from datetime import datetime

from app.bp.get_one_user_usecase import OneUserGetter, OneUserGetterParams


router = APIRouter()

GET_USER_ERROR_MESSAGE: Final = "ERROR IN users ENDPOINT"
USERS_ENDPOINT_SUMMARY: Final = "Show one User"
USERS_ENDPOINT_PATH: Final = "/user/{id}"
USER_KEY: Final = "user"


class GetOneUserInput(BaseModel):
    id: int = Field(default=1)


class GetOneUserResponse(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    email: str = Field(...)
    is_active: Optional[bool] = Field()
    created_at: Optional[datetime] = Field()
    updated_at: Optional[datetime] = Field()


@router.get(
    path=USERS_ENDPOINT_PATH,
    response_model=Dict[str, Any],
    status_code=status.HTTP_200_OK,
    summary=USERS_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def get_one_user(id: int = Path(..., title="User ID")):
    users_response = None
    try:
        user_getter = OneUserGetter()
        user = user_getter.run(OneUserGetterParams(id=id))
        if user:
            users_response = GetOneUserResponse(**user.__dict__)
    except Exception as error:
        logging.error(GET_USER_ERROR_MESSAGE, error)
    return {USER_KEY: users_response}
