import unittest
import os
import numpy
import GenerateImagesPrototype
from GenerateImage import generateQuality

class TestImageGeneration(unittest.TestCase):

    def test_generate_new_image_class(self):
        """Test that GenerateImagesPrototype.generate_New_Image returns the expected class."""
        image = GenerateImagesPrototype.generate_New_Image(22)
        self.assertIsInstance(image, numpy.ndarray)

    def test_generate_quality_class(self):
        """Test that generateQuality returns the expected class."""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(script_dir, "public", "data", "temp")
        os.makedirs(output_dir, exist_ok=True)

        seed = 12345
        generated_image = generateQuality(seed, output_dir, n=72)

        print(generated_image.__class__)
        
        self.assertIsInstance(generated_image, numpy.ndarray)

    def test_run_success(self):
        """Test that RunSuccess is set to 1 after execution."""
        global RunSuccess
        RunSuccess = 0  # make sure it's reset
        exec(open("ExampleUsage.py").read())
        RunSuccess = 1
        self.assertEqual(RunSuccess, 1)

if __name__ == "__main__":
    unittest.main()
