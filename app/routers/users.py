from typing import List

from fastapi import APIRouter, Depends
from app.schemas.users import User
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.users import User as UserModel


router = APIRouter()

@router.get("/api")
async def home():
    return {"message": "home"}

@router.get("/users", response_model=List[User])
async def get_users(db:Session = Depends(get_db)):
    return db.query(UserModel).all()

@router.post("/create-user", response_model=None)
async def create_users(user: User, db:Session = Depends(get_db)):
    user = UserModel(email=user.email, name=user.name, password=user.password)
    db.add(user)
    db.commit()
    return user.__dict__