from ..utils.repository import AbstractRepository
from ..schemas.schemas import ExpenseSchemaAdd
from redis_connection import get_user_data_from_redis
from ..utils.validate_expense import validate_expense


class ExpensesService:
    def __init__(self, expenses_repo: AbstractRepository):
        self.expenses_repo: AbstractRepository = expenses_repo()

    async def add_expense(self, expense: ExpenseSchemaAdd, cookie_jwt: str):
        expense_dict = expense.model_dump()
        user_data = await get_user_data_from_redis(cookie_jwt)
        expense_dict["user_id"] = user_data["user_id"]
        expense_id = await self.expenses_repo.add_one(expense_dict)
        return expense_id

    async def get_expenses(self):
        expenses = await self.expenses_repo.find_all()
        return expenses

    async def get_categories(self):
        categories = await self.expenses_repo.find_all()
        return categories

    async def get_my_expenses(self, cookie_jwt: str):
        user_info = await get_user_data_from_redis(cookie_jwt)
        expenses = await self.expenses_repo.find_by_user_id(user_info["user_id"])
        return expenses

    async def edit_expense(self, expense_id: int, expense_data: dict, cookie_jwt: str):
        await validate_expense(self, expense_id, cookie_jwt)
        await self.expenses_repo.edit_one(expense_id, expense_data)
        return {"detail": "Expense updated successfully"}

    async def drop_expenses(self, expense_id: int, cookie_jwt: str):
        await validate_expense(self, expense_id, cookie_jwt)
        await self.expenses_repo.drop_one(expense_id)
        return {"detail": "Expense deleted successfully"}
