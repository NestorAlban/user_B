from app.services import UserService
from typing import List
from app.models import User


class UserCreator:
    def __init__(self):
        pass

    def run(self) -> List[User]:
        users = []
        user_service = UserService()
        print(users, "2")
        print("=====================================================")
        users = user_service.create_user()
        print(users, "2")
        print("=====================================================")
        return users
