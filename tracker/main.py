from fastapi import FastAPI, Depends
from sqladmin import Admin

from tracker.src.database import engine
from tracker.src.admin.admin import CategoryAdmin, ExpenseAdmin
from tracker.src.api.routers import router as tracker_router

app = FastAPI()
admin = Admin(app, engine)

admin.add_view(CategoryAdmin)
admin.add_view(ExpenseAdmin)

app.include_router(tracker_router)
