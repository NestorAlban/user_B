import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter
from typing import List
from typing import Optional
from typing import Final
from datetime import datetime
from app.bp.get_users_articles_usercase import UsersArticlesGetter


router = APIRouter()

GET_USERS_ARTICLES_ERROR_MESSAGE: Final = "ERROR IN users articles ENDPOINT"
USERS_ARTICLES_ENDPOINT_SUMMARY: Final = "Show Users Articles"
USERS_ARTICLES_ENDPOINT_PATH: Final = "/users/articles/all"


class GetAllUsersArticlesResponse(BaseModel):
    user_id: int = Field(...)
    user_name: str = Field(...)
    user_email: str = Field(...)
    article_id: Optional[int] = Field()
    article_title: Optional[str] = Field()
    article_information: Optional[str] = Field()
    article_published: Optional[datetime] = Field()
    article_updated: Optional[datetime] = Field()


@router.get(
    path=USERS_ARTICLES_ENDPOINT_PATH,
    response_model=List[GetAllUsersArticlesResponse],
    status_code=status.HTTP_200_OK,
    summary=USERS_ARTICLES_ENDPOINT_SUMMARY,
    tags=["Both"],
)
def get_users():
    users_articles_response = []
    try:
        user_getter = UsersArticlesGetter()
        users_articles = user_getter.run()
        users_articles_response = [GetAllUsersArticlesResponse(**ua.__dict__) for ua in users_articles]
        
    except Exception as error:
        logging.error(GET_USERS_ARTICLES_ERROR_MESSAGE, error)
    return users_articles_response