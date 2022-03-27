from app.services import UserService
from typing import List
from app.models import User
from pydantic import Field
from pydantic import BaseModel


class UserCreatorParams(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    email: str = Field(...)
    is_active: bool = Field(...)


class UserCreator:
    def __init__(self):
        pass

    def run(self, params: User) -> bool:
        success = False
        user_service = UserService()
        success = user_service.create_user(
            params.id, params.name, params.email, params.is_active, params.created_at, params.updated_at
        )
        return success
