from app.services import ArticleService
from app.models import Article
from pydantic import Field
from pydantic import BaseModel
from app.database.database import UserDomain


class OneUserArticlesGetterParams(BaseModel):
    id: int = Field(...)


class OneUserArticlesGetter:
    def __init__(self):
        pass

    def run(self, params: OneUserArticlesGetterParams) -> Article:
        article_service = ArticleService()
        articles = article_service.get_one_user_articles(params.id)
        return articles
