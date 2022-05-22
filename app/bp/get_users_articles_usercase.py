from app.services import BothService
from typing import List
from app.models import User


class UsersArticlesGetter:
    def __init__(self):
        pass

    def run(self):
        users_articles = []
        both_service = BothService()
        users_articles = both_service.get_users_articles()
        return users_articles