from sqladmin import ModelView
from tracker.src.models.models import Category, Expense


class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.id, Category.title]


class ExpenseAdmin(ModelView, model=Expense):
    column_list = [Expense.id, Expense.source]
