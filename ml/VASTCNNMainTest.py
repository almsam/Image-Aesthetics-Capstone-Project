import unittest
import numpy as np
import os
from VASTCNNMain import *

class TestModelPredictions(unittest.TestCase):
    
    def test_predictions(self):
        sample_img_path = os.path.join(image_dir, 'img 01L.png')  # use any image path
        img = load_img(sample_img_path, target_size=(32, 32))
        img_array = img_to_array(img) / 255.0  # normalize
        
        # predictin
        predicted_rating = model.predict(np.expand_dims(img_array, axis=0))[0][0]
        
        
        # check that the predicted rating is within a reasonable range, e.g., 0 to 1
        self.assertGreaterEqual(predicted_rating, 0.0, "Predicted rating is less than 0.")
        self.assertLessEqual(predicted_rating, 1.0, "Predicted rating is greater than 1.")
        
        print(f"Sample prediction for img 01L: {predicted_rating}")

unittest.main(argv=[''], exit=False)

class TestModelAccuracy(unittest.TestCase):
    
    def test_accuracy(self):
        test_accuracy = evaluate_L_R_predictions(model, image_dir, average_ratings)
        self.assertGreater(test_accuracy, 50, "Model accuracy is below 50%.")
        
        print(f"Test accuracy: {test_accuracy}%")

# run
unittest.main(argv=[''], exit=False)

