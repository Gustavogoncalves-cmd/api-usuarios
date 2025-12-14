from fastapi import FastAPI, HTTPException
from schemas import UserCreate, User

app = FastAPI()

db: list[User] = []
next_id = 1

@app.get("/")
def root():
    return {"message": "API rodando 🚀"}

@app.get("/users", response_model=list[User])
def list_users():
    return db

@app.post("/users", response_model=User, status_code=201)
def create_user(payload: UserCreate):
    global next_id
    user = User(id=next_id, **payload.model_dump())
    next_id += 1
    db.append(user)
    return user

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for u in db:
        if u.id == user_id:
         return u

    raise HTTPException(status_code=404, detail="user not found")