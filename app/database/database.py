import logging
from fastapi import Body, Path
import psycopg2
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import true as sa_true
from sqlalchemy.exc import IntegrityError

# from models.user import User
from app.models.user import User
from app.models.user import Article
from app.models.user import Base
from typing import Final
from typing import List


from psycopg2 import Error
from psycopg2.extras import RealDictCursor
from psycopg2.errors import UniqueViolation
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
DELETED_USER: Final = False
ACTIVE_USER: Final = True


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


@dataclass(frozen=True)
class ArticleDomain:
    id: int
    title: str
    published_at: Optional[datetime]
    autor_id: int
    


class Db:
    name = "Boris"

    def __init__(self) -> None:
        self.database_user = os.getenv("DATABASE_USER")
        self.database_password = os.getenv("DATABASE_PASSWORD")
        self.database_host = os.getenv("DATABASE_HOST")
        self.database_port = os.getenv("DATABASE_PORT")
        self.database_name = os.getenv("DATABASE_NAME")
        self.engine = create_engine(
            f"postgresql://{self.database_user}:{self.database_password}@{self.database_host}:{self.database_port}/{self.database_name}",
            echo=True,
            future=True,
        )
        Session = sessionmaker(self.engine)
        self.session = Session()
        # Base.metadata.create_all(self.engine)

    ##Users

    # @classmethod
    @staticmethod
    def create_user_domain(user):
        user_domain = UserDomain(
            user.id, 
            user.name, 
            user.email, 
            user.is_active, 
            user.created_at, 
            user.updated_at
        )
        return user_domain

    def get_all_users(self):
        users = self.session.query(User).all()
        for user_object in users:
            print(user_object)
            if user_object:
                user_domain=Db.create_user_domain(user_object)
                print("============================================")
                print(user_domain)
                print(type(user_domain))
                print(user_domain.id)
                print("============================================")
        self.session.close()
        # user_response=[UserDomain(**user.__dict__) for user in users]
        # print(user_response)
        return users

    def get_all_active_users(self):
        users = self.session.query(User).filter(User.is_active == sa_true()).all()
        self.session.close()
        return users

    def create_user(self, name, email):
        user_domain = None
        user = User(name=name, email=email)
        try:
            if user:
                self.session.add(user)
                self.session.commit()
                user_domain = Db.create_user_domain(user)
                print("============================")
                print(user_domain.id)
                print("============================")
        except IntegrityError as e:
            assert isinstance(e.orig, UniqueViolation)
        self.session.close()
        return user_domain

    def get_one_u(self, id):
        user = None
        user = self.session.query(User).filter(User.id == id).first()
        self.session.close()
        return user

    def up_one_user(self, id, name, email):
        # users = self.session.query(User).filter(User.id == id).update(
        #     {
        #         User.name: name,
        #         User.email: email
        #     }
        # )
        user_domain = None
        user = self.session.query(User).filter(User.id == id).first()
        if user:
            user.name = name
            user.email = email
            self.session.commit()
            user_domain = Db.create_user_domain(user)
        self.session.close()
        return user_domain

    def up_user_status(self, id, is_active):
        users = self.session.query(User).filter(User.id == id).update({User.is_active: is_active})
        self.session.commit()
        users2 = self.session.query(User).filter(User.id == id)
        self.session.close()
        return users2

    def delete_user(self, id) -> UserDomain:
        # users = self.session.query(User).filter(User.id == id).update(
        #     {
        #         User.is_active: DELETED_USER
        #     }
        # )
        # self.session.commit()
        # users2 = self.session.query(User).filter(User.id == id)
        # return users2
        user_domain = None
        user_first = self.session.query(User).filter(User.id == id).first()
        print("============================================")
        print(user_first)
        print(type(user_first))
        print("============================================")
        if user_first:
            user_first.is_active = DELETED_USER
            self.session.commit()
            user_domain = Db.create_user_domain(user_first)
            print("============================================")
            print(user_domain)
            print(type(user_domain))
            print(user_domain.id)
            print("============================================")
        self.session.close()
        return user_domain

    def activate_user(self, id: int) -> UserDomain:
        user_domain = None
        user_first = self.session.query(User).filter(User.id == id).first()
        if user_first:
            user_first.is_active = ACTIVE_USER
            self.session.commit()
            user_domain = Db.create_user_domain(user_first)
        self.session.close()
        return user_domain


    ##Articles
    
    # @classmethod
    @staticmethod
    def create_article_domain(article):
        article_domain = ArticleDomain(
            article.id, 
            article.title, 
            article.published_at, 
            article.autor_id
        )
        return article_domain

    def get_all_articles(self):
        articles = self.session.query(Article).all()
        self.session.close()
        return articles

    def create_article(self, title, autor_id):
        article_domain = None
        user_domain = None
        users = None
        users = self.session.query(User).all()
        article = Article(
            title = title, 
            autor_id = autor_id
        )
        try:
            if users:
                for user in users:
                    if user:
                        user_domain = Db.create_user_domain(user)
                        print(user_domain.id, autor_id)
                        if user_domain.id == autor_id:
                            if article:
                                self.session.add(article)
                                self.session.commit()
                                article_domain = Db.create_article_domain(article)
        except IntegrityError as e:
            assert isinstance(e.orig, UniqueViolation)
        self.session.close()
        return article_domain


