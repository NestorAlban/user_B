from app.services import UserService
from typing import List
from app.models import User
from pydantic import Field
from pydantic import BaseModel
from app.database.database import UserDomain


class UserCreatorParams(BaseModel):
    name: str = Field(...)
    email: str = Field(...)


class UserCreator:
    def __init__(self):
        pass

    def run(self, params: UserCreatorParams) -> UserDomain:
        user_service = UserService()
        user = user_service.create_user(params.name, params.email)
        return user
