from fastapi import FastAPI
from database import get_db
from models import User
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/users")
def get_users(db: Session = next(get_db())):
    return db.query(User).all()