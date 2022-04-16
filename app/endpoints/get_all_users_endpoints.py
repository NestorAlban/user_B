import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter
from typing import List
from typing import Optional
from typing import Final
from datetime import datetime
from app.bp.get_all_users_usercase import AllUserGetter


router = APIRouter()

GET_USER_ERROR_MESSAGE: Final = "ERROR IN users ENDPOINT"
USERS_ENDPOINT_SUMMARY: Final = "Show all Users"
USERS_ENDPOINT_PATH: Final = "/all_users"


class GetAllUsersResponse(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    email: str = Field(...)
    is_active: Optional[bool] = Field()
    created_at: Optional[datetime] = Field()
    updated_at: Optional[datetime] = Field()


@router.get(
    path=USERS_ENDPOINT_PATH,
    response_model=List[GetAllUsersResponse],
    status_code=status.HTTP_200_OK,
    summary=USERS_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def get_users():
    users_response = []
    try:
        user_getter = AllUserGetter()
        users = user_getter.run()
        users_response = [GetAllUsersResponse(**user.__dict__) for user in users]
    except Exception as error:
        logging.error(GET_USER_ERROR_MESSAGE, error)
    return users_response
