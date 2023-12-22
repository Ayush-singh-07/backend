from fastapi import FastAPI
from app.routers import  users, base


app = FastAPI()
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(base.router, prefix="/emails", tags=['emails'])