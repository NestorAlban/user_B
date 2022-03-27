from app.services import UserService
from typing import List
from app.models import User


class OneUserGetter:
    def __init__(self):
        pass

    def run(self) -> List[User]:
        users = []
        user_service = UserService()
        print("=====================================================")
        users = user_service.get_one_user()
        idstr = user_service.get_one_user(idstr)
        print(users, "2")
        print("=====================================================")
        return users
