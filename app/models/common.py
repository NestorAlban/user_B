from pydantic import Field
from pydantic import BaseModel
from datetime import datetime


class AuditableBase(BaseModel):
    created_at: str = Field(default=datetime.today())
    updated_at: str = Field(default=datetime.today())


class ActiveBase(BaseModel):
    is_active: bool = Field(default=True)
