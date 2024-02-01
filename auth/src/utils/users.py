import jwt
from fastapi import Depends, HTTPException, Cookie, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2AuthorizationCodeBearer
from starlette import status

from datetime import datetime, timedelta
from typing import Annotated, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from jose import JWTError
from passlib.context import CryptContext

from src.database import get_async_session
from src.models.models import User
from src.schemas.schemas import UserSchemaAdd

SECRET_KEY = "SnSYSxw3Nq"
ALGORITHM = "HS256"

password_hashing = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/login")


class UserService:

    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session

    async def add_user(self, user: UserSchemaAdd):
        new_user = User(username=user.username, email=user.email, hashed_password=password_hashing.hash(user.password))
        self.session.add(new_user)
        await self.session.commit()
        return new_user

    async def authenticate(self, username: str, hashed_password: str):
        result = await self.session.execute(select(User).filter(User.username == username))
        user = result.scalar_one_or_none()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
        if not password_hashing.verify(hashed_password, user.hashed_password):
            return None
        return user

    @staticmethod
    def create_access_token(username: str, user_id: int, expires_delta: timedelta = None):
        encode = {"sub": username, "id": user_id}
        expires = datetime.utcnow() + expires_delta
        encode.update({"exp": expires})
        return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            user_id: int = payload.get("id")
            return {"username": username, "id": user_id}
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="not validate user")
