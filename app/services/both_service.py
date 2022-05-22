from app.database import Database
from app.database import Db
from app.database import UserDomain
from app.database import ArticleDomain

from typing import List
from app.models import User
from app.models import Article


class BothService:
    def __init__(self):
        self.database = Database()
        self.alchemy_db = Db()
        pass

    def get_all_users_with_articles(self):
        users_articles = []
        users_articles = self.alchemy_db.get_all_users_with_articles()
        return users_articles

    def get_users_articles(self):
        users_articles = []
        users_articles = self.alchemy_db.get_users_articles()
        return users_articles
