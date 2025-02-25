from fastapi import APIRouter
from app.services.user import create_user, get_users
from app.schemas.user import UserCreate, UserResponse

router = APIRouter()

@router.get("", response_model=list[UserResponse])
async def read_users():
    return await get_users()

@router.post("", response_model=UserResponse)
async def register_user(user_data: UserCreate):
    return await create_user(user_data)
