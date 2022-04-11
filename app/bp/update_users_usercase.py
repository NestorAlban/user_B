from app.services import UserService
from typing import List
from app.models import User
from pydantic import Field
from pydantic import BaseModel


class UserUpdate:
    def __init__(self):
        pass

    def run(self, params: User) -> bool:
        success = False
        user_service = UserService()
        success = user_service.update_one_user(params.id, params.name, params.email, params.updated_at)
        return success
