from src.models.models import Expense
from src.utils.repository import SQLAlchemyRepository


class ExpensesRepository(SQLAlchemyRepository):
    model = Expense
