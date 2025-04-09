import numpy as np
from tensorflow.keras.models import load_model, Model
# from readModelmain import load_cifar_batch, reshape_images
from ReadModelMain import * # type: ignore

import unittest


class TestRegressionMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        
        cifar_path = 'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/cifar-10-batches-py/data_batch_1'
        cls.model_path = 'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/ml/models/CNN_Main_Model.h5'
        # load images
        images, _ = load_cifar_batch(cifar_path)
        images = reshape_images(images) / 255.0  # normalize
        cls.test_image = np.expand_dims(images[0], axis=0)  # use the first image for testing
        # load model
        cls.model = load_model(cls.model_path)

    def test_model(self):
        model = load_model(self.model_path)
        assert isinstance(model, Model), "object is not a model"

    def test_predictable(self):
        # predict
        predicted_rating = self.model.predict(self.test_image)
        # assert that the predicted rating is a valid number
        assert predicted_rating is not None, "predicted rating is none"
        assert isinstance(predicted_rating[0][0], (float, np.floating)), "predicted rating is not a float"


if __name__ == '__main__':
    unittest.main()