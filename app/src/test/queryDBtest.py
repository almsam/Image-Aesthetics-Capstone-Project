import unittest
import sqlite3

class TestQueryDatabase(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()

        # Create tables and insert data
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Images (
                image_id INTEGER PRIMARY KEY AUTOINCREMENT,
                image_path TEXT NOT NULL,
                height INTEGER,
                width INTEGER
            )
        """)
        
        self.cursor.execute("INSERT INTO Images (image_path, height, width) VALUES (?, ?, ?)", ('/path/to/image1.jpg', 100, 200))
        self.cursor.execute("INSERT INTO Images (image_path, height, width) VALUES (?, ?, ?)", ('/path/to/image2.jpg', 150, 250))
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_query_table(self):
        # Query all images
        self.cursor.execute("SELECT * FROM Images")
        images = self.cursor.fetchall()
        self.assertEqual(len(images), 2)

        # Query a specific image
        self.cursor.execute("SELECT * FROM Images WHERE image_id = ?", (1,))
        image = self.cursor.fetchone()
        self.assertEqual(image[1], '/path/to/image1.jpg')
        
if __name__ == '__main__':
    unittest.main()