import os
import shutil

from fastapi import FastAPI, File, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.model import ImageClassifier

app = FastAPI()
classifier = ImageClassifier()

# Frontend templates & static
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = classifier.predict(temp_path)
    os.remove(temp_path)

    # Return JSON for the frontend JS
    return {
        "predicted_class": result["predicted_class"],
        "confidence": result["confidence"],
    }
