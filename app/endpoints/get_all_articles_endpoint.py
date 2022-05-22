import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter
from typing import List
from typing import Optional
from typing import Final
from datetime import datetime
from app.bp.get_all_articles_usercase import AllArticleGetter


router = APIRouter()

GET_ARTICLE_ERROR_MESSAGE: Final = "ERROR IN all_articles ENDPOINT"
ARTICLES_ENDPOINT_SUMMARY: Final = "Show all Articles"
ARTICLES_ENDPOINT_PATH: Final = "/all_articles"


class GetAllArticlesResponse(BaseModel):
    id: int = Field(...)
    title: str = Field(...)
    information: str = Field(...)
    autor_id: int = Field(...)
    published_at: Optional[datetime] = Field()
    updated_at: Optional[datetime] = Field()


@router.get(
    path=ARTICLES_ENDPOINT_PATH,
    response_model=List[GetAllArticlesResponse],
    status_code=status.HTTP_200_OK,
    summary=ARTICLES_ENDPOINT_SUMMARY,
    tags=["Articles"],
)
def get_articles():
    articles_response = []
    try:
        article_getter = AllArticleGetter()
        articles = article_getter.run()
        articles_response = [
            GetAllArticlesResponse(**article.__dict__) for article in articles
        ]
    except Exception as error:
        logging.error(GET_ARTICLE_ERROR_MESSAGE, error)
    return articles_response
