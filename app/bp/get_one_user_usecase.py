from ast import Param
from app.services import UserService
from typing import List
from app.models import User
from pydantic import Field
from pydantic import BaseModel
from app.database.database import UserDomain


class OneUserGetterParams(BaseModel):
    id: int = Field(...)


class OneUserGetter:
    def __init__(self):
        pass

    def run(self, params: OneUserGetterParams) -> User:
        user_service = UserService()
        users = user_service.get_one_user(params.id)
        return users
