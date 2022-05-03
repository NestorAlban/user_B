from app.services import BothService
from typing import List
from app.models import User


class AllUsersWithArticlesGetter:
    def __init__(self):
        pass

    def run(self):
        users_articles = []
        both_service = BothService()
        users_articles = both_service.get_all_users_with_articles()
        return users_articles
