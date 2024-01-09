from fastapi import FastAPI

from src.schemas.schemas import UserRead, UserCreate
from src.utils.base_config import fastapi_users, auth_backend

app = FastAPI()

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)
