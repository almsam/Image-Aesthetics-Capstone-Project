import unittest
import os
import sys

# Add the src/main directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main')))

from reference.insertImageDB import DatabaseInserter

class TestDatabaseInserter(unittest.TestCase):
    def setUp(self):
        # Create a temporary database for testing
        self.test_db_path = 'test_database.db'
        self.db_inserter = DatabaseInserter(self.test_db_path)

    def tearDown(self):
        # Close the database connection and remove the temporary database
        self.db_inserter.close()
        os.remove(self.test_db_path)

    def test_create_table(self):
        # Check if the table is created successfully
        self.db_inserter.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='images';")
        table_exists = self.db_inserter.cursor.fetchone()
        self.assertIsNotNone(table_exists)

    def test_insert_record(self):
        # Insert a record and check if it is inserted correctly
        self.db_inserter.insert_record('path/to/image.jpg', 5, 123)
        self.db_inserter.cursor.execute("SELECT * FROM images WHERE img_path='path/to/image.jpg';")
        record = self.db_inserter.cursor.fetchone()
        self.assertIsNotNone(record)
        self.assertEqual(record[1], 'path/to/image.jpg')
        self.assertEqual(record[2], 5)
        self.assertEqual(record[3], 123)

if __name__ == '__main__':
    unittest.main()