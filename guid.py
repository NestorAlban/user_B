def pass_file():
    pass
# Python
import json
from uuid import UUID
from datetime import date, datetime
from typing import Optional, List

#  Pydantic
from pydantic import BaseModel
from pydantic.networks import EmailStr
from pydantic import Field

#  FastAPI
from fastapi import FastAPI, status, HTTPException
from fastapi import Body, Form, Path

app = FastAPI()

# Models

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(
        ..., 
        min_length=8,
        max_length=64
    )

class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)

class UserRegister(User):
    password: str = Field(
        ..., 
        min_length=8,
        max_length=64
    )

class LoginOut(BaseModel): 
    email: EmailStr = Field(...)
    message: str = Field(default="Login Successfully!")


### Delete a user
@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
    )
def delete_a_user(
    user_id: UUID = Path(
        ...,
        title="User ID",
        description="This is the user ID",
        example="3fa85f64-5717-4562-b3fc-2c963f66afa1"
    )):

    with open("users.json", "r+", encoding="utf-8") as f: 
        results = json.loads(f.read())
        id = str(user_id)
    for data in results:
        if data["user_id"] == id:
            results.remove(data)
            with open("users.json", "w", encoding="utf-8") as f:
                f.seek(0)
                f.write(json.dumps(results))
            return data
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="¡This user_id doesn't exist!"
        )

### Update a user
@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tags=["Users"]
    )
def update_a_user(
        user_id: UUID = Path(
            ...,
            title="User ID",
            description="This is the user ID",
            example="3fa85f64-5717-4562-b3fc-2c963f66afa3"
        ),
        user: UserRegister = Body(...)
    ):
    """
    Update User

    This path operation update a user information in the app and save in the database

    Parameters:
    - user_id: UUID
    - Request body parameter:
        - **user: User** -> A user model with user_id, email, first name, last name, birth date and password
    
    Returns a user model with user_id, email, first_name, last_name and birth_date
    """
    user_id = str(user_id)
    user_dict = user.dict()
    user_dict["user_id"] = str(user_dict["user_id"])
    user_dict["birth_date"] = str(user_dict["birth_date"])
    with open("users.json", "r+", encoding="utf-8") as f: 
        results = json.loads(f.read())
    for user in results:
        if user["user_id"] == user_id:
            results[results.index(user)] = user_dict
            with open("users.json", "w", encoding="utf-8") as f:
                f.seek(0)
                f.write(json.dumps(results))
            return user
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="¡This user_id doesn't exist!"
        )

