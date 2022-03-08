from uuid import UUID
from pydantic import EmailStr
from pydantic import Field
from pydantic import BaseModel

import psycopg2
from psycopg2 import Error
from psycopg2.extras import RealDictCursor

class Database:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.rows_count=0
    
    def connect_db(self):
        try:
            # Connect to an existing database
            self.connection = psycopg2.connect(user="postgres",
                                        password="12345",
                                        host="localhost",
                                        port="5432",
                                        database="bd-users")

            # Create a cursor to perform database operations
            self.cursor = self.connection.cursor(cursor_factory = RealDictCursor)
        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def disconnect_db(self):
        self.cursor.close()
        self.connection.close()
        print("PostgreSQL connection is closed")
    
    def commit_db(self):
        self.connection.commit()
    
    # def count(self):
    #     self.rows_count=self.cursor.rowcount
    #     self.rows_number=self.cursor.rownumber

    

class query():
    qselect='SELECT * FROM public."ejemplo-user"'
    qinsert='INSERT INTO public."ejemplo-user"(name, mail) VALUES (%s, %s)'
    qupdate='UPDATE public."ejemplo-user" SET mail=%s  WHERE name=%s;'

class UserBase(BaseModel):
    # user_id: UUID = Field(...)
    idper: int= Field(
        ...
    )
    mail: EmailStr = Field(
        ...
        )
    name: str=Field(
        ...,
        min_length=1,
        max_length=100
    )

class  UserActivate(UserBase):
    active: bool

# db=Database()
# #print(db)
# db.connect_db()
# cur=db.cursor
# # b=db.cursor
# users = cur.fetchall()
# print(users)
#print (connect_db())