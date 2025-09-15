# Tomato Disease Classification Web App

A GPU-enabled Dockerized **image classification web application** built with **TensorFlow**, **FastAPI**, and a minimal **frontend**. Users can upload images of tomato plants and get real-time predictions of potential diseases using a pre-trained **MobileNetV2-based model**.

---

## Features

- **Deep Learning Model**: Uses a MobileNetV2 base with additional layers for classifying tomato diseases.
- **Web Interface**: Simple and intuitive frontend to upload images and see predictions.
- **API**: FastAPI backend that can also be used programmatically.
- **Dockerized**: Easy deployment with GPU support using NVIDIA Docker.
- **Real-time Predictions**: Get predicted class and confidence instantly.
- **GPU Accelerated**: TensorFlow GPU support for fast inference.

---

## Supported Classes

| Class Index | Disease Name |
|------------|---------------|
| 0          | Tomato_Blight |
| 1          | Tomato_Healthy |
| 2          | Tomato_Spot |
| 3          | Tomato_YellowLeaf |
| 4          | Tomato_Bacterial |
| 5          | Tomato_Mosaic |

> Update these in `.env` if needed.

---

## Project Structure

\`\`\`
final_year_project/
├── app/
│   ├── main.py          # FastAPI backend
│   ├── model.py         # Model wrapper for predictions
│   ├── requirements.txt # Python dependencies
│   ├── static/          # CSS/JS for frontend (optional)
│   └── templates/       # HTML templates for frontend
├── model/
│   └── tomatoes.h5      # Pre-trained Keras model
├── Dockerfile           # Dockerfile for GPU container
├── docker-compose.yml   # Docker Compose configuration
├── .env                 # Environment variables
└── .dockerignore        # Files to ignore in Docker build
\`\`\`

---

## Getting Started

### Prerequisites

- **Docker** ≥ 20.10
- **NVIDIA GPU** with drivers installed (`nvidia-smi`)
- **NVIDIA Container Toolkit** installed
- Internet connection to pull Docker images

---

### 1️⃣ Clone the repository

\`\`\`bash
git clone https://github.com/Kafle33/tomato-classification.git
cd tomato-classification
\`\`\`

---

### 2️⃣ Place the pre-trained model

Place your `tomatoes.h5` model inside the `model/` folder:

\`\`\`
model/tomatoes.h5
\`\`\`

---

### 3️⃣ Configure environment

Edit the `.env` file if needed:

\`\`\`
APP_HOST=0.0.0.0
APP_PORT=8000
MODEL_PATH=/app/model/tomatoes.h5
CLASS_NAMES=Tomato_Blight,Tomato_Healthy,Tomato_Spot,Tomato_YellowLeaf,Tomato_Bacterial,Tomato_Mosaic
\`\`\`

---

### 4️⃣ Build and run with Docker

\`\`\`bash
docker-compose build
docker-compose up -d
\`\`\`

> The app will be available at [http://localhost:8000](http://localhost:8000)

---

### 5️⃣ Test the API

#### Via Web UI

- Open [http://localhost:8000](http://localhost:8000)
- Upload an image of a tomato leaf
- View predicted class and confidence

#### Via API (curl example)

\`\`\`bash
curl -X POST "http://localhost:8000/predict" \
  -F "file=@path_to_image.jpg"
\`\`\`

Response:

\`\`\`json
{
  "filename": "path_to_image.jpg",
  "predicted_class": "Tomato_Blight",
  "confidence": 95.42
}
\`\`\`

---

### 6️⃣ Verify GPU usage

Inside container:

\`\`\`bash
docker exec -it image-classifier python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
\`\`\`

Expected output:

\`\`\`
[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
\`\`\`

---

## Notes

- Ensure `NVIDIA Container Toolkit` is installed for GPU acceleration.
- You can modify `app/templates/` to customize the frontend.
- For CPU-only environments, replace the Docker base image with `tensorflow/tensorflow:2.15.0` (CPU).

---

## Future Enhancements

- Improved frontend UI with **image preview**, **progress bar**, and **Bootstrap styling**.
- API authentication for secure access.
- Batch image prediction support.
- Logging and monitoring for production deployment.

---

## Author

**Roshan Kafle**
- Email: roshankafle33@gmail.com
- GitHub: [github.com/Kafle33](https://github.com/Kafle33)

---

## License

MIT License – feel free to use and modify for research or personal projects.
