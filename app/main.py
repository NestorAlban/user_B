from fastapi import FastAPI
from .models import UserActivate, UserBase, Database

from fastapi import FastAPI
from fastapi import status
from fastapi import Body, Path
from pydantic import Field

from typing import List

import psycopg2


app = FastAPI()

# table db_persona
# table user_status
ID_KEY = "idper"
NAME_KEY = "name"
MAIL_KEY = "mail"
STATUS_KEY = "active"
Qselect = "SELECT * FROM public.user_status"
Qselect_acive = "SELECT idper, name, mail FROM public.user_status WHERE active=true"
Qinsert = "INSERT INTO public.user_status(name, mail, active) VALUES (%s, %s, %s)"
Qupdate = "UPDATE public.user_status SET name=%s, mail=%s  WHERE idper=%s"
Qupdate_AD = "UPDATE public.user_status SET active=%s  WHERE idper=%s"
Qdelete = "DELETE FROM public.user_status WHERE idper=%s"


@app.get("/")
def home():
    return {"App": "Register a user"}


# show users
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
    # rows=db.rows_count
    rows_co = 0
    # print(users, rows)
    for user in users:
        user = UserBase(
            idper=user[ID_KEY],
            name=user[NAME_KEY].strip(),
            mail=user[MAIL_KEY].strip() if user[MAIL_KEY] else None,
        )
        rows_co += 1
        users_list.append(user)
    db.disconnect_db()
    print(users, rows_co)
    return users_list


##########################################################
###show all user
@app.get(
    path="/usertests_simple",
    response_model=List[UserActivate],
    status_code=status.HTTP_200_OK,
    summary="Show all User tests",
)
def get_users_tests():
    print("=get users=")
    db = Database()
    db.connect_db()
    cursor = db.cursor
    cursor.execute(Qselect)
    users = cursor.fetchall()
    up_rows = cursor.rowcount
    db.disconnect_db()
    print(users, up_rows)
    return users


###show active users
@app.get(
    path="/usertests_active",
    response_model=List[UserBase],
    status_code=status.HTTP_200_OK,
    summary="Show all User tests",
)
def get_users_tests():
    print("=get users=")
    db = Database()
    db.connect_db()
    cursor = db.cursor
    cursor.execute(Qselect_acive)
    users = cursor.fetchall()
    up_rows = cursor.rowcount
    db.disconnect_db()
    print(users, up_rows)
    return users


##########################################################


# Create an user
@app.post(
    path="/registeruser",
    response_model=list[UserBase],
    status_code=status.HTTP_201_CREATED,
    summary="Register a user",
)
def post_a_user(user_register: UserBase = Body(...)):
    print("=register user and show users=")
    users_list = []
    db = Database()
    connect = db.connect_db()
    connect
    cursor = db.cursor
    user_dict = user_register.dict()
    user_dict[ID_KEY] = str(user_dict[ID_KEY])
    user_dict[NAME_KEY] = str(user_dict[NAME_KEY])
    user_dict[MAIL_KEY] = str(user_dict[MAIL_KEY])
    user = (user_dict[ID_KEY], user_dict[NAME_KEY], user_dict[MAIL_KEY])
    user2 = (user_dict[NAME_KEY], user_dict[MAIL_KEY])
    cursor.execute(Qselect)
    cursor.execute(Qinsert, user2)
    db.commit_db()
    cursor.execute(Qselect)
    users = cursor.fetchall()
    print(users)
    for user in users:
        user = UserBase(
            idper=user[ID_KEY],
            name=user[NAME_KEY].strip(),
            mail=user[MAIL_KEY].strip() if user[MAIL_KEY] else None,
        )
        users_list.append(user)
    db.disconnect_db()
    return users_list


##same as the one before
@app.post(
    path="/registeruser_simple",
    response_model=list[UserBase],
    status_code=status.HTTP_201_CREATED,
    summary="Register a user",
)
def post_a_user(user_register: UserBase = Body(...)):
    print("=register user and show users=")
    db = Database()
    db.connect_db()
    cursor = db.cursor
    user_dict = user_register.dict()
    user_dict[ID_KEY] = str(user_dict[ID_KEY])
    user_dict[NAME_KEY] = str(user_dict[NAME_KEY])
    user_dict[MAIL_KEY] = str(user_dict[MAIL_KEY])
    user2 = (user_dict[NAME_KEY], user_dict[MAIL_KEY])
    cursor.execute(Qselect)
    cursor.execute(Qinsert, user2)
    db.commit_db()
    cursor.execute(Qselect)
    users = cursor.fetchall()
    print(users)
    db.disconnect_db()
    return users


##########################################################
#####create a user with status
@app.post(
    path="/registeruser_status",
    response_model=list[UserBase],
    status_code=status.HTTP_201_CREATED,
    summary="Register a user",
)
def post_a_user(user_register: UserActivate = Body(...)):
    print("=register user and show users=")
    db = Database()
    db.connect_db()
    cursor = db.cursor
    user_dict = user_register.dict()
    user_dict[ID_KEY] = str(user_dict[ID_KEY])
    user_dict[NAME_KEY] = str(user_dict[NAME_KEY])
    user_dict[MAIL_KEY] = str(user_dict[MAIL_KEY])
    user_dict[STATUS_KEY] = str(user_dict[STATUS_KEY])
    user2 = (user_dict[NAME_KEY], user_dict[MAIL_KEY], user_dict[STATUS_KEY])
    cursor.execute(Qselect)
    cursor.execute(Qinsert, user2)
    db.commit_db()
    cursor.execute(Qselect)
    users = cursor.fetchall()
    print(users)
    db.disconnect_db()
    return users


##########################################################


# Update an user (in process)
@app.put(
    path="/users/{user_id}/usersupdate",
    response_model=list[UserBase],
    status_code=status.HTTP_200_OK,
    summary="Update user",
)
def update_a_user(user_update: UserBase = Body(...)):
    users_list = []
    db = Database()
    connect = db.connect_db()
    connect
    cursor = db.cursor
    user_dict = user_update.dict()
    user_dict[ID_KEY] = str(user_dict[ID_KEY])
    user_dict[NAME_KEY] = str(user_dict[NAME_KEY])
    user_dict[MAIL_KEY] = str(user_dict[MAIL_KEY])
    user = (user_dict[ID_KEY], user_dict[NAME_KEY], user_dict[MAIL_KEY])
    user2 = (user_dict[NAME_KEY], user_dict[MAIL_KEY], user_dict[ID_KEY])
    cursor.execute(Qselect)
    cursor.execute(Qupdate, user2)
    db.commit_db()
    cursor.execute(Qselect)
    users = cursor.fetchall()
    print(users)
    for user in users:
        user = UserBase(
            idper=user[ID_KEY],
            name=user[NAME_KEY].strip(),
            mail=user[MAIL_KEY].strip() if user[MAIL_KEY] else None,
        )
        users_list.append(user)

    db.disconnect_db()
    return users_list


##########################################################
##in process
@app.put(
    path="/users/{user_id}/usersupdate_simple",
    response_model=list[UserBase],
    status_code=status.HTTP_200_OK,
    summary="Update id",
)
def update_a_user(user_update: UserBase = Body(...)):
    db = Database()
    db.connect_db()
    cursor = db.cursor
    user_dict = user_update.dict()
    user_dict[ID_KEY] = str(user_dict[ID_KEY])
    user_dict[NAME_KEY] = str(user_dict[NAME_KEY])
    user_dict[MAIL_KEY] = str(user_dict[MAIL_KEY])
    user = (user_dict[ID_KEY], user_dict[NAME_KEY], user_dict[MAIL_KEY])
    user2 = (user_dict[NAME_KEY], user_dict[MAIL_KEY], user_dict[ID_KEY])
    cursor.execute(Qselect)
    cursor.execute(Qupdate, user2)
    db.commit_db()
    cursor.execute(Qselect)
    users = cursor.fetchall()
    up_rows = cursor.rowcount
    db.disconnect_db()
    print(users, up_rows)
    return users


##change status
@app.put(
    path="/users/{user_id}/usersupdate_status",
    response_model=list[UserActivate],
    status_code=status.HTTP_200_OK,
    summary="Update id",
)
def update_a_user(user_update: UserActivate = Body(...)):
    db = Database()
    db.connect_db()
    cursor = db.cursor
    user_dict = user_update.dict()
    user_dict[ID_KEY] = str(user_dict[ID_KEY])
    user_dict[STATUS_KEY] = bool(user_dict[STATUS_KEY])
    user4 = (user_dict[STATUS_KEY], user_dict[ID_KEY])
    cursor.execute(Qselect)
    cursor.execute(Qupdate_AD, user4)
    db.commit_db()
    cursor.execute(Qselect)
    users = cursor.fetchall()
    up_rows = cursor.rowcount
    db.disconnect_db()
    print(users, up_rows)
    return users


##########################################################


# Delete an user
@app.delete(
    path="/users/{user_id}/deleteuser",
    response_model=list[UserBase],
    status_code=status.HTTP_200_OK,
    summary="Delete a user",
)
def delete_a_user(user_delete: UserBase = Body(...)):
    users_list = []
    db = Database()
    connect = db.connect_db()
    connect
    cursor = db.cursor
    user_dict = user_delete.dict()
    user_dict[ID_KEY] = str(user_dict[ID_KEY])
    user_dict[NAME_KEY] = str(user_dict[NAME_KEY])
    user_dict[MAIL_KEY] = str(user_dict[MAIL_KEY])
    user3 = user_dict[ID_KEY]
    cursor.execute(Qselect)
    cursor.execute(Qdelete, user3)
    db.commit_db()
    cursor.execute(Qselect)
    users = cursor.fetchall()
    print(users)
    for user in users:
        user = UserBase(
            idper=user[ID_KEY],
            name=user[NAME_KEY].strip(),
            mail=user[MAIL_KEY].strip() if user[MAIL_KEY] else None,
        )
        users_list.append(user)
    db.disconnect_db()
    return users_list


##same as the one before (can use 2 digits in id)
@app.delete(
    path="/users/{user_id}/deleteuser_simple",
    response_model=list[UserBase],
    status_code=status.HTTP_200_OK,
    summary="Delete a user",
)
def delete_a_user(user_delete: UserBase = Body(...)):
    db = Database()
    db.connect_db()
    cursor = db.cursor
    user_dict = user_delete.dict()
    user_dict[ID_KEY] = str(user_dict[ID_KEY])
    user_dict[NAME_KEY] = str(user_dict[NAME_KEY])
    user_dict[MAIL_KEY] = str(user_dict[MAIL_KEY])
    user3 = user_dict[ID_KEY]
    cursor.execute(Qselect)
    cursor.execute("DELETE FROM public.db_persona WHERE idper=" + user3)
    db.commit_db()
    cursor.execute(Qselect)
    users = cursor.fetchall()
    up_rows = cursor.rowcount
    db.disconnect_db()
    print(users, up_rows)
    return users
