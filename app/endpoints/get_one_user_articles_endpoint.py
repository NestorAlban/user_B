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

from app.bp.get_one_user_articles_usercase import OneUserArticlesGetterParams
from app.bp.get_one_user_articles_usercase import OneUserArticlesGetter


router = APIRouter()

GET_USER_ARTICLES_ERROR_MESSAGE: Final = "ERROR IN user articles ENDPOINT"
USER_ARTICLES_ENDPOINT_SUMMARY: Final = "Show one User Articles"
USER_ARTICLES_ENDPOINT_PATH: Final = "/user/{id}/articles"
USER_ARTICLES_KEY: Final = "user articles"


class GetOneUserInput(BaseModel):
    id: int = Field(default=1)


class GetOneUserArticlesResponse(BaseModel):
    id: int = Field(...)
    title: str = Field(...)
    published_at: Optional[datetime] = Field()
    autor_id: int = Field(...)



@router.get(
    path=USER_ARTICLES_ENDPOINT_PATH,
    response_model=Dict[str, Any],
    status_code=status.HTTP_200_OK,
    summary=USER_ARTICLES_ENDPOINT_SUMMARY,
    tags=["Articles"],
)
def get_one_user_articles(id: int = Path(..., title="User ID")):
    user_articles_response = None
    try:
        use_articles_getter = OneUserArticlesGetter()
        articles = use_articles_getter.run(OneUserArticlesGetterParams(id = id))
        if articles:
            user_articles_response = [
                GetOneUserArticlesResponse(**article.__dict__) for article in articles
            ]
    except Exception as error:
        logging.error(GET_USER_ARTICLES_ERROR_MESSAGE, error)
    return {USER_ARTICLES_KEY: user_articles_response}



