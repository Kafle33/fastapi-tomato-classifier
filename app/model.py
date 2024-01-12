import os

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input


class ImageClassifier:
    def __init__(self):
        model_path = os.getenv("MODEL_PATH", "tomatoes.h5")
        self.model = load_model(model_path)

    def predict(self, image_path: str):
        img = image.load_img(image_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        # Use MobileNetV2 standard preprocessing (scales to [-1, 1])
        img_array = preprocess_input(img_array)

        predictions = self.model.predict(img_array)
        pred = predictions[0]
        
        # Calculate weighted moisture score (0-100)
        # Assuming indices 0-5 represent an ordered scale of moisture levels
        moisture_score = float(sum(i * p for i, p in enumerate(pred)) / 5.0 * 100)
        
        # Categorize based on weighted score
        if moisture_score < 30:
            category = "Low Moisture"
            suggestion = "Irrigation needed immediately."
            color = "#f59e0b"
        elif moisture_score < 65:
            category = "Optimal Moisture"
            suggestion = "Conditions are ideal. No action needed."
            color = "#10b981"
        else:
            category = "High Moisture"
            suggestion = "Excess moisture detected. Monitor for drainage issues."
            color = "#3b82f6"

        print(f"Moisture Score: {moisture_score:.2f}% -> {category}")

        return {
            "moisture_score": round(moisture_score, 2),
            "moisture_category": category,
            "suggestion": suggestion,
            "color": color,
            "confidence": round(float(np.max(pred) * 100), 2)
        }
