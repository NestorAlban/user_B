import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter
from typing import List
from typing import Optional
from typing import Final
from datetime import datetime
from app.bp.get_all_users_with_articles_usercase import AllUsersWithArticlesGetter


router = APIRouter()

GET_USERS_WITH_ARTICLES_ERROR_MESSAGE: Final = "ERROR IN users with articles ENDPOINT"
USERS_WITH_ARTICLES_ENDPOINT_SUMMARY: Final = "Show all Users with Articles"
USERS_WITH_ARTICLES_ENDPOINT_PATH: Final = "/users/articles"


class GetAllUsersWithArticlesResponse(BaseModel):
    user_id: int = Field(...)
    article_id: Optional[int] = Field()
    user_name: str = Field(...)
    article_title: Optional[str] = Field()




@router.get(
    path=USERS_WITH_ARTICLES_ENDPOINT_PATH,
    response_model=List[GetAllUsersWithArticlesResponse],
    status_code=status.HTTP_200_OK,
    summary=USERS_WITH_ARTICLES_ENDPOINT_SUMMARY,
    tags=["Both"],
)
def get_users():
    users_articles_response = []
    try:
        user_articles_getter = AllUsersWithArticlesGetter()
        users_articles = user_articles_getter.run()
        users_articles_response = [GetAllUsersWithArticlesResponse(**ua.__dict__) for ua in users_articles]
        
    except Exception as error:
        logging.error(GET_USERS_WITH_ARTICLES_ERROR_MESSAGE, error)
    return users_articles_response
