from app.services import ArticleService
from app.models import Article
from pydantic import Field
from pydantic import BaseModel
from app.database.database import UserDomain



class ActiveUsersArticlesGetter:
    def __init__(self):
        pass

    def run(self) -> Article:
        article_service = ArticleService()
        articles = article_service.get_active_users_articles()
        return articles
