from src.schemas.schema import ExpenseSchemaAdd
from src.utils.repository import AbstractRepository


class ExpensesService:
    def __init__(self, expenses_repo: AbstractRepository):
        self.expenses_repo: AbstractRepository = expenses_repo()

    async def add_expense(self, expense: ExpenseSchemaAdd):
        expense_dict = expense.model_dump()
        expense_id = await self.expenses_repo.add_one(expense_dict)
        return expense_id

    async def get_expenses(self):
        expenses = await self.expenses_repo.find_all()
        return expenses
