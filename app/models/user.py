from typing import Final
from pydantic import EmailStr
from pydantic import Field
from app.models.common import AuditableBase
from app.models.common import ActiveBase
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy import func


MIN_NAME_LENGTH: Final = 1
MAX_NAME_LENGTH: Final = 100

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    is_active = Column(Boolean(), default=True, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )
