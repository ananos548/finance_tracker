from ..repositories.expenses import ExpensesRepository
from ..services.expenses import ExpensesService
from ..services.expenses_statistics import ExpensesStatisticsService

from ..repositories.categories import CategoriesRepository
from ..services.categories import CategoriesService


def expenses_service():
    return ExpensesService(ExpensesRepository)


def expenses_statistics_service():
    return ExpensesStatisticsService(ExpensesRepository)


def categories_service():
    return CategoriesService(CategoriesRepository)
