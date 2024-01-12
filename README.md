# Soil Moisture Analyzer

This app checks water in tomato leaves. It uses AI to help you.

![Soil Moisture Analyzer](app/static/screenshot.png)

## What it does

- **Checks Moisture**: Tells if plant has Low, Good, or High water.
- **Gives Advice**: Tells you if you need to water the plant.
- **Test Images**: Has photos to try.
- **Easy to Use**: Simple web page.

## What you need

- Docker
- Git

## How to run

1. **Get the code:**
   ```bash
   git clone https://github.com/yourusername/soil-moisture-analyzer.git
   cd soil-moisture-analyzer
   ```

2. **Start the app:**
   ```bash
   docker compose up --build
   ```

3. **Open app:**
   Go to your browser and type: `http://localhost:8000`

## How to use

1. **Pick an Image**: Use test image or upload your own.
2. **Click Button**: Click "Analyze Moisture".
3. **See Result**: See if plant needs water.

## Project Files

- `app/main.py`: The web server code.
- `app/model.py`: The AI brain code.
- `Dockerfile`: How to build the app.
- `docker-compose.yml`: How to run the app.

## License

MIT License
