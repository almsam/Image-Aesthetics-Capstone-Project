import os
import unittest

class TestModelPredictions(unittest.TestCase):
    
    def test_predictions(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        save_path = os.path.join(script_dir, "hd_gallery_20seeds.png")

        print(os.path.exists(save_path))
        self.assertTrue(os.path.exists(save_path), f"Expected file {save_path} dne")



# run
unittest.main(argv=[''], exit=False)

# snapshot test:

# verify 20 HD images of 20 different seeds are visible