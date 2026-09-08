A dependency is a reusable piece of logic that FastAPI executes and provides to our endpoint...

## Why do we need Dependencies ??

Suppose several endpoint need the same logic:
- Get Current User
- Check Authentication
- Validate API key
- Connect to DB
- Pagination
- Common Query parameters

without dependencies, We should repeat the same code....::

```python
@app.get("/users")
def get_users():
    # authentication logic
    # database logic
    # ...
    pass
@app.get("/products")
def get_products():
    # same authentication logic
    # database logic
    # ...
    pass
```
This is bad because of code duplication.
**Dependencies allow us to write the logic once and reuse it.**

## What is dependency injection in FastAPI?

Dependency Injection is a mechanism where FastAPI automatically provides the required dependencies to an endpoint. It allows us to reuse common logic such as authentication, database connections, pagination, and authorization without duplicating code. FastAPI's `Depends()` is used to declare these dependencies.

syntax to remember:
```python
@app.get("/users")
def get_users(
    data=Depends(common_parameters)
):
    return data
```


## Why Dependencies Matter
The real advantage isn't just saving a few lines.
Dependencies provide:

**♻️ Reusability**

Write logic once and reuse it.

**🧩 Separation of concerns**

Keep authentication/database/pagination logic outside your endpoint.

**🧪 Testability**

Dependencies can be replaced during testing.

**🔐 Authentication**

Very commonly used for authentication and authorization.

**🗄️ Database**

Database sessions are commonly injected through dependencies.