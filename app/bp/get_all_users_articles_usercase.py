from app.services import BothService
from typing import List
from app.models import User


class AllUsersArticlesGetter:
    def __init__(self):
        pass

    def run(self) -> List[User]:
        users_articles = []
        both_service = BothService()
        users_articles = both_service.get_users()
        return users_articles
