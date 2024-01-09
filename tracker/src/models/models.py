from datetime import datetime
from sqlalchemy import Column, Integer, String, TIMESTAMP, Float, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base

from src.schemas.schema import ExpenseSchema


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)


class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    source = Column(String(255), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(TIMESTAMP, default=datetime.utcnow)
    category_id = Column(Integer, ForeignKey('categories.id'))
    user_id = Column(Integer)

    def to_read_model(self) -> ExpenseSchema:
        return ExpenseSchema(
            id=self.id,
            source=self.source,
            amount=self.amount,
            category_id=self.category_id,
            user_id=self.user_id
        )
