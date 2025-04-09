import unittest
import os
import sqlite3
import sys

# Add the src/main directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main')))

from imageDB import ImageDatabase

class TestImageDatabase(unittest.TestCase):
    def setUp(self):
        # Set up a temporary database for testing.
        self.test_db_path = 'test_image_database.db'
        self.db = ImageDatabase(self.test_db_path)

    def tearDown(self):
        # Clean up the temporary database after tests.
        self.db.close()
        os.remove(self.test_db_path)

    def test_create_tables(self):
        # Test if the tables are created successfully.
        tables = ['Images', 'User', 'Question', 'Rating', 'Admin']
        self.db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        created_tables = [table[0] for table in self.db.cursor.fetchall()]
        self.assertTrue(all(table in created_tables for table in tables))

    def test_insert_initial_images(self):
        # Test if the initial images are inserted successfully.
        self.db.insert_initial_images()
        self.db.cursor.execute("SELECT COUNT(*) FROM Images;")
        count = self.db.cursor.fetchone()[0]
        self.assertEqual(count, 100)

    def test_connection(self):
        # Test if the database connection is established.
        self.assertIsInstance(self.db.conn, sqlite3.Connection)

    def test_insert_user(self):
        # Test inserting a user into the User table.
        self.db.cursor.execute(
            "INSERT INTO User (userEmail, userAge, userGender, visualArtsCourse) VALUES (?, ?, ?, ?)",
            ('test@example.com', 25, 'Male', True)
        )
        self.db.conn.commit()
        self.db.cursor.execute("SELECT * FROM User WHERE userEmail = 'test@example.com';")
        user = self.db.cursor.fetchone()
        self.assertIsNotNone(user)
        self.assertEqual(user[0], 'test@example.com')
        self.assertEqual(user[1], 25)
        self.assertEqual(user[2], 'Male')
        self.assertEqual(user[3], 1)  # BOOLEAN is stored as INTEGER in SQLite

    def test_insert_rating(self):
        # Test inserting a rating into the Rating table.
        self.db.cursor.execute(
            "INSERT INTO User (userEmail, userAge, userGender, visualArtsCourse) VALUES (?, ?, ?, ?)",
            ('test@example.com', 25, 'Male', True)
        )
        self.db.cursor.execute(
            "INSERT INTO Images (image_id, image_path, points) VALUES (?, ?, ?)",
            (1, 'path/to/image', 0)
        )
        self.db.cursor.execute(
            "INSERT INTO Rating (userEmail, questionNumber, image_id) VALUES (?, ?, ?)",
            ('test@example.com', 3, 5)
        )
        self.db.conn.commit()
        self.db.cursor.execute("SELECT * FROM Rating WHERE userEmail = 'test@example.com';")
        rating = self.db.cursor.fetchone()
        self.assertIsNotNone(rating)
        self.assertEqual(rating[1], 'test@example.com')
        self.assertEqual(rating[2], 3)
        self.assertEqual(rating[3], 5)

if __name__ == '__main__':
    unittest.main()