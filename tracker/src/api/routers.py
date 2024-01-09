from typing import Annotated

from fastapi import APIRouter, Depends

from src.schemas.schema import ExpenseSchemaAdd
from src.services.expenses import ExpensesService
from src.api.dependencies import expenses_service

router = APIRouter(
    prefix="/finances",
    tags=["Finances"],
)


@router.post("/add_expense")
async def add_expense(
        expense: ExpenseSchemaAdd,
        service: Annotated[ExpensesService, Depends(expenses_service)]
):
    expense_id = await service.add_expense(expense)
    # if user_id not in fwd: exception
    return {"expense_id": expense_id}


@router.get("/get_expenses")
async def get_expenses(service: Annotated[ExpensesService, Depends(expenses_service)]):
    expenses = await service.get_expenses()
    return expenses
