from fastapi import FastAPI, UploadFile, File
from huggingface_model import predict_pollution

app = FastAPI()

@app.post("/analyze")
async def analyze_image(image: UploadFile = File(...)):
    image_bytes = await image.read()
    result = predict_pollution(image_bytes)
    return result
