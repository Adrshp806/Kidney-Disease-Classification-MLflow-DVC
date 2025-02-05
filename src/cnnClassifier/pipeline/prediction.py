import numpy as np
import tensorflow as tf
import os 
from pathlib import Path
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image 

import os


class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self):
        model_path = os.path.join("models", "model.h5")
        # model_path = Path("artifacts") / "training" / "model.h5"
        print(model_path)
        print(f"Loading model from: {model_path}")
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at {model_path}")
        
        model = load_model(model_path)

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Tumor'
            return [{ "image" : prediction}]
        else:
            prediction = 'Normal'
            return [{ "image" : prediction}]