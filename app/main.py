from fastapi import FastAPI
from app.api.v1 import router as api_router
from tortoise.contrib.fastapi import register_tortoise
from app.core.config import TORTOISE_ORM

app = FastAPI(title="FastAPI with Tortoise & PostgreSQL")

app.include_router(api_router, prefix="/api/v1")

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI with Tortoise-ORM!"}


# from fastapi import FastAPI, File, UploadFile
# from io import BytesIO
# from PIL import Image
# import torch
# from torchvision import transforms

# # Load your trained model (Replace with actual model loading code)
# class SimpleModel(torch.nn.Module):
#     def forward(self, x):
#         return torch.rand(1, 2)  # Dummy prediction (Replace with actual model inference)

# model = SimpleModel()
# model.eval()

# # Define transformation for input images
# transform = transforms.Compose([
#     transforms.Resize((224, 224)),
#     transforms.ToTensor(),
# ])

# app = FastAPI()

# @app.post("/classify")
# async def classify_image(file: UploadFile = File(...)):
#     image = Image.open(BytesIO(await file.read())).convert("RGB")
#     image = transform(image).unsqueeze(0)  # Add batch dimension
    
#     with torch.no_grad():
#         output = model(image)
#         prediction = torch.argmax(output, dim=1).item()
    
#     classes = ["Cat", "Dog"]
#     return {"filename": file.filename, "prediction": classes[prediction]}
