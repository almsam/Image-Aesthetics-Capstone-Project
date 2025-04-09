import sys
import os
import unittest
import json
import hashlib

# Add the src/main/auth directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../main/auth')))

from verifyAdmin import app, db

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

        # Initialize the database
        with db.conn:
            db.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Admin (
                    adminID INTEGER PRIMARY KEY AUTOINCREMENT,
                    adminUsername TEXT NOT NULL,
                    adminPassword TEXT NOT NULL 
                );
            ''')
            db.conn.commit()

        # Insert a test admin user
        with db.conn:
            db.cursor.execute('''
                INSERT INTO Admin (adminUsername, adminPassword)
                VALUES (?, ?)
            ''', ('admin', hashlib.sha256('admin123'.encode()).hexdigest()))
            db.conn.commit()

    def tearDown(self):
        # Clean up the database
        with db.conn:
            db.cursor.execute('DROP TABLE IF EXISTS Admin')
            db.conn.commit()

    def test_admin_login_success(self):
        # Test data
        test_data = {
            'username': 'admin',
            'password': 'admin123'
        }

        # Send POST request to /api/admin-login route
        response = self.app.post('/api/admin-login', data=json.dumps(test_data), content_type='application/json')

        # Check the response
        self.assertEqual(response.status_code, 200)
        self.assertIn('Login successful!', response.data.decode())

    def test_admin_login_missing_fields(self):
        # Test data with missing fields
        test_data = {
            'username': 'admin'
        }

        # Send POST request to /api/admin-login route
        response = self.app.post('/api/admin-login', data=json.dumps(test_data), content_type='application/json')

        # Check the response
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing required fields: username, password', response.data.decode())

    def test_admin_login_invalid_credentials(self):
        # Test data with invalid credentials
        test_data = {
            'username': 'admin',
            'password': 'wrongpassword'
        }

        # Send POST request to /api/admin-login route
        response = self.app.post('/api/admin-login', data=json.dumps(test_data), content_type='application/json')

        # Check the response
        self.assertEqual(response.status_code, 401)
        self.assertIn('Invalid credentials!', response.data.decode())

if __name__ == '__main__':
    unittest.main()