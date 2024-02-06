from datetime import timedelta

from fastapi import APIRouter, Depends, Cookie, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from src.utils.users import UserService
from src.schemas.schemas import UserSchemaAdd

from src.models.models import User
from starlette import status

router = APIRouter(
    prefix="/auth",
    tags=['auth'],

)


@router.post("/registration")
async def create_user(
        new_user: UserSchemaAdd,
        service: UserService = Depends(UserService)
):
    user = await service.add_user(new_user)
    return {"user_id": user.id}


@router.post("/login")
async def login_for_access_token(
        service: UserService = Depends(UserService),
        form_data: OAuth2PasswordRequestForm = Depends()):
    user = await service.authenticate(form_data.username, form_data.password)
    token = service.create_access_token(user_id=user.id, username=user.username, expires_delta=timedelta(minutes=3600))
    response = JSONResponse(content={"message": "куки установлены"})
    response.set_cookie(
        key="cookie_jwt",
        value=token
    )
    return response


@router.post("/logout")
def logout(response: Response):
    response.delete_cookie("cookie_jwt")
    return {"message": "Logged out successfully"}


@router.get("/current_user")
def get_current_user(cookie_jwt: str | None = Cookie(default=None), service: UserService = Depends(UserService)):
    user = service.get_current_user(cookie_jwt)
    return user
