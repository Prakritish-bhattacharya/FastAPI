from fastapi import FastAPI, Header
app = FastAPI()

@app.get("/headers")
def get_headers(user_agent: str | None = Header(default = None)):
    return {
        "user_agent": user_agent
    }