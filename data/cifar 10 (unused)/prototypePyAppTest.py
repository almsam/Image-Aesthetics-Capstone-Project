import unittest
from unittest.mock import patch, mock_open
import pickle
import numpy as np
import os
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt


from prototypePyApp import load_cifar_batch, reshape_images, show_image_and_rate_terminal, rate_all_images

class TestCifarApp(unittest.TestCase):

    def setUp(self):
        self.mock_images = np.random.randint(255, size=(10000, 3, 32, 32))  # rand image data
        self.mock_labels = np.random.randint(10, size=(10000))  # rand labels (0-9)

    @patch("builtins.open", new_callable=mock_open)
    def test_load_cifar_batch(self, mock_file):
        with patch("pickle.load", return_value={'data': self.mock_images, 'labels': self.mock_labels}):
            images, labels = load_cifar_batch('mock_file_path')

        # asert returned images = mock data
        self.assertTrue(np.array_equal(images, self.mock_images))
        self.assertTrue(np.array_equal(labels, self.mock_labels))

    def test_reshape_images(self):
        # test reshape func
        reshaped_images = reshape_images(self.mock_images)
        self.assertEqual(reshaped_images.shape, (10000, 32, 32, 3))

    # @patch("builtins.input", side_effect=[5])
    # @patch("csv.writer")
    # @patch("matplotlib.pyplot.show")
    # def test_show_image_and_rate_terminal(self, mock_show, mock_csv_writer, mock_input):
    #     with patch("builtins.open", new_callable=mock_open) as mock_file:
    #         writer = mock_csv_writer.return_value
    #         show_image_and_rate_terminal(0)
    #         writer.writerow.assert_called_once_with([0, 5])

    # @patch("builtins.input", side_effect=['3', 'n'])
    # @patch("csv.writer")
    # @patch("matplotlib.pyplot.show")
    # def test_rate_all_images(self, mock_show, mock_csv_writer, mock_input):
    #     with patch("builtins.open", new_callable=mock_open):
    #         writer = mock_csv_writer.return_value
    #         rate_all_images()
    #         writer.writerow.assert_called_once_with([0, 5])
    # @patch('builtins.input', side_effect=['8', 'y', '6',  'y', '7',  'y', '5', 'n'])
    # def test_rate_all_images(self, mock_input):
    #     rate_all_images()


if __name__ == "__main__":
    unittest.main()

# note, to test the rate_all_images method, use input:

# 2, y, 8, y, 6, y, 2, n

# & assert the csv has the following:

# Image ID,Rating
# 0,2
# 1,8
# 2,6
# 3,2