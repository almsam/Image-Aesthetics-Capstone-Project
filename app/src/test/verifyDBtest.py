import unittest
import json
import os
import sqlite3
import sys

# Firts we add the main file's path to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../main')))

from verifyDB import app, DATABASE, get_db_connection # this helps in using the functions and variables from the main file

class ImageRatingTestCase(unittest.TestCase):

    def setUp(self):
        # then we set up the test client and create a test database
        app.config['TESTING'] = True
        self.app = app.test_client()
        
        # Initialize the database
        with app.app_context():
           self.init_db()  # Calling the setup function
            
         # Creating a new SQLite database for testing

        self.conn = sqlite3.connect(DATABASE)
        self.conn.execute('DROP TABLE IF EXISTS image_ratings')
        self.conn.execute(''' 
            CREATE TABLE image_ratings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                image_url TEXT NOT NULL,
                rating REAL NOT NULL CHECK(rating >= 0 AND rating <= 5),
                user_id INTEGER NOT NULL
            );
        ''')
        self.conn.commit()

    def tearDown(self):
        # this helps in cleaning up after the tests
        self.conn.close()
       
    def init_db(self):
        with get_db_connection() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS image_ratings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    image_url TEXT NOT NULL,
                    rating REAL NOT NULL,
                    user_id INTEGER NOT NULL
                )
            ''')
            conn.commit()

    def test_rate_image_success(self):
        # Test valid rating submission
        res = self.app.post('/rate_image', data=json.dumps({
            'image_url': 'http://example.com/image.jpg',
            'rating': 4.5,
            'user_id': 1
        }), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn(b"Rating successfully submitted!", res.data)

    def test_missing_fields(self):
        # Test missing fields
        res = self.app.post('/rate_image', data=json.dumps({
            'rating': 4.5,
            'user_id': 1
        }), content_type='application/json')
        self.assertEqual(res.status_code, 400)
        self.assertIn(b"Missing required fields: image_url, rating, user_id", res.data)

    def test_invalid_rating(self):
        # Test invalid rating value
        res = self.app.post('/rate_image', data=json.dumps({
            'image_url': 'http://example.com/image.jpg',
            'rating': 6,
            'user_id': 1
        }), content_type='application/json')
        self.assertEqual(res.status_code, 400)
        self.assertIn(b"Invalid rating. It should be a number between 0 and 5.", res.data)

    def test_invalid_user_id(self):
        # Test invalid user ID format
        res = self.app.post('/rate_image', data=json.dumps({
            'image_url': 'http://example.com/image.jpg',
            'rating': 4.5,
            'user_id': 'abc'
        }), content_type='application/json')
        self.assertEqual(res.status_code, 400)
        self.assertIn(b"Invalid user_id format. It should be an integer.", res.data)

if __name__ == '__main__':
    unittest.main()