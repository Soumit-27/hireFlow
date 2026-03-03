# routes/

from fastapi import APIRouter
from app.schemas.auth import RegisterSchema, LoginSchema
from app.controllers.auth_ctrl import register_user, login_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
async def register(user: RegisterSchema):
    return await register_user(user)

@router.post("/login")
async def login(user: LoginSchema):
    return await login_user(user)