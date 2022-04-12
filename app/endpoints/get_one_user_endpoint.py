import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import Body, Path
from fastapi import status
from fastapi import APIRouter
from typing import List
from typing import Optional
from typing import Final
from datetime import datetime

from app.bp.get_one_user_usecase import (
    OneUserGetter, 
    OneUserGetterParams
)


router = APIRouter()

GET_USER_ERROR_MESSAGE: Final = "ERROR IN users ENDPOINT"
USERS_ENDPOINT_SUMMARY: Final = "Show one User"
USERS_ENDPOINT_PATH: Final = "/user/{id}"

class GetOneUserInput(BaseModel):
    id: int = Field(default=1)

class GetUsersResponse(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    email: str = Field(...)
    is_active: Optional[bool] = Field()
    created_at: Optional[datetime] = Field()
    updated_at: Optional[datetime] = Field()


@router.get(
    path=USERS_ENDPOINT_PATH,
    response_model=List[GetUsersResponse],
    status_code=status.HTTP_200_OK,
    summary=USERS_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def get_users(id: int = Path(..., title="User ID")):
    users_response = []
    try:
        user_getter = OneUserGetter()
        print("=====================================================")
        users = user_getter.run(OneUserGetterParams(id=id))
        print(users, "1")
        print("=====================================================")
        users_response = [
            GetUsersResponse(**user.__dict__) for user in users
        ]
    except Exception as error:
        logging.error(GET_USER_ERROR_MESSAGE, error)
    return users_response

