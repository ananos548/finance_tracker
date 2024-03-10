from fastapi import FastAPI, Depends
from tracker.src.api.routers import router as tracker_router

app = FastAPI()

app.include_router(tracker_router)
