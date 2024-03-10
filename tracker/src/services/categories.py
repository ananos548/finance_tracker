from ..utils.repository import AbstractRepository
from ..schemas.schemas import CategorySchemaAdd


class CategoriesService:
    def __init__(self, categories_repo: AbstractRepository):
        self.categories_repo: AbstractRepository = categories_repo()

    async def add_category(self, category: CategorySchemaAdd):
        category_dict = category.model_dump()
        category_id = await self.categories_repo.add_one(category_dict)
        return category_id

    async def get_categories(self):
        categories = await self.categories_repo.find_all()
        return categories
