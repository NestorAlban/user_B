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
    __tablename__ = "user_try1"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean(), default=True, nullable=True)
    created_at = Column(DateTime, default=func.now(), nullable=True)
    updated_at = Column(DateTime, default=func.now(), nullable=True, onupdate=func.now())

    # def save(self, *args, **kwargs):
    #     super(User, self).save(*args, **kwargs)
