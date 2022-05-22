import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter
from typing import List
from typing import Optional
from typing import Final
from datetime import datetime
from app.bp.get_users_usecase import UserGetter


router = APIRouter()

GET_USER_ERROR_MESSAGE: Final = "ERROR IN users ENDPOINT"
USERS_ENDPOINT_SUMMARY: Final = "Show active Users"
USERS_ENDPOINT_PATH: Final = "/users"


class GetActiveUsersResponse(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    email: str = Field(...)
    is_active: Optional[bool] = Field()
    created_at: Optional[datetime] = Field()
    updated_at: Optional[datetime] = Field()


@router.get(
    path=USERS_ENDPOINT_PATH,
    response_model=List[GetActiveUsersResponse],
    status_code=status.HTTP_200_OK,
    summary=USERS_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def get_users():
    users_response = []
    try:
        user_getter = UserGetter()
        users = user_getter.run()
        users_response = [GetActiveUsersResponse(**user.__dict__) for user in users]
    except Exception as error:
        logging.error(GET_USER_ERROR_MESSAGE, error)
    return users_response
