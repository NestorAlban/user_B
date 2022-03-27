from app.database import Database
from typing import List
from app.models import User


class UserService:
    def __init__(self):
        pass

    def get_users(self) -> List[User]:
        database = Database()
        users = []
        users_dict_list = database.get_all_active_users()
        users = [User(**user_dict) for user_dict in users_dict_list]
        return users
