from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
app = FastAPI()


'''class User(BaseModel):
    username: str
    email: str
    password: str
@app.post("/users", status_code = status.HTTP_202_ACCEPTED)
def create_user(user: User):
    return {"message": "User created successfully", "user": user}'''

'''-------------------------------------------------------'''
'''users = {
    1:"Alice",
    2:"Bob",
    3:"Charlie"
}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return {"user_id": user_id, "username": users[user_id]}'''
    

'''--------------------------------Combining Status Codes + Response Model-----------------------'''
'''class User(BaseModel):
    name:str
    age:int
    email:str

class UserResponse(BaseModel):
    name:str
    email:str

@app.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    return {"name": user.name, "email": user.email}'''

