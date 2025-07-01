from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import SessionLocal, engine, Base, get_db
from models import User
from sqlalchemy.orm import Session

app = FastAPI()
Base.metadata.create_all(bind=engine)

class RegisterRequest(BaseModel):
    name: str
    email: str

@app.post("/register")
def register_user(data: RegisterRequest, db: Session = next(get_db())):
    user = User(name=data.name, email=data.email)
    db.add(user)
    db.commit()
    return {"message": "User registered"}