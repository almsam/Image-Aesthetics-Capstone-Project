import os
import unittest
import VASTGeneratingExperiment

class TestImageGeneration(unittest.TestCase):

    def setUp(self):
        self.seeds = [100, 300, 500]  # Test for these seeds
        self.output_dir = r"C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/generated_images/"
        
    def test_images_generated(self):
        for seed in self.seeds:
            image_path = os.path.join(self.output_dir, f"generated_image_{seed}.png")
            self.assertTrue(os.path.exists(image_path), f"File does not exist: {image_path}")

if __name__ == "__main__":
    unittest.main()
