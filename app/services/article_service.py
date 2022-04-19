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

    def create_article(self, title: str, autor_id: int) -> ArticleDomain:
        article = self.alchemy_db.create_article(title, autor_id)
        return article

