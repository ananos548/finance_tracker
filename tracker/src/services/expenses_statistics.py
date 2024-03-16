from collections import Counter
from typing import List, Dict
from datetime import datetime, timedelta

from redis_connection import get_user_data_from_redis
from tracker.src.utils.repository import AbstractRepository


class ExpensesStatisticsService:

    def __init__(self, expenses_repo: AbstractRepository):
        self.expenses_repo: AbstractRepository = expenses_repo()

    async def calculate_total_expenses(self):
        user_data = await get_user_data_from_redis()
        expenses = await self.expenses_repo.find_by_user_id(user_data["user_id"])
        total_expenses = sum(expense.amount for expense in expenses)
        return total_expenses

    async def calculate_expenses_by_category(self):
        user_data = await get_user_data_from_redis()
        expenses = await self.expenses_repo.find_by_user_id(user_data["user_id"])
        categories_counter = Counter(expense.category_id for expense in expenses)
        total_expenses = sum(expense.amount for expense in expenses)
        expenses_by_category = {category_id: amount / total_expenses * 100 for category_id, amount in
                                categories_counter.items()}
        return expenses_by_category
