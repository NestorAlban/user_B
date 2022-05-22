from tkinter import N
from app.database import Database
from app.database import Db
from app.database import UserDomain
from app.database import ArticleDomain

from typing import List
from app.models import User
from app.models import Article


class ArticleService:
    def __init__(self):
        self.database = Database()
        self.alchemy_db = Db()
        pass

    def get_all_articles(self) -> List[Article]:
        articles = []
        articles = self.alchemy_db.get_all_articles()
        return articles

    def create_article(self, title: str, information: str, autor_id: int) -> ArticleDomain:
        article = self.alchemy_db.create_article(title, information, autor_id)
        return article

    def get_one_user_articles(self, id: int) -> List[Article]:
        articles = self.alchemy_db.get_one_user_articles(id)
        return articles

    def get_active_users_articles(self) -> List[Article]:
        articles = self.alchemy_db.get_active_users_articles()
        return articles

    def update_one_user_article(self, id: int, title: str, information: str) -> ArticleDomain:
        articles = self.alchemy_db.update_one_user_article(id, title, information)
        return articles