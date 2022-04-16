from app.services import UserService
from typing import List
from app.models import User
from pydantic import Field
from pydantic import BaseModel

class UserStatusModParams(BaseModel):
    id: int = Field(...)
    is_active: bool = Field(...)

class UserStatus:
    def __init__(self):
        pass

    def run(self, params: User) -> bool:
        users = []
        user_service = UserService()
        users = user_service.update_user_status(params.id, params.is_active)
        return users
