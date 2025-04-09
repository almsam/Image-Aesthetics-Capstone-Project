import unittest
import os
from PIL import Image
from VASTPreview import load_vast_images

class TestVastFunctions(unittest.TestCase):

    def setUp(self):
        self.test_dir = r'C:\Users\samia\OneDrive\Desktop\cosc 499\capstone-project-team-9-Order-Of-Aesthetics\data\VAST Images'
        
        # does dir exist?
        if not os.path.exists(self.test_dir): self.skipTest(f"Test directory {self.test_dir} does not exist.")

    def test_load_vast_images(self):
        images, filenames = load_vast_images(self.test_dir, num_images=5)
        
        # 3 tests
        
        for img in images:  self.assertIsInstance(img, Image.Image, "Loaded images should be instances of PIL.Image.Image")
        for filename in filenames: self.assertIsInstance(filename, str, "Filenames should be strings")
        self.assertEqual(len(images), len(filenames), "Number of images and filenames should match")
    

if __name__ == '__main__':
    unittest.main()
