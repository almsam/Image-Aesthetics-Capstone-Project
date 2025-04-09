import unittest
from unittest.mock import patch, mock_open
import pickle
import numpy as np
import os
import csv
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt

from prototypePyAppV2 import load_cifar_batch, reshape_images, show_image_and_rate_terminal, rate_all_images, get_last_rated_image_id

class TestCifarApp(unittest.TestCase):

    csv_file = 'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/prototype_image_ratings.csv'
    file_exists = os.path.exists(csv_file)
    mock_csv_data = """Image ID,Rating
0,2
1,8
2,6
"""

    def setUp(self):
        self.mock_images = np.random.randint(255, size=(10000, 3, 32, 32))  # rand image data
        self.mock_labels = np.random.randint(10, size=(10000))  # rand labels (0-9)

    @patch("builtins.open", new_callable=mock_open)
    def test_load_cifar_batch(self, mock_file):
        with patch("pickle.load", return_value={'data': self.mock_images, 'labels': self.mock_labels}):
            images, labels = load_cifar_batch('mock_file_path')
            mock_csv_data = """Image ID,Rating
0,2
1,8
2,6
"""

        # asert returned images = mock data
        self.assertTrue(np.array_equal(images, self.mock_images))
        self.assertTrue(np.array_equal(labels, self.mock_labels))

    def test_reshape_images(self):
        reshaped_images = reshape_images(self.mock_images)
        self.assertEqual(reshaped_images.shape, (10000, 32, 32, 3))

    @patch("builtins.open", new_callable=mock_open, read_data=mock_csv_data)
    def test_get_last_rated_image_id(self, csv_file):
        csv_file = 'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/prototype_image_ratings.csv'
        last_rated_image_id = get_last_rated_image_id(csv_file)
        self.assertGreaterEqual(last_rated_image_id, 1)



if __name__ == "__main__":
    unittest.main()


# Snapshot test the CSV has the  following:

# Image ID,Rating
# 0,2
# 1,8
# 2,6
# 3,2