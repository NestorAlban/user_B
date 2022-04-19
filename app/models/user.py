from typing import Final
from colorama import Fore
from pydantic import EmailStr
from pydantic import Field
from app.models.common import AuditableBase
from app.models.common import ActiveBase
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, String, Integer, DateTime, Boolean
from sqlalchemy import func
from sqlalchemy.orm import relationship


MIN_NAME_LENGTH: Final = 1
MAX_NAME_LENGTH: Final = 100

Base = declarative_base()


class User(Base):
    __tablename__ = "user_try1"

    id = Column(
        Integer, 
        primary_key = True
    )
    name = Column(
        String, 
        nullable = False, 
        unique = True
    )
    email = Column(
        String, 
        nullable = False, 
        unique = True
    )
    is_active = Column(
        Boolean(), 
        default = True, 
        nullable = True
    )
    created_at = Column(
        DateTime, 
        default = func.now(), 
        nullable = True
    )
    updated_at = Column(
        DateTime, 
        default = func.now(), 
        nullable = True, 
        onupdate = func.now()
    )
    articles = relationship('Article')
    # def save(self, *args, **kwargs):
    #     super(User, self).save(*args, **kwargs)

class Article(Base):
    __tablename__ = "articles"

    id = Column(
        Integer, 
        primary_key = True
    )
    title = Column(
        String,
        nullable = False
    )
    published_at = Column(
        DateTime, 
        default = func.now(), 
        nullable = True
    )
    autor_id = Column(
        Integer,
        ForeignKey(User.id),
        nullable = False
    )
    autor = relationship(
        User,
        back_populates = 'articles'
    )
    
