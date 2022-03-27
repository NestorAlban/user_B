from pydantic import Field
from typing import Optional

from pydantic import BaseModel
from datetime import datetime


class AuditableBase(BaseModel):
    created_at: Optional[str] = Field(default=datetime.today(), nullable=True)
    updated_at: Optional[str] = Field(default=datetime.today(), nullable=True)


class ActiveBase(BaseModel):
    is_active: Optional[bool] = Field(default=True, nullable=True)
