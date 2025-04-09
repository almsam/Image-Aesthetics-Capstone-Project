import sqlite3
from flask import Flask, request, jsonify
import bcrypt

app = Flask(__name__)

# Define SQLite database path
DATABASE = 'admin_login.db'     #just naming it admin_login.db for now temporarily

# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Function to create the database table for admin login if it doesn't exist
def init_db():
    with get_db_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS admins (
                admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL
            );
        ''')
        conn.commit()

# Initializing the database before the first request
@app.before_request
def setup():
    init_db()

# Endpoint to register a new admin
@app.route('/register_admin', methods=['POST'])
def register_admin():
    data = request.get_json()

    # then we chcek if all the required fields are provided
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Missing required fields: username, password"}), 400

    username = data['username']
    password = data['password']

    # Now we hash the password using bcrypt which is really useful with python
    hashedPW = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # then we try to insert the new admin into the database
    try:
        with get_db_connection() as conn:
            conn.execute('INSERT INTO admins (username, password_hash) VALUES (?, ?)', 
                         (username, hashedPW))
            conn.commit()
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username already exists."}), 400

    return jsonify({"message": "Admin registered successfully!"}), 201

# Endpoint to login an admin
@app.route('/login_admin', methods=['POST'])
def login_admin():
    data = request.get_json()

    # Check if all required fields are provided
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Missing required fields: username, password"}), 400

    username = data['username']
    password = data['password']

    # then we try to retrieve admin data from the database
    with get_db_connection() as conn:
        admin = conn.execute('SELECT * FROM admins WHERE username = ?', (username,)).fetchone()

        if admin is None:
            return jsonify({"error": "Admin not found."}), 404

        # verifying the password
        if not bcrypt.checkpw(password.encode('utf-8'), admin['password_hash']):
            return jsonify({"error": "Invalid password."}), 403

    return jsonify({"message": "Login successful!"}), 200

# running the Flask application
if __name__ == '__main__':
    app.run(debug=True)
