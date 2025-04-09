import unittest
import json
import os
import sqlite3
import sys

# First we add the main file's path to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../main')))

from passwordHashing import app, DATABASE

class AdminAuthTestCase(unittest.TestCase):

    def setUp(self):
        # Then we setup the test client and initialize the database for testing
        app.config['TESTING'] = True
        self.app = app.test_client()

        # Now initialising the database for testing and assign it to self.conn
        self.conn = sqlite3.connect(DATABASE)   #the values id, username and password are just basic as of now
        self.conn.execute('DROP TABLE IF EXISTS admin') #and maybe changed in the future
        self.conn.execute('''
            CREATE TABLE admin (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL      
            )
        ''')
        self.conn.commit()
        self.conn.close()  # Closing the connection after setup

    def tearDown(self):
        # Incsae the database connection is still open we close
        if hasattr(self, 'conn') and self.conn:
            self.conn.close()
        
        # removing the database file after the connection is closed
        if os.path.exists(DATABASE):
            try:
                os.remove(DATABASE)
            except PermissionError as e:
                print(f"Error removing the database: {e}")  #this part may need to be polished further

    def init_db(self):
        # satrting a new test database
        with sqlite3.connect(DATABASE) as conn:
            conn.execute('DROP TABLE IF EXISTS admins')
            conn.execute('''
                CREATE TABLE admins (
                    admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password_hash TEXT NOT NULL
                );
            ''')
            conn.commit()

        print(res.data)  # Add logging to see the res data
        self.assertEqual(res.status_code, 201)
        self.assertIn(b"Admin registered successfully!", res.data)

    def test_register_admin_missing_fields(self):
        # Test registration with missing fields
        res = self.app.post('/register_admin', data=json.dumps({
            'username': 'admin1'
        }), content_type='application/json')

        self.assertEqual(res.status_code, 400)
        self.assertIn(b"Missing required fields: username, password", res.data)

    def test_register_admin_same_username(self):
        # Test registering the same username twice should lead to a fail as thats not logical
        self.app.post('/register_admin', data=json.dumps({
            'username': 'admin1',
            'password': 'password123'
        }), content_type='application/json')

        res = self.app.post('/register_admin', data=json.dumps({
            'username': 'admin1',
            'password': 'password456'
        }), content_type='application/json')

        self.assertEqual(res.status_code, 400)
        self.assertIn(b"Username already exists.", res.data)

    def test_login_admin_success(self):
        # Register an admin first
        self.app.post('/register_admin', data=json.dumps({
            'username': 'admin1',
            'password': 'password123'
        }), content_type='application/json')

        # Testign successful login
        res = self.app.post('/login_admin', data=json.dumps({
            'username': 'admin1',
            'password': 'password123'
        }), content_type='application/json')

        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Login successful!", res.data)

    def test_login_admin_wrong_password(self):
        # Register an admin first
        self.app.post('/register_admin', data=json.dumps({
            'username': 'admin1',
            'password': 'password123'
        }), content_type='application/json')

        # Testing login with the wrong password
        res = self.app.post('/login_admin', data=json.dumps({
            'username': 'admin1',
            'password': 'wrongpassword'
        }), content_type='application/json')

        self.assertEqual(res.status_code, 403)
        self.assertIn(b"Invalid password.", res.data)

    def test_login_admin_nonexistent(self):
        # Tesing login with a non-existent username
        res = self.app.post('/login_admin', data=json.dumps({
            'username': 'nonexistent_admin',
            'password': 'password123'
        }), content_type='application/json')

        self.assertEqual(res.status_code, 404)
        self.assertIn(b"Admin not found.", res.data)

if __name__ == '__main__':
    unittest.main()