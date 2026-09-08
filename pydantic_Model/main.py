'''
==============================================
            Pydantic Models
==============================================
'''
# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Optional
# app = FastAPI()

# class User(BaseModel):
#     name: str
#     age: int
#     email: str
#     phone: Optional[str] = None

# @app.post("/users")
# def create_user(user: User):
#     return {
#         "message": "User created successfully.",
#         "user": user
#     } 


'''
Request Model vs Response Model
'''
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


# Request Model
class User(BaseModel):
    name: str
    age: Optional[int] = None
    email: str
    password: str


# Response Model
class UserResponse(BaseModel):
    name: str
    email: str


@app.post("/users", response_model=UserResponse)
def create_user(user: User):
    return {
        "name": user.name,
        "email": user.email
    }