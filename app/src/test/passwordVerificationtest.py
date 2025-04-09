import unittest
import json
import os
import sys

# Adding the main file's path to sys.path so that passswrodVerification.py can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../main')))

from passwordVerification import app, get_db_connection, DATABASE

class PasswordVerificationTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

        # aagain initialsing the test database
        with app.app_context():
            self.init_db()

    def tearDown(self):
        # then closing the database connection and remove the test database so no duplicates are there
        with app.app_context():
            self.clear_db()

    def init_db(self):
        with get_db_connection() as conn:
            conn.execute('DROP TABLE IF EXISTS admins')
            conn.execute('''
                CREATE TABLE admins (
                    admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password_hash TEXT NOT NULL
                )
            ''')
            conn.commit()

    def clear_db(self): #to clean the db after the tests
        with get_db_connection() as conn:
            conn.execute('DROP TABLE IF EXISTS admins')
            conn.commit()

#got to test the register_admin endpoint
    def test_register_admin_success(self):
        response = self.app.post('/register_admin', data=json.dumps({
            'username': 'admin1',
            'password': 'securepassword'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Admin registered successfully!', response.data)

#testing the register_admin endpoint with missing fields
    def test_register_admin_duplicate(self):
        self.app.post('/register_admin', data=json.dumps({
            'username': 'admin1',
            'password': 'securepassword'
        }), content_type='application/json')

        response = self.app.post('/register_admin', data=json.dumps({
            'username': 'admin1',
            'password': 'anotherpassword'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 409)
        self.assertIn(b'Username already exists.', response.data)

#testing the login_admin endpoint with valid credentials
    def test_login_admin_success(self):
        self.app.post('/register_admin', data=json.dumps({
            'username': 'admin1',
            'password': 'securepassword'
        }), content_type='application/json')

        response = self.app.post('/login_admin', data=json.dumps({
            'username': 'admin1',
            'password': 'securepassword'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login successful!', response.data)

#testing the login_admin endpoint with invalid credentials
    def test_login_admin_invalid(self):
        self.app.post('/register_admin', data=json.dumps({
            'username': 'admin1',
            'password': 'securepassword'
        }), content_type='application/json')

        response = self.app.post('/login_admin', data=json.dumps({
            'username': 'admin1',
            'password': 'wrongpassword'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn(b'Invalid password.', response.data)

if __name__ == '__main__':
    unittest.main()