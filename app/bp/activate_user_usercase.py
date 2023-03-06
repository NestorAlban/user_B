from app.services import UserService
from pydantic import Field
from pydantic import BaseModel
from app.database.database import UserDomain


class ActivateUserParams(BaseModel):
    id: int = Field(...)


class UserActivator:
    def __init__(self):
        pass

    def run(self, params: ActivateUserParams) -> UserDomain:
        user_service = UserService()
        user = user_service.activate_user(params.id)
        return user
