from fastapi import APIRouter
from app.api.v1.user.user import router as user_router
from app.api.v1.image.image import router as image_router

router = APIRouter()

router.include_router(user_router, prefix="/user", tags=["User"])
router.include_router(image_router, prefix='/image', tags=['Images'])