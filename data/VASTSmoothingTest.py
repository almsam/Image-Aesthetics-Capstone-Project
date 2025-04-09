import os
import unittest
import VASTSmoothing

class TestImageSaving(unittest.TestCase):
    
    def setUp(self):
        self.data_dir = r"C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/generated_images/"
        self.output_dir = r"C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/generated_images/smoothed_images/"
        self.seed = 100

    def test_image_saved(self):
        smoothed_image_path = r"C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/generated_images"
        self.assertTrue(os.path.exists(smoothed_image_path), f"File does not exist: {smoothed_image_path}")

if __name__ == "__main__":
    unittest.main()