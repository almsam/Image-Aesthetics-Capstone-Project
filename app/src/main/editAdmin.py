import sqlite3
import bcrypt
from flask import Flask, request, jsonify

app = Flask(__name__)
DATABASE = 'admin_login.db'

# Connect to the database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Initialize the admin table before any requests are made
@app.before_request
def init_db():
    with get_db_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS admin (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL
            );
        ''')
        conn.commit()

# here we are regeistering an admin (gonna hash the password before storing)
@app.route('/register_admin', methods=['POST'])
def register_admin():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    # Hasingh the password
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        with get_db_connection() as conn:
            conn.execute('INSERT INTO admin (username, password_hash) VALUES (?, ?)',
                         (username, password_hash))
            conn.commit()
        return jsonify({'message': 'Admin registered successfully'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Admin with this username already exists'}), 409

# Verifying the admin login
@app.route('/login_admin', methods=['POST'])
def login_admin():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    with get_db_connection() as conn:
        admin = conn.execute('SELECT * FROM admin WHERE username = ?', (username,)).fetchone()

    if admin and bcrypt.checkpw(password.encode('utf-8'), admin['password_hash'].encode('utf-8')):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

# Now we try to edit admin details (username or password)
@app.route('/edit_admin_details', methods=['PUT'])
def edit_admin_details():
    data = request.get_json()

    if not data or 'username' not in data or 'current_password' not in data :
        return jsonify({"error": "Missing required fields: username, current_password"}), 400

    username = data['username']
    current_password = data['current_password']
    new_password = data.get('new_password')
    new_username = data.get('new_username')

    with get_db_connection() as conn:
        admin = conn.execute('SELECT * FROM admin WHERE username = ?', (username,)).fetchone()

        if admin and bcrypt.checkpw(current_password.encode('utf-8'), admin['password_hash']):
            if new_password:
                new_password_hash = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
                conn.execute('UPDATE admin SET password_hash = ? WHERE username = ?', (new_password_hash, username))
            if new_username:
                conn.execute('UPDATE admin SET username = ? WHERE username = ?', (new_username, username))
            conn.commit()
            return jsonify({"message": "Admin details updated successfully!"}), 200
        else:
            return jsonify({"error": "Invalid current password."}), 401

# running the Flask application
if __name__ == '__main__':
    app.run(debug=True)
