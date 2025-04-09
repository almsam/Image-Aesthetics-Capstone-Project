import os
import unittest
from tensorflow.keras.preprocessing.image import img_to_array
import GenerateImage
import numpy as np

class TestGenerateImage(unittest.TestCase):

    def setUp(self):
        self.test_dir = "C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/generated_images/test"
        os.makedirs(self.test_dir, exist_ok=True)

    def test_generate_image_saves_file(self):
        image = GenerateImage.generateSmooth(96, "C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/generated_images")
        image_array = img_to_array(image)
        
        self.assertIsInstance(image_array, np.ndarray, "Generated image is not of correct type")
        
    def test_generate_2s(self):
        seed = 97
        GenerateImage.generateDoubleSmooth(seed, self.test_dir)
        
        first_smooth_path = os.path.join(self.test_dir, f"generated_image_smooth1_{seed}.png")
        second_smooth_path = os.path.join(self.test_dir, f"generated_image_smooth2_{seed}.png")
        
        self.assertTrue(os.path.exists(first_smooth_path), "First smoothed image was not saved")
        self.assertTrue(os.path.exists(second_smooth_path), "Second smoothed image was not saved")
    
    def test_generate_hd(self):
        seed = 24
        GenerateImage.generateQuality(seed, self.test_dir)
        
        hd_image_path = os.path.join(self.test_dir, f"generated_image_quality_{seed}.png")
        
        self.assertTrue(os.path.exists(hd_image_path), "HD image was not saved")


if __name__ == "__main__":
    unittest.main()
    
    print("Note: manually delete data/generated_images/generated_image_smooth_96.png")
