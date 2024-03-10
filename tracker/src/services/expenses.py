from ..utils.repository import AbstractRepository
from ..schemas.schemas import ExpenseSchemaAdd
from redis_connection import get_user_data_from_redis
from ..utils.validate_decorator import expense_validator


class ExpensesService:
    def __init__(self, expenses_repo: AbstractRepository):
        self.expenses_repo: AbstractRepository = expenses_repo()

    async def add_expense(self, expense: ExpenseSchemaAdd):
        expense_dict = expense.model_dump()
        user_data = await get_user_data_from_redis()
        expense_dict["user_id"] = user_data["user_id"]
        expense_id = await self.expenses_repo.add_one(expense_dict)
        return expense_id

    async def get_expenses(self):
        expenses = await self.expenses_repo.find_all()
        return expenses

    async def get_my_expenses(self):
        user_info = await get_user_data_from_redis()
        expenses = await self.expenses_repo.find_by_user_id(user_info["user_id"])
        return expenses

    @expense_validator
    async def edit_expense(self, expense_id: int, expense_data: dict):
        await self.expenses_repo.edit_one(expense_id, expense_data)
        return {"detail": "Expense updated successfully"}

    @expense_validator
    async def drop_expenses(self, expense_id: int):
        await self.expenses_repo.drop_one(expense_id)
        return {"detail": "Expense deleted successfully"}
