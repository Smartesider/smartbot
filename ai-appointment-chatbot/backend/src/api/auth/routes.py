from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..core import database, security
from ..models import user as user_model
from ..schemas import user as user_schema

router = APIRouter()

@router.post("/register", response_model=user_schema.User)
def register_user(user: user_schema.UserCreate, db: Session = Depends(database.get_db)):
    db_user = user_model.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_model.create_user(db=db, user=user)

@router.post("/login", response_model=user_schema.User)
def login_user(user: user_schema.UserLogin, db: Session = Depends(database.get_db)):
    db_user = user_model.get_user_by_email(db, email=user.email)
    if not db_user or not security.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return db_user

@router.get("/me", response_model=user_schema.User)
def get_current_user(db: Session = Depends(database.get_db), current_user: user_schema.User = Depends(security.get_current_user)):
    return current_user