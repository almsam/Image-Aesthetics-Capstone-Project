import numpy as np
from tensorflow.keras.models import load_model, Model
from VASTReadModelMain import *
import unittest
import os

class TestModelMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.model_path = r'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/ml/models/VAST_CNN_Main_Model.h5'
        cls.image_dir = r'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/VAST Images'
        cls.csv_file = r'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/vast_image_ratings.csv'
        
        # stuffs from CSV
        image_ratings = defaultdict(list)
        with open(cls.csv_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                try:
                    image_id = row[0]
                    rating = int(row[2])  # Convert to int
                    image_ratings[image_id].append(rating)
                except ValueError:
                    print(f"Skipping invalid row: {row}")
        
        cls.average_ratings = {image_id: np.mean(ratings) for image_id, ratings in image_ratings.items()}
        
        # load cls model
        cls.model = load_model(cls.model_path)
        print("Model loaded for testing")

    def test_model(self):
        assert isinstance(self.model, Model), "Loaded model is not an instance of Model!" # test that the model is loaded correctly

    def test_predictable(self):
        # random image from the rated images to test prediction
        for filename in os.listdir(self.image_dir):
            if filename.endswith('.png'):
                img_id = os.path.splitext(filename)[0]
                normalized_id = img_id.split()[1][:-1]  # nrom
                
                if normalized_id in self.average_ratings:
                    img_path = os.path.join(self.image_dir, filename)
                    img = load_img(img_path, target_size=(32, 32))  # resize
                    img_array = img_to_array(img) / 255.0  # nrom
                    
                    predicted_rating = self.model.predict(np.expand_dims(img_array, axis=0))[0][0]
                    
                    assert predicted_rating is not None, f"Predicted rating for {img_id} is None"
                    assert isinstance(predicted_rating, (float, np.floating)), f"Predicted rating for {img_id} is not a float"
                    
                    print(f"Image {img_id}: Predicted Rating = {predicted_rating}")

    def test_L_R_prediction_accuracy(self):
        accuracy = evaluate_L_R_predictions(self.model, self.image_dir, self.average_ratings)
        print(f"L/R Prediction Accuracy: {accuracy:.2f}%")
        assert accuracy >= 0, "L/R Prediction Accuracy is negative"

if __name__ == '__main__':
    unittest.main()
