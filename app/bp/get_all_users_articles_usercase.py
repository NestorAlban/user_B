from app.services import BothService
from typing import List
from app.models import User


class AllUsersArticlesGetter:
    def __init__(self):
        pass

    def run(self) -> List[User]:
        users = []
        user_service = BothService()
        users = user_service.get_users()
        return users
