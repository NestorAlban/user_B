import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter
from typing import Any
from typing import Final
from typing import Dict
from app.bp.update_articles_usercase import ArticleUpdate
from app.bp.update_articles_usercase import ArticleModParams
from typing import Optional
from datetime import datetime

from app.models.user import Article


router = APIRouter()

UPDATE_ARTICLE_ERROR_MESSAGE: Final = "ERROR IN update_article ENDPOINT"
UPDATE_ARTICLE_ENDPOINT_SUMMARY: Final = "Update an Article"
UPDATE_ARTICLE_ENDPOINT_PATH: Final = "/articles/{id}/update_article"
SUCCESS_KEY: Final = "success"
ARTICLE_KEY: Final = "article"


class UpdateArticleInput(BaseModel):
    id: int = Field(...)
    title: str = Field(...)
    information: str = Field(...)


class UpdatedArticleResponse(BaseModel):
    id: int = Field(...)
    title: str = Field(...)
    information: str = Field(...)
    autor_id: int = Field(...)
    published_at: Optional[datetime] = Field()
    updated_at: Optional[datetime] = Field()


@router.put(
    path=UPDATE_ARTICLE_ENDPOINT_PATH,
    status_code=status.HTTP_200_OK,
    response_model=Dict[str, Any],
    summary=UPDATE_ARTICLE_ENDPOINT_SUMMARY,
    tags=["Articles"],
)
def update_article(new_article_data: UpdateArticleInput):
    success = False
    article_response = None
    try:
        article_update = ArticleUpdate()
        title = new_article_data.title.strip()
        information = new_article_data.information.strip()
        if len(title) != 0 and len(information) != 0:
            article = article_update.run(ArticleModParams(
                id = new_article_data.id, 
                title = title, 
                information = information
            ))
            if article:
                success = True
                article_response = UpdatedArticleResponse(**article.__dict__)
    except Exception as error:
        logging.error(UPDATE_ARTICLE_ERROR_MESSAGE, error)
    return {SUCCESS_KEY: success, ARTICLE_KEY: article_response}
