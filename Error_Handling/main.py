from fastapi import FastAPI, HTTPException,status
app = FastAPI()

users = {
    1: "Alice",
    2: "Bob",
    3: "Charlie"
}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    
    if user_id <=0:
        raise HTTPException(
            status_code = 400,
            detail = "User ID must be a positive integer."
        )
    
    if user_id not in users:
        raise HTTPException(
            status_code = 404,
            detail = "User not found."
        )
    
    return {"user_id": user_id, "name": users[user_id]}