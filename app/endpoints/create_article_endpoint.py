import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter
from typing import Final
from typing import Optional
from datetime import datetime

from app.bp.create_articles_usercase import ArticleCreator
from app.bp.create_articles_usercase import ArticleCreatorParams


router = APIRouter()

CREATE_ARTICLE_ERROR_MESSAGE: Final = "ERROR IN create_article ENDPOINT"
CREATE_ARTICLE_ENDPOINT_SUMMARY: Final = "Create a new Article"
CREATE_ARTICLE_ENDPOINT_PATH: Final = "/create_article"
SUCCESS_KEY: Final = "success"
ARTICLE_KEY: Final = "article"


class CreateArticleInput(BaseModel):
    title: str = Field(default = "This is a title example")
    information: str = Field(default = "This is an information example to try the API and SQLAlchemy")
    autor_id: int = Field(default = 1)


class CreateArticleResponse(BaseModel):
    id: int = Field(...)
    title: str = Field(...)
    information: str = Field(...)
    autor_id: int = Field(...)
    published_at: Optional[datetime] = Field()
    updated_at: Optional[datetime] = Field()



@router.post(
    path=CREATE_ARTICLE_ENDPOINT_PATH,
    status_code=status.HTTP_201_CREATED,
    summary=CREATE_ARTICLE_ENDPOINT_SUMMARY,
    tags=["Articles"],
)
def create_user(new_article_data: CreateArticleInput):
    success = False
    article_response = None
    try:
        article_creator = ArticleCreator()
        title = new_article_data.title.strip()
        information = new_article_data.information.strip()
        autor_id = new_article_data.autor_id

        if len(title) != 0 and len(information) != 0:
            article = article_creator.run(ArticleCreatorParams(
                title = title,
                information = information,
                autor_id = autor_id)
            )
            if article:
                success = True
                article_response = CreateArticleResponse.construct(
                    id = article.id,
                    title = article.title,
                    information = article.information,
                    autor_id = article.autor_id,
                    published_at = article.published_at,
                    updated_at = article.updated_at,
                ).dict(by_alias=True)
    except Exception as error:
        logging.error(CREATE_ARTICLE_ERROR_MESSAGE, error)
    return {SUCCESS_KEY: success, ARTICLE_KEY: article_response}
