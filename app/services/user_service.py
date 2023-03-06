from tkinter import N
from app.database import Database
from app.database import Db
from app.database import UserDomain
from app.database import ArticleDomain

from typing import List
from app.models import User
from app.models import Article


class UserService:
    def __init__(self):
        self.database = Database()
        self.alchemy_db = Db()
        pass

    def get_users(self) -> List[User]:
        users = []
        users = self.alchemy_db.get_all_active_users()
        return users

    def create_user(self, name: str, email: str) -> UserDomain:
        user = self.alchemy_db.create_user(name, email)
        return user

    def get_one_user(self, id: int) -> User:
        user = self.alchemy_db.get_one_u(id)
        return user

    def update_one_user(self, id: int, name: str, email: str) -> UserDomain:
        users = self.alchemy_db.up_one_user(id, name, email)
        return users

    def update_user_status(self, id: int, is_active: bool) -> UserDomain:
        users = []
        users = self.alchemy_db.up_user_status(id, is_active)
        return users

    def get_all_users(self) -> List[User]:
        users = []
        users = self.alchemy_db.get_all_users()
        return users

    def delete_user(self, id: int) -> UserDomain:
        users = self.alchemy_db.delete_user(id)
        return users

    def activate_user(self, id: int) -> UserDomain:
        user = self.alchemy_db.activate_user(id)
        return user

    def get_users_simple(self):
        users = []
        users = self.alchemy_db.get_all_users()
        return users
