from fastapi import FastAPI
app = FastAPI()
# Path Parameters
@app.get("/users/{user_id}")
def get_user(user_id):
    return {"user_id": user_id}

@app.get("/user/{user_id}/{user_name}")
def get_user_details(user_id:int, user_name:str):
    return {"message": [
        {"user_id": user_id, "user_name": user_name}
    ]}