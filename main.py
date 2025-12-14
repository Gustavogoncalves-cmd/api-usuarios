from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from db import SessionLocal, engine, Base
from models import UserModel
from schemas import UserCreate, User, UserUpdate

app = FastAPI()

# cria as tabelas
Base.metadata.create_all(bind=engine)

# dependencia do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "API rodando 🚀"}

@app.get("/users", response_model=list[User])
def list_users(db: Session = Depends(get_db)):
    return db.query(UserModel).all()

@app.post("/users", response_model=User, status_code=201)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):

    existing = db.query(UserModel).filter(UserModel.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=409, detail="Email already exists")

    user = UserModel(name=payload.name, email=payload.email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# -------- PUT (atualiza tudo) --------
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, payload: UserCreate, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    exists = db.query(UserModel).filter(
        UserModel.email == payload.email,
        UserModel.id != user_id
    ).first()
    if exists:
        raise HTTPException(status_code=409, detail="Email already exists")

    user.name = payload.name
    user.email = payload.email

    db.commit()
    db.refresh(user)
    return user

# -------- PATCH (atualiza parcial) --------
@app.patch("/users/{user_id}", response_model=User)
def patch_user(user_id: int, payload: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if payload.email is not None:
        exists = db.query(UserModel).filter(
            UserModel.email == payload.email,
            UserModel.id != user_id
        ).first()
        if exists:
            raise HTTPException(status_code=409, detail="Email already exists")
        user.email = payload.email

    if payload.name is not None:
        user.name = payload.name

    db.commit()
    db.refresh(user)
    return user

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, payload: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.name = payload.name
    user.email = payload.email

    if payload.name is not None:
        user .name = payload.name

    if payload.email is not None:
        user.email = payload.email

    db.commit()
    db.refresh(user)
    return user

@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return
