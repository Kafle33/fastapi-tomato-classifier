# Soil Moisture Analyzer

An AI-powered application that analyzes soil moisture levels from tomato leaf images. Built with FastAPI, TensorFlow, and Docker.

![Soil Moisture Analyzer](app/static/screenshot.png)

## Features

- **Moisture Analysis**: Detects Low, Optimal, and High moisture levels.
- **Smart Suggestions**: Provides actionable irrigation advice based on analysis.
- **Demo Mode**: Includes a set of test images for quick demonstration.
- **Modern UI**: Clean, responsive interface with dark mode support.
- **Dockerized**: Easy to deploy with Docker Compose.

## Prerequisites

- Docker and Docker Compose
- Git

## Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/soil-moisture-analyzer.git
   cd soil-moisture-analyzer
   ```

2. **Run with Docker Compose:**
   ```bash
   docker compose up --build
   ```

3. **Access the application:**
   Open your browser and navigate to `http://localhost:8000`.

## Usage

1. **Select an Image**: Choose from the provided demo images or upload your own.
2. **Analyze**: Click the "Analyze Moisture" button.
3. **View Results**: See the moisture percentage, category, and irrigation suggestion.

## Project Structure

```
.
├── app/
│   ├── main.py              # FastAPI application
│   ├── model.py             # TensorFlow model wrapper
│   ├── static/              # Static assets (css, images)
│   └── templates/           # HTML templates
├── Dockerfile               # Docker build instructions
├── docker-compose.yml       # Docker Compose configuration
└── requirements.txt         # Python dependencies
```

## Technology Stack

- **Backend**: FastAPI, Uvicorn
- **ML/AI**: TensorFlow, Keras, MobileNetV2
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Containerization**: Docker

## License

MIT License
