from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.schemas.schemas import Token
from src.utils.users import UserService
from src.schemas.schemas import UserSchemaAdd

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


@router.post("/login", response_model=Token)
async def login_for_access_token(
        service: UserService = Depends(UserService),
        form_data: OAuth2PasswordRequestForm = Depends()):
    user = await service.authenticate(form_data.username, form_data.password)
    token = service.create_access_token(user.username, user.id, timedelta(minutes=3600))
    return {"access_token": token, "token_type": "bearer"}


@router.get("/current")
async def get_user_info(user: Annotated[dict, Depends(UserService.get_current_user)]):
    return {"user_info": user}
