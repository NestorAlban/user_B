import logging
from fastapi import Body, Path
import psycopg2
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import true as sa_true
from models.user import User
from typing import Final
from typing import List

from psycopg2 import Error
from psycopg2.extras import RealDictCursor
from datetime import datetime
from typing import Optional
from dataclasses import dataclass
from app.database.queries import (
    CREATE_USER_QUERY,
    GET_ALL_ACTIVE_USERS_QUERY,
    GET_ONE_USER_QUERY,
    UPDATE_USER_DATA_QUERY,
    UPDATE_USER_STATUS_QUERY,
)

logger = logging.getLogger(__name__)
logger.level = logger.setLevel(logging.INFO)
DATABASE_CONNECTION_ERROR: Final = "Error while connecting to PostgreSQL"
CLOSED_DATABASE_MESSAGE: Final = "PostgreSQL connection is closed"
CONNECTING_DB_MESSAGE: Final = "Connecting PostgreSQL database======"


class Database:
    def __init__(self):
        self.database_user = os.getenv("DATABASE_USER")
        self.database_password = os.getenv("DATABASE_PASSWORD")
        self.database_host = os.getenv("DATABASE_HOST")
        self.database_port = os.getenv("DATABASE_PORT")
        self.database_name = os.getenv("DATABASE_NAME")
        self.cursor = None
        self.connection = None

    def connect(self):
        try:
            # Connect to an existing database
            self.connection = psycopg2.connect(
                user=self.database_user,
                password=self.database_password,
                host=self.database_host,
                port=self.database_port,
                database=self.database_name,
            )

            # Create a cursor to perform database operations
            self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        except (Exception, Error) as error:
            logging.error(DATABASE_CONNECTION_ERROR, error)
        return

    def disconnect(self):
        self.cursor.close()
        self.connection.close()
        logging.info(CLOSED_DATABASE_MESSAGE)
        return

    def commit(self):
        self.connection.commit()
        return

    def get_all_active_users(self) -> List[RealDictCursor]:
        users = []
        query = GET_ALL_ACTIVE_USERS_QUERY
        self.connect()
        self.cursor.execute(query)
        users = self.cursor.fetchall()
        self.disconnect()
        return users

    def create_new_user(
        self, id: int, name: str, email: str, is_active: bool, created_at: str, updated_at: str
    ) -> bool:
        success = False
        try:
            query = CREATE_USER_QUERY
            self.connect()
            self.cursor.execute(query, (name, email, is_active, created_at, updated_at))
            self.commit()
            self.disconnect()
            success = True
        except Exception as e:
            logging("DB ERROR", e)
        return success

    def get_one_user(self, id: int = Path(..., title="User ID")) -> List[RealDictCursor]:
        users = []
        query = GET_ONE_USER_QUERY
        self.connect()
        self.cursor.execute(query + str(id))
        users = self.cursor.fetchall()
        self.disconnect()
        return users

    def update_one_user(self, id: int, name: str, email: str, updated_at: str) -> bool:
        success = False
        try:
            query = UPDATE_USER_DATA_QUERY
            self.connect()
            self.cursor.execute(query, (name, email, updated_at, str(id)))
            self.commit()
            self.disconnect()
            success = True
        except Exception as e:
            logging("DB ERROR", e)
        return success

    def update_user_status(self, id: int, is_active: str, updated_at: str) -> bool:
        success = False
        try:
            query = UPDATE_USER_STATUS_QUERY
            self.connect()
            self.cursor.execute(query, (bool(is_active), updated_at, str(id)))
            self.commit()
            self.disconnect()
            success = True
        except Exception as e:
            logging("DB ERROR", e)
        return success


@dataclass(frozen=True)
class UserDomain:
    id: int
    name: str
    email: str
    is_active: Optional[bool]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class Db:
    def __init__(self) -> None:
        engine = create_engine("postgresql://postgres:postgres@127.0.0.1:5445/bd-users", echo=True, future=True)
        Session = sessionmaker(engine)
        self.session = Session()
        # Base.metadata.create_all(engine)

    def get_all_active_users(self):
        users = self.session.query(User).filter(User.is_active == sa_true()).all()
        return users

    def create_user(self, name, email):
        user = User(name=name, email=email)
        self.session.add(user)
        self.session.commit()
        user_domain = UserDomain(user.id, user.name, user.email, user.is_active, user.created_at, user.updated_at)
        return user_domain
