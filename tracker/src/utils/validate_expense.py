from fastapi import HTTPException, status

from redis_connection import get_user_data_from_redis


async def validate_expense(self, expense_id: int, cookie_jwt: str):
    user_info = await get_user_data_from_redis(cookie_jwt)
    expenses = await self.expenses_repo.find_by_user_id(user_info["user_id"])
    if not any(expense.id == expense_id for expense in expenses):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expense.jsx not found or you are not authorized to access it"
        )
