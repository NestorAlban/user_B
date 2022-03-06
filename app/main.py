
from operator import index
from select import select
from turtle import title
from fastapi import FastAPI
from .models import UserBase, Database, query

from fastapi import FastAPI
from fastapi import status
from fastapi import Body, Path
from pydantic import Field

from typing import List

import psycopg2

app=FastAPI()

#table db_persona
NAME_KEY="name"
MAIL_KEY="mail"
Qselect='SELECT * FROM public.db_persona'
Qinsert='INSERT INTO public.db_persona(name, mail) VALUES (%s, %s)'
# Qupdate='UPDATE public.db_persona SET mail=%s  WHERE name=%s;'
# Qdelete='DELETE FROM public.db_persona name=%s;'

@app.get("/")
def home():
    return {"App":"Register a user"}


#show users
@app.get(
    path="/usertests",
    response_model=List[UserBase],
    status_code=status.HTTP_200_OK,
    summary="Show all User tests",
    )
def get_users_tests():
    print("=get users=")
    users_list = []
    db = Database()
    db.connect_db()
    cursor = db.cursor    
    cursor.execute(Qselect)
    users = cursor.fetchall()
    print(users)
    for user in users:
        user = UserBase(
            idper=user["idper"],
            name=user[NAME_KEY].strip(),
            mail=user[MAIL_KEY].strip() if user[MAIL_KEY] else None
        )
        users_list.append(user)
    db.disconnect_db()
    
    return users_list


@app.post(
    path="/registeruser",
    response_model=list[UserBase],
    status_code=status.HTTP_201_CREATED,
    summary="Register a user"
)
def post_a_user(user_register: UserBase=Body(...)):
    print("=register user and show users=")
    users_list = []
    db = Database()
    connect=db.connect_db()
    connect
    cursor = db.cursor
    user_dict=user_register.dict()
    user_dict["idper"]=str(user_dict["idper"])
    user_dict[NAME_KEY]=str(user_dict[NAME_KEY])
    user_dict[MAIL_KEY]=str(user_dict[MAIL_KEY])
    user=(user_dict["idper"],user_dict[NAME_KEY],user_dict[MAIL_KEY])
    user2=(user_dict[NAME_KEY],user_dict[MAIL_KEY])
    cursor.execute(Qselect)
    cursor.execute(Qinsert, user2)
    db.commit_db
    cursor.execute(Qselect)
    users = cursor.fetchall()
    print(users)
    for user in users:
        user = UserBase(
            idper=user["idper"],
            name=user[NAME_KEY].strip(),
            mail=user[MAIL_KEY].strip() if user[MAIL_KEY] else None
        )
        users_list.append(user)
    db.disconnect_db()
    return users_list

@app.delete(
    path="/deleteuser",
    response_model=list[UserBase],
    status_code=status.HTTP_200_OK,
    summary="Delete a user"
)
def delete_a_user():
    pass