import os
import unittest
from tensorflow.keras.preprocessing.image import img_to_array
import GenerateImage
import numpy as np

class TestGenerateImage(unittest.TestCase):

    def test_generate_image_saves_file(self):
        image = GenerateImage.generateSmooth(96, "C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/generated_images")
        image_array = img_to_array(image)
        
        self.assertIsInstance(image_array, np.ndarray, "Generated image is not of correct type")

if __name__ == "__main__":
    unittest.main()
    
    print("Note: manually delete data/generated_images/generated_image_smooth_96.png")
