from fastapi import FastAPI
from sqladmin import Admin

from auth.src.database import engine
from auth.src.admin.admin import UserAdmin
from auth.src.api.routers import router as auth_router

app = FastAPI()

app.include_router(auth_router)
admin = Admin(app, engine)

admin.add_view(UserAdmin)
