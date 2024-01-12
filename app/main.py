import os
import shutil
from pathlib import Path

from fastapi import FastAPI, File, Request, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.model import ImageClassifier

# Setup paths
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"
TEST_IMAGES_DIR = STATIC_DIR / "test_images"

app = FastAPI()
classifier = ImageClassifier()

# Add CORS middleware to allow cross-origin requests (helpful for development/debugging)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Frontend templates & static
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/demo-images")
def get_demo_images():
    """Return list of demo images from test_images folder."""
    if not TEST_IMAGES_DIR.exists():
        return {"images": []}
        
    images = [
        f.name for f in TEST_IMAGES_DIR.iterdir() 
        if f.is_file() and f.suffix.lower() in (".jpg", ".jpeg", ".png")
    ]
    return {"images": sorted(images)}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Ensure temp directory exists
    temp_dir = BASE_DIR / "temp"
    temp_dir.mkdir(exist_ok=True)
    
    temp_path = temp_dir / f"temp_{file.filename}"
    
    try:
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        result = classifier.predict(str(temp_path))
        print("\n\n\nthis is result", result)
        
        # Return JSON for the frontend JS
        return {
            "moisture_score": result["moisture_score"],
            "moisture_category": result["moisture_category"],
            "suggestion": result["suggestion"],
            "color": result["color"],
            "confidence": result["confidence"],
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    finally:
        if temp_path.exists():
            os.remove(temp_path)

# Handle GET requests to /predict to avoid 405 confusion
@app.get("/predict")
def predict_info():
    return JSONResponse(
        status_code=405, 
        content={"message": "This endpoint expects a POST request with an image file."}
    )
