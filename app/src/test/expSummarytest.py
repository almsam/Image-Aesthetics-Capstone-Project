import sqlite3
import unittest
import os
import sys
# Adjust the path to include the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main')))

# Import the functions from main/exp.py
from reference.expSummary import get_unique_participants_count, increment_image_point, get_image_percentage

class TestExpSummary(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE User (userEmail TEXT)")
        self.cursor.execute("CREATE TABLE Images (image_id INTEGER, points INTEGER)")
        self.cursor.execute("INSERT INTO User (userEmail) VALUES ('user1@example.com')")
        self.cursor.execute("INSERT INTO User (userEmail) VALUES ('user2@example.com')")
        self.cursor.execute("INSERT INTO Images (image_id, points) VALUES (1, 0)")
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_get_unique_participants_count(self):
        count = get_unique_participants_count(self.cursor)
        self.assertEqual(count, 2)

    def test_increment_image_point(self):
        increment_image_point(self.cursor, 1)
        self.cursor.execute("SELECT points FROM Images WHERE image_id = 1")
        points = self.cursor.fetchone()[0]
        self.assertEqual(points, 1)

    def test_get_image_percentage(self):
        total_participants = get_unique_participants_count(self.cursor)
        increment_image_point(self.cursor, 1)
        self.conn.commit()
        percentage = get_image_percentage(self.cursor, 1, total_participants)
        self.assertAlmostEqual(percentage, 50.0)

if __name__ == '__main__':
    unittest.main()