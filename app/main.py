from fastapi import FastAPI
from app.db import Base, engine
from app.routes.users import router as users_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users_router)


@app.get("/")
def root():
    return {"message": "API rodando 🚀"}
