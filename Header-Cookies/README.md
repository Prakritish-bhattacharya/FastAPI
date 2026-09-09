Now let's learn Headers and Cookies. These are commonly used for authentication, client information, tokens and session management.
# HTTP Headers
Headers are metadata sent with an HTTP request or response.
**Example:**
```text
GET /users

Headers:
Authorization: Bearer abc123
User-Agent: Chrome
Accept: application/json
```
## Reading a Header
```python
from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/headers")
def get_headers(user_agent: str | None = Header(default=None)):
    return {
        "user_agent": user_agent
    }
```
Now when the client sends:
```text
User-Agent: Chrome
```
FastAPI gives your function:
```python
user_agent = "Chrome"
```
## Why `Header()`
**Compare:**
```python
def get_headers(user_agent: str):
```
**with:**
```python
def get_headers(user_agent: str = Header()):
```
The second explicitly tells FastAPI:
>Get `user_agent` from the HTTP request headers.

So:
> `Header()` is used when the value should come from HTTP headers.

Headers carry metadata with an HTTP request or response, while cookies are small pieces of data stored by the client (commonly a browser) and sent back to the server with subsequent requests. FastAPI provides `Header` and `Cookie` for reading them.