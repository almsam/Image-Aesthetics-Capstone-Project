import unittest
from unittest.mock import patch
import sys
import os

# Adjust the path to include the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main')))

from imageGrouper import ImageGrouper

class TestImageGrouper(unittest.TestCase):

    @patch('imageGrouper.os.listdir')
    def test_group_images_pair(self, mock_listdir):
        mock_listdir.return_value = ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg']
        grouper = ImageGrouper('test_config.json', 'test.db')
        data = {'group_type': 'pair', 'num_questions': 1, 'image_folder': 'test_images'}
        groups = grouper.group_images(data)
        self.assertEqual(len(groups), 2)
        self.assertEqual(len(groups[0][0]), 2)
        self.assertEqual(len(groups[1][0]), 2)
    
    
    @patch('imageGrouper.os.listdir')
    def test_group_images_insufficient_images(self, mock_listdir):
        mock_listdir.return_value = ['image1.jpg']
        grouper = ImageGrouper('test_config.json', 'test.db')
        data = {'group_type': 'pair', 'num_questions': 2, 'image_folder': 'test_images'}
        with self.assertRaises(ValueError):
            groups = grouper.group_images(data)

    @patch('imageGrouper.os.listdir')
    def test_group_images_invalid_group_type(self, mock_listdir):
        mock_listdir.return_value = ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg']
        grouper = ImageGrouper('test_config.json', 'test.db')
        data = {'group_type': 'invalid_type', 'num_questions': 1, 'image_folder': 'test_images'}
        with self.assertRaises(ValueError):
            groups = grouper.group_images(data)

   

if __name__ == '__main__':
    unittest.main()