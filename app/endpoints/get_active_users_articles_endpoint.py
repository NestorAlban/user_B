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

from app.bp.get_active_users_articles_usercase import ActiveUsersArticlesGetter


router = APIRouter()

GET_ACTIVE_USERS_ARTICLES_ERROR_MESSAGE: Final = "ERROR IN users articles ENDPOINT"
ACTIVE_USERS_ARTICLES_ENDPOINT_SUMMARY: Final = "Show active Users Articles"
ACTIVE_USERS_ARTICLES_ENDPOINT_PATH: Final = "/users/articles"
ACTIVE_USERS_ARTICLES_KEY: Final = "active users articles"


class GetOneUserInput(BaseModel):
    id: int = Field(default=1)


class GetOneUserArticlesResponse(BaseModel):
    id: int = Field(...)
    title: str = Field(...)
    published_at: Optional[datetime] = Field()
    autor_id: int = Field(...)



@router.get(
    path=ACTIVE_USERS_ARTICLES_ENDPOINT_PATH,
    response_model=Dict[str, Any],
    status_code=status.HTTP_200_OK,
    summary=ACTIVE_USERS_ARTICLES_ENDPOINT_SUMMARY,
    tags=["Articles"],
)
def get_one_user_articles():
    user_articles_response = None
    try:
        use_articles_getter = ActiveUsersArticlesGetter()
        articles = use_articles_getter.run()
        if articles:
            user_articles_response = [
                GetOneUserArticlesResponse(**article.__dict__) for article in articles
            ]
    except Exception as error:
        logging.error(GET_ACTIVE_USERS_ARTICLES_ERROR_MESSAGE, error)
    return {ACTIVE_USERS_ARTICLES_KEY: user_articles_response}