import os
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Defining the SQLite database path

DATABASE = 'ratings.db'

# Function to connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Accessning rows as dictionaries, row_factory could eaily show us 
                                    # the row names and their values returned from the database
    return conn

# Function to create the database table if it doesn't exist
@app.before_request
def init_db():
    with get_db_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS image_ratings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                image_url TEXT NOT NULL,
                rating REAL NOT NULL CHECK(rating >= 0 AND rating <= 5),
                user_id INTEGER NOT NULL
            );
        ''')
        conn.commit()

# Endpoint to accept and verify incoming data
@app.route('/rate_image', methods=['POST'])
def rate_image():
    data = request.get_json()

    # Verify the incoming data
    if not data or 'image_url' not in data or 'rating' not in data or 'user_id' not in data:
        return jsonify({"error": "Missing required fields: image_url, rating, user_id"}), 400

    image_url = data['image_url']
    rating = data['rating']
    user_id = data['user_id']

    # Then we validate the data types

    if not isinstance(image_url, str):
        return jsonify({"error": "Invalid image_url format. It should be a string."}), 400
    if not isinstance(rating, (int, float)) or not (0 <= rating <= 5):
        return jsonify({"error": "Invalid rating. It should be a number between 0 and 5."}), 400
    if not isinstance(user_id, int):
        return jsonify({"error": "Invalid user_id format. It should be an integer."}), 400

     # Inserting data into the database

    with get_db_connection() as conn:
        conn.execute('INSERT INTO image_ratings (image_url, rating, user_id) VALUES (?, ?, ?)',
                     (image_url, rating, user_id))
        conn.commit()

    return jsonify({"message": "Rating successfully submitted!"}), 201

# Running the application
if __name__ == '__main__':
    app.run(debug=True)

