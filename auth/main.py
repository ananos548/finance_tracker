from fastapi import FastAPI

from auth.src.api.routers import router as auth_router

app = FastAPI()

app.include_router(auth_router)
