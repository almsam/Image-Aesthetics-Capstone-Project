import unittest
import os
import sys

# Add the src/main directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main')))

from reference.deletefromDB import DeleteFromDatabase

class TestDeleteFromDatabase(unittest.TestCase):
    def setUp(self):
        self.db_path = ':memory:'
        self.deleter = DeleteFromDatabase(self.db_path)

        # Create table and insert sample data within the DeleteFromDatabase class
        self.deleter.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Images (
                image_id INTEGER PRIMARY KEY AUTOINCREMENT,
                image_path TEXT NOT NULL,
                height INTEGER,
                width INTEGER
            )
        """)
        
        self.deleter.cursor.execute("INSERT INTO Images (image_path, height, width) VALUES (?, ?, ?)", ('/path/to/image1.jpg', 100, 200))
        self.deleter.cursor.execute("INSERT INTO Images (image_path, height, width) VALUES (?, ?, ?)", ('/path/to/image2.jpg', 150, 250))
        self.deleter.conn.commit()

    def tearDown(self):
        self.deleter.close()

    def test_delete_image(self):
        self.deleter.delete_item('Images', 'image_id = ?', (1,))

        # Verify the deletion
        self.deleter.cursor.execute("SELECT * FROM Images WHERE image_id = 1")
        result = self.deleter.cursor.fetchone()
        self.assertIsNone(result)
        
        
if __name__ == '__main__':
    unittest.main()