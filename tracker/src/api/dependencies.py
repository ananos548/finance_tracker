from ..repositories.expenses import ExpensesRepository
from ..services.expenses import ExpensesService
from ..repositories.categories import CategoriesRepository
from ..services.categories import CategoriesService


def expenses_service():
    return ExpensesService(ExpensesRepository)


def categories_service():
    return CategoriesService(CategoriesRepository)
