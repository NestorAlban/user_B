from app.services import UserService
from typing import List
from app.models import User
from pydantic import Field
from pydantic import BaseModel

class UserModParams(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    email: str = Field(...)

class UserUpdate:
    def __init__(self):
        pass

    def run(self, params: UserModParams) -> bool:
        users = []
        user_service = UserService()
        users = user_service.update_one_user(params.id, params.name, params.email)
        return users
