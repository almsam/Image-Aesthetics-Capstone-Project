import sqlite3
from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)
#doing the password verification for the admin only as for user it is not needed
DATABASE = 'imageDB.db'  # just for naming it admin_login.db for now temporarily

# making thsi to connect to the database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# then makig the function to create the database table for admin login if it does not exist
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

# then we go ahead and initialise the database before any request
@app.before_request
def setup():
    init_db()

# Endpoint to register a new admin
@app.route('/register_admin', methods=['POST'])
def register_admin():
    data = request.get_json()

    # checking if all the required fields are provided
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Missing required fields: username, password"}), 400

    username = data['username']
    password = data['password']

    # Hashing the password using hashlib as done earlier for another task
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # then after creating we insert the new admin into the database
    try:
        with get_db_connection() as conn:
            conn.execute('INSERT INTO admins (username, password_hash) VALUES (?, ?)', 
                         (username, hashed_password))
            conn.commit()
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username already exists."}), 409

    return jsonify({"message": "Admin registered successfully!"}), 201

# then like registering this is the endpoint to login an admin
@app.route('/login_admin', methods=['POST'])
def login_admin():
    data = request.get_json()

    # checking if all required fields are provided
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Missing required fields: username, password"}), 400

    username = data['username']
    password = data['password']

    # trying to retrieve the admin from the database
    with get_db_connection() as conn:
        admin = conn.execute('SELECT * FROM admins WHERE username = ?', (username,)).fetchone()

        if admin is None:
            return jsonify({"error": "Admin not found."}), 404

        # verifying the password
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if hashed_password != admin['password_hash']:
            return jsonify({"error": "Invalid password."}), 401

    return jsonify({"message": "Login successful!"}), 200

# running the Flask application
if __name__ == '__main__':
    app.run(debug=True)