import sys
import os
from flask import Blueprint, Flask, request, jsonify, send_file
from flask_cors import CORS
import logging
import hashlib

# Add the src/main directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from imageDB import ImageDatabase

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes 

# Use environment variable for database path
db_path = os.getenv('DATABASE_PATH', 'imageDB.db')
db = ImageDatabase(db_path=db_path)

logging.basicConfig(level=logging.DEBUG)  # Log all requests and errors to a file to check in case any errors are there to debug
admin_bp = Blueprint('admin', __name__)
@admin_bp.route('/api/admin-login', methods=['POST'])
def admin_login():
    data = request.get_json()
    app.logger.debug(f"Received login data: {data}")

    # Verify the incoming data
    if not data or 'username' not in data or 'password' not in data:
        app.logger.error("Missing required fields: username, password")
        return jsonify({"error": "Missing required fields: username, password"}), 400

    username = data['username']
    password = data['password']

    # Hash the password (assuming passwords are stored as hashes in the database)
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    # Log the hashed password
    app.logger.debug(f"Hashed password: {password_hash}")
    
    # Check the credentials against the database
    db = ImageDatabase(db_path=db_path)
    db.cursor.execute("SELECT * FROM Admin WHERE adminUsername = ? AND adminPassword = ?", (username, password_hash))
    admin = db.cursor.fetchone()
    db.close()

    if admin:
        app.logger.info("Admin login successful!")
        return jsonify({"message": "Login successful!"}), 200
    else:
        app.logger.error("Invalid credentials!")
        return jsonify({"error": "Invalid credentials!"}), 401


@admin_bp.route('/api/export', methods=['POST'])
def export_data():
    db = ImageDatabase(db_path=db_path)
    db.cursor.execute("SELECT * FROM Rating")
    ratings = db.cursor.fetchall()

    if not ratings:
        app.logger.error("No ratings found!")
        return jsonify({"error": "No ratings found!"}), 404
    
    # Correct file path (in project root directory)
    file_path = os.path.join(os.getcwd(), "ratings.csv")
    
    # Export the ratings data to a CSV file
    try:
        with open(file_path, 'w') as f:
            f.write("rating_id, userEmail,question_id,image_id\n")
            for rating in ratings:
                f.write(f"{rating[0]},{rating[1]},{rating[2]},{rating[3]}\n")
        app.logger.info("Ratings data exported successfully!")
        return send_file(file_path, as_attachment=True, download_name='ratings.csv'), 200
    except Exception as e:
        app.logger.error(f"Error exporting ratings data: {e}")
        return jsonify({"error": f"Error exporting ratings data: {e}"}), 500
    finally:
        db.close()

if __name__ == '__main__':
    app.run(debug=True)