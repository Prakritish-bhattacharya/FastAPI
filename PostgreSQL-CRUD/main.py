from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from models import User

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "FastAPI + PostgreSQL is working!"}

@app.post("/users")
def create_user(name: str,age: int,email: str,db: Session = Depends(get_db)):
    new_user = User(
        name=name,
        age=age,
        email=email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user