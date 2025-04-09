import os
import unittest

class TestModelPredictions(unittest.TestCase):
    
    def test_predictions(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        save_path = os.path.join(script_dir, "gallery_4seeds.png")

        print(os.path.exists(save_path))
        self.assertTrue(os.path.exists(save_path), f"Expected file {save_path} dne")



# run
unittest.main(argv=[''], exit=False)

# snapshot test:

# verify 16 images of 4 different seeds are visible
# verify the 1st 4 are raw input (B/W/G pixels)
# verify the 2nd/3rd 4 are smoothed (B/W pixels with 3rd col having less noise then 2nd)
# verify the last 4 are HD