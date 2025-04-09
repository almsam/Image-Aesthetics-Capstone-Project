import os
import unittest

# Verify files are made

class TestModelFilesExistence(unittest.TestCase):
    def setUp(self):
        """Set up the paths to the model files"""
        self.model_paths = [
                            "C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/ml/models/CNN_Color_Model.h5",
                            "C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/ml/models/CNN_Contrast_Model.h5",
                            "C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/ml/models/CNN_Shape_Model.h5",
                            "C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/ml/models/CNN_Overall_Model.h5"
                            ]

    def test_model_files_exist(self):
        """Check if all model files exist"""
        for model_path in self.model_paths:
            with self.subTest(model_path=model_path):
                self.assertTrue(os.path.exists(model_path), f"Model file not found: {model_path}")


if __name__ == "__main__":
    unittest.main()