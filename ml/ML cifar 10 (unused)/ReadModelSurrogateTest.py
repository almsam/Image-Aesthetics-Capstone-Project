import numpy as np
from tensorflow.keras.models import load_model, Model
from ReadModelSurrogate import *  # type: ignore
import unittest

class TestSurrogateModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # path shenanigans
        cifar_path = 'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/cifar-10-batches-py/data_batch_1'
        cls.model_paths = {
            "Color": 'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/ml/models/CNN_Color_Model.h5',
            "Contrast": 'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/ml/models/CNN_Contrast_Model.h5',
            "Shape": 'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/ml/models/CNN_Shape_Model.h5',
            "Overall": 'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/ml/models/CNN_Overall_Model.h5',
        }
    
        # load images
        images, _ = load_cifar_batch(cifar_path) # type: ignore
        images = reshape_images(images) / 255.0  # type: ignore # Normalize
        cls.test_image = np.expand_dims(images[0], axis=0)  # Use the first image for testing
        
        # load models
        cls.models = {}
        for rating_type, path in cls.model_paths.items():
            cls.models[rating_type] = load_model(path)
            
    def test_models_exist(self):
        for rating_type, model in self.models.items():
            with self.subTest(rating_type=rating_type):
                assert isinstance(model, Model), f"{rating_type} model is not a valid Keras Model"

    def test_model_predictions(self):
        for rating_type, model in self.models.items():
            with self.subTest(rating_type=rating_type):
                predicted_rating = model.predict(self.test_image)
                # Assert the prediction is a valid number
                assert predicted_rating is not None, f"{rating_type} predicted rating is None"
                assert isinstance(predicted_rating[0][0], (float, np.floating)), f"{rating_type} predicted rating is not a float"



if __name__ == '__main__':
    unittest.main()