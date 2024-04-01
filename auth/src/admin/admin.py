from sqladmin import ModelView
from auth.src.models.models import User


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username]
