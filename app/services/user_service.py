from tkinter import N
from app.database import Database
from app.database import Db

from typing import List
from app.models import User


class UserService:
    def __init__(self):
        self.database = Database()
        self.alchemy_db = Db()
        pass

    def get_users(self) -> List[User]:
        users = []
        users = self.alchemy_db.get_all_active_users()
        return users

    def create_user(self, name: str, email: str):
        user = self.alchemy_db.create_user(name, email)
        # print(f"user S:{user}")
        return user

    def get_one_user(self, id: int) -> List[User]:
        users = []
        users_dict_list = self.database.get_one_user(id)
        users = [User(**user_dict) for user_dict in users_dict_list]
        print(users)
        return users

    def update_one_user(self, id: int, name: str, email: str, updated_at: str) -> bool:
        success = self.database.update_one_user(id, name, email, updated_at)
        return success

    def update_user_status(self, id: int, is_active: bool, updated_at: str) -> bool:
        success = self.database.update_user_status(id, is_active, updated_at)
        return success
