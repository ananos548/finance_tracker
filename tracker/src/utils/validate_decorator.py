from fastapi import HTTPException, status

from redis_connection import get_user_data_from_redis


def expense_validator(func):
    async def wrapper(self, expense_id: int, *args, **kwargs):
        user_info = await get_user_data_from_redis()
        expenses = await self.expenses_repo.find_by_user_id(user_info["user_id"])
        if not any(expense.id == expense_id for expense in expenses):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Expense not found or you are not authorized to access it"
            )
        return await func(self, expense_id, *args, **kwargs)

    return wrapper
