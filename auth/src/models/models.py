from datetime import datetime
from sqlalchemy import Column, String, TIMESTAMP, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    email = Column(String(254), unique=True, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    hashed_password = Column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
