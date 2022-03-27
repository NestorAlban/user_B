import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter

from typing import Final
from typing import Dict
from app.bp.create_users_usecase import UserCreator

# from app.database.queries import NAME_KEY
# from app.database.queries import MAIL_KEY
# from app.database.queries import STATUS_KEY
# from app.database.queries import CREATED_KEY
# from app.database.queries import UPDATED_KEY
from app.models.user import User
from app.bp.create_users_usecase import UserCreatorParams


router = APIRouter()

CREATE_USER_ERROR_MESSAGE: Final = "ERROR IN create_user ENDPOINT"
CREATE_USER_ENDPOINT_SUMMARY: Final = "Create a new User"
CREATE_USER_ENDPOINT_PATH: Final = "/create_user"
SUCCESS_KEY: Final = "success"


class CreateUserInput(BaseModel):
    id: int = Field(...)
    name: str = Field(default="Example")
    email: str = Field(default="example@email.com")
    is_active: bool = Field(default=True)


@router.post(
    path=CREATE_USER_ENDPOINT_PATH,
    response_model=Dict[str, bool],
    status_code=status.HTTP_201_CREATED,
    summary=CREATE_USER_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def create_user(new_user_data: User):
    success = False
    try:
        user_creator = UserCreator()
        success = user_creator.run(
            User(
                id=new_user_data.id,
                name=new_user_data.name,
                email=new_user_data.email,
                is_active=new_user_data.is_active,
                created_at=new_user_data.created_at,
                updated_at=new_user_data.updated_at,
            )
        )
    except Exception as error:
        logging.error(CREATE_USER_ERROR_MESSAGE, error)
    return {SUCCESS_KEY: success}
