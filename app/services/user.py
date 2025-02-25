from app.models.user import User
from app.core.security import hash_password

async def create_user(user_data):
    user = await User.create(email=user_data.email, password_hash=hash_password(user_data.password))
    return user

async def get_users():
    return await User.all()
