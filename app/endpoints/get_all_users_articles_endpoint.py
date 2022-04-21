import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter
from typing import List
from typing import Optional
from typing import Final
from datetime import datetime
from app.bp.get_all_users_articles_usercase import AllUsersArticlesGetter


router = APIRouter()

GET_USER_ERROR_MESSAGE: Final = "ERROR IN users articles ENDPOINT"
USERS_ENDPOINT_SUMMARY: Final = "Show all Users Articles"
USERS_ENDPOINT_PATH: Final = "/users_articles"


class GetAllUsersArticlesResponse(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    email: str = Field(...)



@router.get(
    path=USERS_ENDPOINT_PATH,
    response_model=List[GetAllUsersArticlesResponse],
    status_code=status.HTTP_200_OK,
    summary=USERS_ENDPOINT_SUMMARY,
    tags=["Both"],
)
def get_users():
    users_articles_response = []
    try:
        user_getter = AllUsersArticlesGetter()
        users_articles = user_getter.run()
        # users_articles_response = [GetAllUsersArticlesResponse(**ua.__dict__) for ua in users_articles]
    except Exception as error:
        logging.error(GET_USER_ERROR_MESSAGE, error)
    return users_articles_response
