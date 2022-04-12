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
        users = self.alchemy_db.get_one_u(id)
        return users

    def update_one_user(self, id: int, name: str, email: str) -> bool:
        users = []
        users = self.alchemy_db.up_one_user(id, name, email)
        return users

    def update_user_status(self, id: int, is_active: bool) -> bool:
        users = []
        users = self.alchemy_db.up_user_status(id, is_active)
        return users

    def get_all_users(self):
        users = []
        users = self.alchemy_db.get_all_users()
        return users
