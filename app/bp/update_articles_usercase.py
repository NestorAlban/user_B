from app.services import ArticleService
from typing import List
from app.models import User
from pydantic import Field
from pydantic import BaseModel
from app.database.database import ArticleDomain


class ArticleModParams(BaseModel):
    id: int = Field(...)
    title: str = Field(...)
    information: str = Field(...)


class ArticleUpdate:
    def __init__(self):
        pass

    def run(self, params: ArticleModParams) -> ArticleDomain:
        article_service = ArticleService()
        articles = article_service.update_one_user_article(params.id, params.title, params.information)
        return articles