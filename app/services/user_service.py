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

    def create_user(self, id: int, name: str, email: str) -> bool:
        user = self.alchemy_db.create_user(name, email)
        return user
