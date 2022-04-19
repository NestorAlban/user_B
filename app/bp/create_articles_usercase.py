
from app.services import ArticleService
from typing import List
from app.models import User
from pydantic import Field
from pydantic import BaseModel
from app.database.database import ArticleDomain


class ArticleCreatorParams(BaseModel):
    title: str = Field(...)
    autor_id: int = Field(...)


class ArticleCreator:
    def __init__(self):
        pass

    def run(self, params: ArticleCreatorParams) -> ArticleDomain:
        article_service = ArticleService()
        article = article_service.create_article(params.title, params.autor_id)
        return article

