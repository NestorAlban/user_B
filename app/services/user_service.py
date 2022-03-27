from tkinter import N
from app.database import Database
from typing import List
from app.models import User


class UserService:
    def __init__(self):
        self.database = Database()
        pass

    def get_users(self) -> List[User]:
        users = []
        print("=====================================================")
        users_dict_list = self.database.get_all_active_users()
        print(users_dict_list, "3")
        print("=====================================================")
        users = [User(**user_dict) for user_dict in users_dict_list]
        print(users)
        return users

    def create_user(self, id: int, name: str, email: str) -> bool:
        success = self.database.create_new_user(id, name, email)
        return success
