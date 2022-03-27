from app.services import UserService
from typing import List
from app.models import User


class OneUserGetter:
    def __init__(self):
        pass

    def run(self, id: int) -> List[User]:
        users = []
        user_service = UserService()
        print("=====================================================")
        users = user_service.get_one_user(id)
        print(users, "2")
        print("=====================================================")
        return users
