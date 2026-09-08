from fastapi import FastAPI, HTTPException, Depends
app = FastAPI()

def common_parameters(skip: int = 0,limit: int = 10):
    return {
        "skip": skip,
        "limit": limit
        }

@app.get("/users")
def get_users(params = Depends(common_parameters)):
    return {"resource": "users", **params}

@app.get("/products")
def get_products(params = Depends(common_parameters)):
    return {"resource": "products", **params}