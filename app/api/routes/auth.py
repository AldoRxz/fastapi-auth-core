from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut, Token, UserLogin
from app.db import models
from app.db.session import SessionLocal
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user  # importa el validador de JWT
)

router = APIRouter()

# Dependencia de sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Registro de usuarios
@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password),
        status=True
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Inicio de sesión con generación de token
@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token(data={"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}

# Ruta protegida (requiere token JWT)
@router.get("/me", response_model=dict)
def read_current_user(current_user: str = Depends(get_current_user)):
    return {"email": current_user}

# -------------------------------------------------------------------
# 👇 EJEMPLO: Cómo proteger otra ruta con JWT
# from fastapi import FastAPI, Depends
# from app.core.security import get_current_user
#
# @router.get("/dashboard")
# def dashboard(current_user: str = Depends(get_current_user)):
#     return {"message": f"Bienvenido {current_user}"}
# -------------------------------------------------------------------


