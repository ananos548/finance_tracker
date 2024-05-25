from fastapi import FastAPI, Depends
from sqladmin import Admin
from fastapi.middleware.cors import CORSMiddleware

from tracker.src.database import engine
from tracker.src.admin.admin import CategoryAdmin, ExpenseAdmin
from tracker.src.api.routers import router as tracker_router

app = FastAPI()
admin = Admin(app, engine)

admin.add_view(CategoryAdmin)
admin.add_view(ExpenseAdmin)

app.include_router(tracker_router)

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
