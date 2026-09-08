from fastapi import FastAPI
app = FastAPI()

# Query Parameters
@app.get("/Query-products")
def get_products(category:str, limit:int):
    return{"category": category, "limit": limit}

# Query Parameters + Path Parameters
@app.get("/users/{user_id}/orders")
def get_orders(user_id:int, limit:int=10):
    return {"user_id": user_id, "limit": limit}

@app.get("/users/search")
def search_users(name:str, age:int):
    return {"name": name, "age": age}