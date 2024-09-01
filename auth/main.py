from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin

from auth.src.database import engine
from auth.src.admin.admin import UserAdmin
from auth.src.api.routers import router as auth_router

app = FastAPI()

app.include_router(auth_router)
admin = Admin(app, engine)

admin.add_view(UserAdmin)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
