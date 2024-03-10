from tracker.src.models.models import Expense
from tracker.src.utils.repository import SQLAlchemyRepository


class ExpensesRepository(SQLAlchemyRepository):
    model = Expense
