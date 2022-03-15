from fastapi import FastAPI
from app.models import UserActivate, UserBase, Database


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
Qselect_user = "SELECT * FROM public.user_status WHERE idper="
Qinsert = "INSERT INTO public.user_status(name, mail, active) VALUES (%s, %s, %s)"
Qupdate = "UPDATE public.user_status SET name=%s, mail=%s  WHERE idper=%s"
Qupdate_AD = "UPDATE public.user_status SET active=%s  WHERE idper=%s"
Qdelete = "DELETE FROM public.user_status WHERE idper=%s"


@app.get("/")
def home():
    return {"App": "Register a user"}


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
    summary="Show active Users",
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


@app.get(
    path="/user/{idper}",
    response_model=List[UserActivate],
    status_code=status.HTTP_200_OK,
    summary="Show a user",
)
def get_one_user(idper: int = Path(..., title="User ID")):
    print("=get user=")
    db = Database()
    db.connect_db()
    cursor = db.cursor
    idp = str(idper)
    cursor.execute(Qselect_user + idp)
    users = cursor.fetchall()
    db.disconnect_db()
    print(users)
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
    user_dict[NAME_KEY] = str(user_dict[NAME_KEY])
    user_dict[MAIL_KEY] = str(user_dict[MAIL_KEY])
    user_dict[STATUS_KEY] = str(user_dict[STATUS_KEY])
    user2 = (user_dict[NAME_KEY], user_dict[MAIL_KEY], user_dict[STATUS_KEY])
    cursor.execute(Qinsert, user2)
    db.commit_db()
    cursor.execute(Qselect)
    users = cursor.fetchall()
    print(users)
    db.disconnect_db()
    return users


##########################################################

##Update an user
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
    user2 = (user_dict[NAME_KEY], user_dict[MAIL_KEY], user_dict[ID_KEY])
    cursor.execute(Qupdate, user2)
    db.commit_db()
    cursor.execute(Qselect)
    users = cursor.fetchall()
    up_rows = cursor.rowcount
    db.disconnect_db()
    print(users, up_rows)
    return users


##change status
@app.delete(
    path="/users/{user_id}/usersupdate_status",
    response_model=list[UserActivate],
    status_code=status.HTTP_200_OK,
    summary="Update status",
)
def update_a_user(user_update: UserActivate = Body(...)):
    db = Database()
    db.connect_db()
    cursor = db.cursor
    user_dict = user_update.dict()
    user_dict[ID_KEY] = str(user_dict[ID_KEY])
    user_dict[STATUS_KEY] = bool(user_dict[STATUS_KEY])
    user4 = (user_dict[STATUS_KEY], user_dict[ID_KEY])
    cursor.execute(Qupdate_AD, user4)
    db.commit_db()
    cursor.execute(Qselect)
    users = cursor.fetchall()
    up_rows = cursor.rowcount
    db.disconnect_db()
    print(users, up_rows)
    return users


##########################################################

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
