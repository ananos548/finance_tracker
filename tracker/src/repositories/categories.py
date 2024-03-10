from tracker.src.models.models import Category
from tracker.src.utils.repository import SQLAlchemyRepository


class CategoriesRepository(SQLAlchemyRepository):
    model = Category
