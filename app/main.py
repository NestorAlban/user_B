
from fastapi import FastAPI
from .models import UserBase, Database

from fastapi import FastAPI
from fastapi import status
from fastapi import Body

from typing import List


app=FastAPI()
MAIL_KEY="mail"


@app.get("/")
def home():
    return {"App":"Register a user"}

#create user
# @app.post(
#     path="/createuser",
#     response_model=UserBase,
#     status_code=status.HTTP_201_CREATED,
#     summary="Register a User"
#     )

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
    cursor.execute('SELECT * FROM public."ejemplo-user"')
    users = cursor.fetchall()
    print(users)
    for user in users:
        user = UserBase(
            # id=user['id'],
            name=user['name'].strip(),
            mail=user[MAIL_KEY].strip() if user[MAIL_KEY] else None
            # is_active=user['is_active'],
            # status=user['status']
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
    user_dict["name"]=str(user_dict["name"])
    user_dict["mail"]=str(user_dict["mail"])
    user=(user_dict["name"],user_dict["mail"])
    insert_query= 'INSERT INTO public."ejemplo-user"(name, mail) VALUES (%s, %s)'

    cursor.execute('SELECT * FROM public."ejemplo-user"')
    cursor.execute(insert_query, user)
    db.commit_db
    cursor.execute('SELECT * FROM public."ejemplo-user"')
    users = cursor.fetchall()
    print(users)
    for user in users:
        user = UserBase(
            # id=user['id'],
            name=user['name'].strip(),
            mail=user[MAIL_KEY].strip() if user[MAIL_KEY] else None
            # is_active=user['is_active'],
            # status=user['status']
        )
        users_list.append(user)
    db.disconnect_db()
    return users_list
