from src.repositories.expenses import ExpensesRepository
from src.services.expenses import ExpensesService


def expenses_service():
    return ExpensesService(ExpensesRepository)