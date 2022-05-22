from app.services import UserService
from typing import List
from app.models import User


class AllUsersSimpleGetter:
    def __init__(self):
        pass

    def run(self):
        users = []
        user_service = UserService()
        users = user_service.get_users_simple()
        return users