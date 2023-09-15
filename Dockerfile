# Use official TensorFlow GPU image (includes CUDA + cuDNN)
FROM tensorflow/tensorflow:2.15.0-gpu

WORKDIR /app

# Install system dependencies (needed for Pillow, OpenCV, etc.)
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code and model
COPY app/ ./app
COPY model/ ./model

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

# Run FastAPI app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
