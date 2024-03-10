from typing import Annotated

from fastapi import APIRouter, Depends

from tracker.src.api.dependencies import expenses_service, categories_service

from tracker.src.schemas.schemas import ExpenseSchemaAdd, CategorySchemaAdd
from tracker.src.services.expenses import ExpensesService

from tracker.src.services.categories import CategoriesService
from redis_connection import get_user_data_from_redis

router = APIRouter(
    prefix="/finances",
    tags=["Finances"],
)


@router.post("/add_category")
async def add_category(
        category: CategorySchemaAdd,
        service: Annotated[CategoriesService, Depends(categories_service)]
):
    category_id = await service.add_category(category)
    return {"category_id": category_id}


@router.post("/add_expense")
async def add_expense(
        expense: ExpenseSchemaAdd,
        service: Annotated[ExpensesService, Depends(expenses_service)],
):
    expense_id = await service.add_expense(expense)
    return {"expense_id": expense_id}


@router.get("/get_expenses")
async def get_expenses(service: Annotated[ExpensesService, Depends(expenses_service)]):
    expenses = await service.get_expenses()
    return expenses


@router.get("/get_my_expenses")
async def get_my_expenses(service: Annotated[ExpensesService, Depends(expenses_service)]):
    expenses = await service.get_my_expenses()
    return expenses


@router.patch("/edit_expense/{expense_id}")
async def edit_expense(expense_id: int,
                       expense: ExpenseSchemaAdd,
                       service: Annotated[ExpensesService, Depends(expenses_service)]):
    expense = await service.edit_expense(expense_id, expense.model_dump())
    return expense


@router.delete("/remove_expense/{expense_id}")
async def drop_expense(
        expense_id: int,
        service: Annotated[ExpensesService, Depends(expenses_service)]):
    expense = await service.drop_expenses(expense_id)
    return expense


@router.get("/user/")
async def get_user_data():
    user_data = await get_user_data_from_redis()
    return user_data
