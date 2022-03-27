from app.database import Database
from typing import List
from app.models import User


class UserService:
    def __init__(self):
        pass

    def get_users(self) -> List[User]:
        database = Database()
        users = []
        print("=====================================================")
        users_dict_list = database.get_all_active_users()
        print(users, "3")
        print("=====================================================")
        users = [User(**user_dict) for user_dict in users_dict_list]
        return users

    def create_user(self):
        database = Database()
        users = []
        print(users, "3")
        print("=====================================================")
        users_dict_list = database.create_new_users()
        print(users, "3")
        print("=====================================================")
        users = [User(**user_dict) for user_dict in users_dict_list]
        return users

    def get_one_user(self) -> List[User]:
        database = Database()
        users = []
        print("=====================================================")
        users_dict_list = database.get_one_user()
        idstr = database.get_one_user(idstr)
        print(users, "3")
        print("=====================================================")
        users = [User(**user_dict) for user_dict in users_dict_list]
        return users
