from app.services import UserService
from typing import List
from app.models import User
from pydantic import Field
from pydantic import BaseModel
from app.database.database import UserDomain


class DeleteUserParams(BaseModel):
    id: int = Field(...)


class UserDeleter:
    def __init__(self):
        pass

    def run(self, params: DeleteUserParams) -> UserDomain:
        user_service = UserService()
        users = user_service.delete_user(params.id)
        return users
