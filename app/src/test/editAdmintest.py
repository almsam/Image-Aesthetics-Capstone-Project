import unittest
import sqlite3
import bcrypt
import json
import os
import sys

# Adding the main file's path to sys.path so that editAdmin.py can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../main')))

from editAdmin import app, get_db_connection, DATABASE

class AdminEditingTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

        # Initialize the test database
        with app.app_context():
            self.init_db()

    def tearDown(self):
        # closing the database's connection and remove the test database
        with app.app_context():
            self.clear_db()

    def init_db(self):
        with get_db_connection() as conn:
            conn.execute('DROP TABLE IF EXISTS admin')
            conn.execute('''
                CREATE TABLE admin (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password_hash TEXT NOT NULL
                );
            ''')
            conn.commit()

    def clear_db(self):
        with get_db_connection() as conn:
            conn.execute('DROP TABLE IF EXISTS admin')
            conn.commit()
#----------------------------------------------------------------
    #testing the register_admin endpoint
    def test_register_admin_success(self):
        response = self.app.post('/register_admin', data=json.dumps({
            'username': 'admin1',
            'password': 'securepassword'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Admin registered successfully', response.data)
    #testing the register_admin endpoint with missing fields
    def test_edit_admin_username(self):
        # Register an admin first
        self.app.post('/register_admin', data=json.dumps({
            'username': 'admin1',
            'password': 'securepassword'
        }), content_type='application/json')

        # Edit the admin username
        response = self.app.put('/edit_admin_details', data=json.dumps({
            'username': 'admin1',
            'current_password': 'securepassword',
            'new_username': 'admin2'
        }), content_type='application/json')

        print(response.data)  # putting this to see what the response says on terminal
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Admin details updated successfully', response.data)
    #testing the register_admin endpoint with missing fields
    def test_edit_admin_password(self):
        # Register an admin first
        self.app.post('/register_admin', data=json.dumps({
            'username': 'admin1',
            'password': 'securepassword'
        }), content_type='application/json')

        # Edit the admin password
        response = self.app.put('/edit_admin_details', data=json.dumps({
            'username': 'admin1',
            'current_password': 'securepassword',
            'new_password': 'newpassword'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Admin details updated successfully', response.data)
    
    def test_edit_admin_invalid_password(self):
        # Register an admin first
        self.app.post('/register_admin', data=json.dumps({
            'username': 'admin1',
            'password': 'securepassword'
        }), content_type='application/json')

        # Try editing admin details with an incorrect current password
        response = self.app.put('/edit_admin_details', data=json.dumps({
            'username': 'admin1',
            'current_password': 'wrongpassword',
            'new_password': 'newpassword'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn(b'Invalid current password', response.data)

if __name__ == '__main__':
    unittest.main()
