from fastapi import FastAPI
from src.api.routers import router as tracker_router

app = FastAPI()

app.include_router(tracker_router)
