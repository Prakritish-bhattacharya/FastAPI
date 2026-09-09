from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel

app = FastAPI()

# create a User model
class User(BaseModel):
    name: str
    age: int
    email: str

users = {}


# CREATE
@app.post("/users", status_code = status.HTTP_201_CREATED)
def create_user(user: User):
    user_id = len(users) + 1
    
    users[user_id] = user
    return{
        "id": user_id,
        "user": user
    }
    
# READ ALL
@app.get("/users")
def get_users():
    return users

# READ ONE
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(
            status_code = 404,
            detail = "User not found"
        )
    return {
        "id": user_id,
        "user": users[user_id]
    }


# UPDATE
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id not in users:
        raise HTTPException(
            status_code = 404,
            detail = "User not found"
        )
    users[user_id] = user
    return {
        "id": user_id,
        "user": user
    }


# DELETE
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(
            status_code = 404,
            detail = "User not found"
        )
    del users[user_id]
    return {
        "message": "User deleted successfully"
    }