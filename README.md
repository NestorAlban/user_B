# users_B
fastapi to create a user

- Create POST endpoint ('createuser')
- Create that receives name, email as parameters(body)
- Connect with Postgresql and creates a new record in user_test table
- Return record created

1. Run DB:
    - Run with docker
        ```shell
        docker-compose up -d db
        ```

2. Run fastapi
    - Run with uvicorn
        ```shell
        python -m uvicorn app.main:app --host 0.0.0.0
        ```


# @app.put(
#     path="/updateuser",
#     response_model=list[UserBase],
#     status_code=status.HTTP_200_OK,
#     summary="Update a user"
# )
# def update_a_user(user_update: UserBase=Body(...)):
#     print("=update user and show users=")
#     users_list = []
#     db = Database()
#     connect=db.connect_db()
#     connect
#     cursor = db.cursor
#     user_dict=user_update.dict()
#     user_dict["name"]=str(user_dict["name"])
#     user_dict["mail"]=str(user_dict["mail"])
#     user=(user_dict["name"],user_dict["mail"])
#     cursor.execute('SELECT * FROM public."ejemplo-user"')
#     cursor.execute(update, user)
#     db.commit_db()
#     cursor.execute('SELECT * FROM public."ejemplo-user"')
#     users = cursor.fetchall()
#     print(users)
#     for user in users:
#         user = UserBase(
#             # id=user['id'],
#             name=user['name'].strip(),
#             mail=user[MAIL_KEY].strip() if user[MAIL_KEY] else None
#             # is_active=user['is_active'],
#             # status=user['status']
#         )
#         users_list.append(user)
#     db.disconnect_db()
#     return users_list
