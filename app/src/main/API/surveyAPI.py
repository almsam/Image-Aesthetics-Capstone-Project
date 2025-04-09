import sqlite3
from flask import Blueprint, Flask, request, jsonify
from flask_cors import CORS
import logging
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from imageDB import ImageDatabase
email = 'temp'
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes 

# Use environment variable for database path
db_path = os.getenv('DATABASE_PATH', 'imageDB.db')
db = ImageDatabase(db_path=db_path)

logging.basicConfig(level=logging.DEBUG)  # Log all requests and errors to a file to check in case any errors are there to debug
survey_bp = Blueprint('survey', __name__)

@survey_bp.route('/api/survey', methods=['POST'])  # now checking survey functionality with the database
def submit_survey():
    global email
    data = request.get_json()
    app.logger.debug(f"Received survey data: {data}")

    # first we validate incoming data
    if not data or 'age' not in data or 'gender' not in data or 'email' not in data:
        app.logger.error("Missing required fields: age, gender, email")
        return jsonify({"error": "Missing required fields: age, gender, email"}), 400

    age = data['age']
    gender = data['gender']
    email = data['email']
    arts_degree = data.get('artsDegree', False)

    # then we insert the survey data into the User table
    db = ImageDatabase(db_path=db_path)
    try:
        db.cursor.execute("INSERT INTO User (userEmail, userAge, userGender, visualArtsCourse) VALUES (?, ?, ?, ?)",
                          (email, age, gender, arts_degree))
        db.conn.commit()
        app.logger.info("Survey successfully submitted!")
        return jsonify({"message": "Survey successfully submitted!"}), 201
    except sqlite3.IntegrityError:
        app.logger.error("Survey submission failed: email already exists")
        return jsonify({"error": "Survey submission failed: email already exists"}), 400
    finally:
        db.close()

@survey_bp.route('/api/survey', methods=['GET'])
def get_surveys():
    app.logger.debug("Fetching survey data...")

    db = ImageDatabase(db_path=db_path)
    try:
        db.cursor.execute("SELECT userEmail, userAge, userGender, visualArtsCourse FROM User")
        users = db.cursor.fetchall()
        if users:
            user_data = [
                {
                    "email": user[0],
                    "age": user[1],
                    "gender": user[2],
                    "artsDegree": user[3]
                } for user in users
            ]
            app.logger.info("Fetched survey data")
            return jsonify(user_data), 200
        else:
            app.logger.error("No survey data found")
            return jsonify({"error": "No survey data found"}), 404
    except sqlite3.Error as e:
        app.logger.error(f"Database error: {e}")
        return jsonify({"error": "Database error"}), 500
    finally:
        db.close()

@survey_bp.route('/api/survey/<email>', methods=['DELETE'])
def delete_survey(email):
    app.logger.debug(f"Deleting survey data for email: {email}")

    db = ImageDatabase(db_path=db_path)
    try:
        db.cursor.execute("DELETE FROM User WHERE userEmail = ?", (email,))
        if db.cursor.rowcount == 0:
            app.logger.error(f"No survey data found for email: {email}")
            return jsonify({"error": "No survey data found"}), 404
        db.conn.commit()
        app.logger.info(f"Survey data deleted for email: {email}")
        return jsonify({"message": "Survey data deleted"}), 200
    except sqlite3.Error as e:
        app.logger.error(f"Database error: {e}")
        return jsonify({"error": "Database error"}), 500
    finally:
        db.close()

@survey_bp.route('/api/survey', methods=['PUT'])
def update_survey():
    data = request.json
    app.logger.debug(f"Received survey update data: {data}")

    if not data :
        app.logger.error("Missing required fields")
        return jsonify({"error": "Missing required fields"}), 400

    age = data.get('age')
    gender = data.get('gender')
    arts_degree = data.get('artsDegree')

    db = ImageDatabase(db_path=db_path)
    try:
        db.cursor.execute("SELECT * FROM User WHERE userEmail = ?", (email,))
        user = db.cursor.fetchone()
        if not user:
            app.logger.warning(f"Survey not found for update: {email}")
            return jsonify({"message": "Survey not found"}), 404

        update_fields = []
        update_values = []

        if age is not None:
            update_fields.append("userAge = ?")
            update_values.append(age)
        if gender is not None:
            update_fields.append("userGender = ?")
            update_values.append(gender)
        if arts_degree is not None:
            update_fields.append("visualArtsCourse = ?")
            update_values.append(arts_degree)

        update_values.append(email)

        db.cursor.execute(f"UPDATE User SET {', '.join(update_fields)} WHERE userEmail = ?", update_values)
        db.conn.commit()
        app.logger.info("Survey successfully updated!")
        return jsonify({"message": "Survey successfully updated!"}), 200
    except sqlite3.Error as e:
        app.logger.error(f"Database error: {e}")
        return jsonify({"error": "Database error"}), 500
    finally:
        db.close()

app.register_blueprint(survey_bp)

if __name__ == '__main__':
    app.run(debug=True)