import unittest
from unittest.mock import patch, mock_open
import os
import csv
from io import StringIO


from VASTprototypePyApp import save_choice_to_csv

class TestVastImageAppCSVRead(unittest.TestCase):

    def setUp(self):
        # mock CSV content
        self.csv_content = """Pair ID,Chosen Image ID,Choice
0,image_0.jpg,Left
1,image_3.jpg,Right
2,image_4.jpg,Left
"""
        self.expected_data = [
            {"Pair ID": "0", "Chosen Image ID": "image_0.jpg", "Choice": "Left"},
            {"Pair ID": "1", "Chosen Image ID": "image_3.jpg", "Choice": "Right"},
            {"Pair ID": "2", "Chosen Image ID": "image_4.jpg", "Choice": "Left"},
        ]

    @patch("builtins.open", new_callable=mock_open, read_data="""Pair ID,Chosen Image ID,Choice
0,image_0.jpg,Left
1,image_3.jpg,Right
2,image_4.jpg,Left
""")
    def test_read_csv_and_verify_content(self, mock_file):
        # actual CSV content
        actual_data = []
        with open("mock_vast_image_ratings.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                actual_data.append(row)

        # assertEqual
        self.assertEqual(len(actual_data), len(self.expected_data))
        for expected_row, actual_row in zip(self.expected_data, actual_data):
            self.assertDictEqual(expected_row, actual_row)


if __name__ == "__main__":
    unittest.main()