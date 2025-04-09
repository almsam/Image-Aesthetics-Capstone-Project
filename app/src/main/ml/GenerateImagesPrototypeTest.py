import unittest
import numpy as np
from GenerateImagesPrototype import *

class TestGenerateRandomImage(unittest.TestCase):
    
    def test_same_seed_generates_same_image(self):
        """confirm we're deterministic"""
        seed = 96
        image1 = generate_random_image(seed=seed); image2 = generate_random_image(seed=seed)
        
        np.testing.assert_array_equal(
            image1, image2,
            err_msg="Images generated with same seed arent identical"
        )

    def test_returns_valid_image(self):
        image = generate_random_image(seed=123)
        
        self.assertIsInstance(image, np.ndarray, "Generated image is not a NumPy array")
        self.assertEqual(image.shape, (32, 32, 3), "Generated image does not have the correct shape")
        self.assertEqual(image.dtype, np.float32, "Generated image does not have the correct data type")

if __name__ == "__main__": unittest.main()
