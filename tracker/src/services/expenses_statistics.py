from datetime import datetime, timedelta
from collections import defaultdict, Counter

from dateutil.relativedelta import relativedelta

from redis_connection import get_user_data_from_redis
from tracker.src.utils.repository import AbstractRepository


class ExpensesStatisticsService:

    def __init__(self, expenses_repo: AbstractRepository):
        self.expenses_repo: AbstractRepository = expenses_repo()

    async def calculate_total_expenses(self, cookie_jwt: str, month: int = None, year: int = None):
        expenses_by_category = await self.calculate_expenses_by_category(cookie_jwt, month, year)
        total_expenses_by_category = sum(
            value for value in expenses_by_category.values() if isinstance(value, (int, float)))
        return total_expenses_by_category

    async def calculate_expenses_by_category(self, cookie_jwt: str, month: int = None, year: int = None):
        user_data = await get_user_data_from_redis(cookie_jwt)
        expenses = await self.expenses_repo.find_expenses_with_categories(user_data["user_id"])
        expenses_by_category = defaultdict(int)

        if month is None or year is None:
            now = datetime.utcnow()
            month = now.month
            year = now.year

        start_of_month = datetime(year, month, 1)
        next_month = start_of_month + relativedelta(months=1)
        end_of_month = next_month - timedelta(days=1)

        for category_name, amount, expense_date in expenses:
            if start_of_month <= expense_date < end_of_month:
                expenses_by_category[category_name] += amount
        if not expenses_by_category:
            return {"Не обнаружено трат в этот период": "No expenses found for the selected period"}

        return expenses_by_category

    async def get_the_biggest_expense(self, cookie_jwt: str, month: int = None, year: int = None):
        try:
            expenses_by_category = await self.calculate_expenses_by_category(cookie_jwt, month, year)
            max_expense = max(expenses_by_category.items(), key=lambda x: x[1])[0]
            return max_expense
        except ValueError:
            return ValueError("Расходов не обнаружено")
