from fastapi import APIRouter, File, UploadFile
from app.services.image import predict_image

router = APIRouter()


@router.post("/classify")
async def classify_image(file: UploadFile = File(...)):
  return await predict_image(file)
   
