from collections import defaultdict

from redis_connection import get_user_data_from_redis
from tracker.src.utils.repository import AbstractRepository


class ExpensesStatisticsService:

    def __init__(self, expenses_repo: AbstractRepository):
        self.expenses_repo: AbstractRepository = expenses_repo()

    async def calculate_total_expenses(self, cookie_jwt: str):
        user_data = await get_user_data_from_redis(cookie_jwt)
        expenses = await self.expenses_repo.find_by_user_id(user_data["user_id"])
        total_expenses = sum(expense.amount for expense in expenses)
        return total_expenses

    async def calculate_expenses_by_category(self, cookie_jwt: str):
        user_data = await get_user_data_from_redis(cookie_jwt)
        expenses = await self.expenses_repo.find_expenses_with_categories(user_data["user_id"])
        expenses_by_category = defaultdict(int)

        for category_name, amount in expenses:
            expenses_by_category[category_name] += amount

        return expenses_by_category
