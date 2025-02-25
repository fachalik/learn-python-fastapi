from fastapi import FastAPI, File, UploadFile
from io import BytesIO
from PIL import Image
import torch
from torchvision import transforms

# Load your trained model (Replace with actual model loading code)
class SimpleModel(torch.nn.Module):
    def forward(self, x):
        return torch.rand(1, 2)  # Dummy prediction (Replace with actual model inference)

model = SimpleModel()
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

async def predict_image(file: UploadFile = File(...)):
    image = Image.open(BytesIO(await file.read())).convert("RGB")
    image = transform(image).unsqueeze(0)  # Add batch dimension
    
    with torch.no_grad():
        output = model(image)
        prediction = torch.argmax(output, dim=1).item()
    
    classes = ["Cat", "Dog"]
    return {"filename": file.filename, "prediction": classes[prediction]}
