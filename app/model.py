import os

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


class ImageClassifier:
    def __init__(self):
        model_path = os.getenv("MODEL_PATH", "tomatoes.h5")
        self.model = load_model(model_path)
        self.class_names = os.getenv(
            "CLASS_NAMES",
            "Tomato_Blight,Tomato_Healthy,Tomato_Spot,Tomato_YellowLeaf,Tomato_Bacterial,Tomato_Mosaic",
        ).split(",")

    def predict(self, image_path: str):
        img = image.load_img(image_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        predictions = self.model.predict(img_array)
        predicted_index = np.argmax(predictions[0])
        predicted_class = self.class_names[predicted_index]
        confidence = float(np.max(predictions[0]) * 100)

        return {"predicted_class": predicted_class, "confidence": round(confidence, 2)}
