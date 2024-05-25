from abc import ABC, abstractmethod

from sqlalchemy import insert, select, delete, update
from sqlalchemy.orm import joinedload

from tracker.src.database import async_session_maker
from tracker.src.models.models import Category


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def find_all():
        raise NotImplementedError

    @abstractmethod
    async def find_by_user_id():
        raise NotImplementedError

    @abstractmethod
    async def drop_one():
        raise NotImplementedError

    @abstractmethod
    async def edit_one():
        raise NotImplementedError

    @abstractmethod
    async def find_expenses_with_categories():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def find_all(self):
        async with async_session_maker() as session:
            stmt = select(self.model).options(joinedload(self.model.category))
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res

    async def find_by_user_id(self, user_id: int = None):
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.user_id == user_id).options(joinedload(self.model.category))
            res = await session.execute(stmt)
            expenses = res.scalars().all()
            return [expense.to_read_model() for expense in expenses]

    async def find_expenses_with_categories(self, user_id: int = None):
        async with async_session_maker() as session:
            stmt = select(Category.title, self.model.amount, self.model.date).join(Category,
                                                                                   self.model.category_id == Category.id).where(
                self.model.user_id == user_id)
            res = await session.execute(stmt)
            return res

    async def edit_one(self, expense_id: int, data: dict):
        async with async_session_maker() as session:
            stmt = update(self.model).where(self.model.id == expense_id).values(**data)
            await session.execute(stmt)
            await session.commit()

    async def drop_one(self, id: int = None):
        async with async_session_maker() as session:
            stmt = delete(self.model).where(self.model.id == id)
            await session.execute(stmt)
            await session.commit()
