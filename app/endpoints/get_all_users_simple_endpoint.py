import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter
from typing import List
from typing import Optional
from typing import Final
from datetime import datetime
from app.bp.get_all_users_simple_usercase import AllUsersSimpleGetter


router = APIRouter()

GET_USER_SIMPLE_ERROR_MESSAGE: Final = "ERROR IN users simple ENDPOINT"
USERS_SIMPLE_ENDPOINT_SUMMARY: Final = "Show all Users simple"
USERS_SIMPLE_ENDPOINT_PATH: Final = "/users_simple"


class GetAllUsersSimpleResponse(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    email: str = Field(...)



@router.get(
    path=USERS_SIMPLE_ENDPOINT_PATH,
    response_model=List[GetAllUsersSimpleResponse],
    status_code=status.HTTP_200_OK,
    summary=USERS_SIMPLE_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def get_users_simple():
    users_response = []
    try:
        user_getter = AllUsersSimpleGetter()
        users = user_getter.run()
        users_response = [GetAllUsersSimpleResponse(**user.__dict__) for user in users]
    except Exception as error:
        logging.error(GET_USER_SIMPLE_ERROR_MESSAGE, error)
    return users_response
