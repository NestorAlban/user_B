import logging
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
from app.database.queries import CREATE_USER_QUERY, GET_ALL_ACTIVE_USERS_QUERY
from models.user import Base

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

    def create_new_user(self, id: int, name: str, email: str) -> bool:
        success = False
        try:
            query = CREATE_USER_QUERY
            self.connect()
            self.cursor.execute(query, (id, name, email))
            self.commit()
            self.disconnect()
            success = True
        except Exception as e:
            logging("DB ERROR", e)
        return success


class Db:
    def __init__(self) -> None:
        engine = create_engine("postgresql://postgres:postgres@127.0.0.1:5445/bd-users", echo=True, future=True)
        Session = sessionmaker(engine)
        self.session = Session()
        Base.metadata.create_all(engine)

    def get_all_active_users(self):
        users = self.session.query(User).filter(User.is_active == sa_true()).all()
        return users

    def create_user(self, name, email):
        user = User(name=name, email=email)
        self.session.add(user)
        self.session.commit()
        return user
