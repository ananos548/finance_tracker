from typing import Annotated

from fastapi import APIRouter, Depends, Cookie, Query

from tracker.src.api.dependencies import expenses_service, categories_service, expenses_statistics_service

from tracker.src.schemas.schemas import ExpenseSchemaAdd, CategorySchemaAdd
from tracker.src.services.expenses import ExpensesService
from tracker.src.services.expenses_statistics import ExpensesStatisticsService

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
        cookie_jwt: str = Cookie(None)
):
    expense_id = await service.add_expense(expense, cookie_jwt)
    return {"expense_id": expense_id}


@router.get("/get_expenses")
async def get_expenses(service: Annotated[ExpensesService, Depends(expenses_service)]):
    expenses = await service.get_expenses()
    return expenses


@router.get("/get_my_expenses")
async def get_my_expenses(service: Annotated[ExpensesService, Depends(expenses_service)],
                          cookie_jwt: str = Cookie(None)):
    expenses = await service.get_my_expenses(cookie_jwt)
    return expenses


@router.patch("/edit_expense/{expense_id}")
async def edit_expense(expense_id: int,
                       expense: ExpenseSchemaAdd,
                       service: Annotated[ExpensesService, Depends(expenses_service)],
                       cookie_jwt: str = Cookie(None)):
    expense = await service.edit_expense(expense_id, expense.model_dump(), cookie_jwt)
    return expense


@router.delete("/remove_expense/{expense_id}")
async def drop_expense(
        expense_id: int,
        service: Annotated[ExpensesService, Depends(expenses_service)],
        cookie_jwt: str = Cookie(None)):
    expense = await service.drop_expenses(expense_id, cookie_jwt)
    return expense


@router.get("/user/")
async def get_user_data(cookie_jwt: str = Cookie(None)):
    user_data = await get_user_data_from_redis(cookie_jwt)
    return user_data


@router.get("/statistic")
async def get_statistic(service: Annotated[ExpensesStatisticsService, Depends(expenses_statistics_service)],
                        cookie_jwt: str = Cookie(None),
                        month: int = Query(None, description="Месяц для статистики"),
                        year: int = Query(None, description="Год для статистики")):
    statistics = {
        "Sum_for_month": await service.calculate_total_expenses(cookie_jwt, month, year),
        "By_category": await service.calculate_expenses_by_category(cookie_jwt, month, year),
        "Biggest_category": await service.get_the_biggest_expense(cookie_jwt, month, year)
    }
    return {
        "Сумма расходов за месяц": statistics["Sum_for_month"],
        "Статистика по категориями": statistics["By_category"],
        "Самые большие траты в: ": statistics["Biggest_category"]
    }
