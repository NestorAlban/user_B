from typing import Final
from pydantic import EmailStr
from pydantic import Field
from app.models.common import AuditableBase
from app.models.common import ActiveBase


MIN_NAME_LENGTH: Final = 1
MAX_NAME_LENGTH: Final = 100


class User(AuditableBase, ActiveBase):
    id: int = Field()
    name: str = Field(default="Example", min_length=MIN_NAME_LENGTH, max_length=MAX_NAME_LENGTH)
    email: EmailStr = Field(default="example@email.com")
