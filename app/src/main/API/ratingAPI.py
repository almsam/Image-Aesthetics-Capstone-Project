from flask import Blueprint, Flask, request, jsonify
from flask_cors import CORS
import logging
import sys
import os
import sqlite3

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from imageDB import ImageDatabase
db_path = os.getenv('DATABASE_PATH', 'imageDB.db')

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes 
db = ImageDatabase(db_path='imageDB.db')

logging.basicConfig(level = logging.DEBUG)  # Log all requests and errors to a file to check incase any errors are there to debug
rating_bp = Blueprint('rating', __name__)

@rating_bp.route('/api/ratings', methods=['POST'])
def submit_rating():
    from API.surveyAPI import email
    data = request.get_json()
    app.logger.debug(f"Received data: {data}")
    
    # Verify the incoming data
    if not data or 'choices' not in data:
        app.logger.error("Missing required fields: choices")
        return jsonify({"error": "Missing required fields: choices"}), 400

    choices = data['choices']

    # Validate data
    for choice in choices:
        if 'pairIndex' not in choice or 'selectedImageId' not in choice :
            app.logger.error("Missing required fields: pairIndex, selectedImageId")
            return jsonify({"error": "Missing required fields: pairIndex, selectedImageId"}), 400
        if not isinstance(choice['pairIndex'], int):
            app.logger.error("Invalid pairIndex format. It should be an integer.")
            return jsonify({"error": "Invalid pairIndex format. It should be an integer."}), 400
        if not isinstance(choice['selectedImageId'], int):
            app.logger.error("Invalid selectedImageId format. It should be an integer.")
            return jsonify({"error": "Invalid selectedImageId format. It should be an integer."}), 400

    # Send data to the database
    try:
        db = ImageDatabase(db_path=db_path)  # Create a new database connection for this request
        for choice in choices:
            db.cursor.execute("SELECT points FROM Images WHERE image_id = ?", (choice['selectedImageId'],))
            image_points = db.cursor.fetchone()
            if not image_points:
                app.logger.error(f"No points found for image_id: {choice['selectedImageId']}")
                return jsonify({"error": f"No points found for image_id: {choice['selectedImageId']}"}), 400
            new_points = image_points[0] + 1
            db.cursor.execute("INSERT INTO Rating (userEmail, questionNumber, image_id) VALUES (?, ?, ?)", (email, choice['pairIndex'] + 1, choice['selectedImageId']))
            db.cursor.execute("UPDATE Images SET points = ? WHERE image_id = ?", (new_points, choice['selectedImageId']))
        db.conn.commit()
        app.logger.info("Ratings successfully submitted!")
        return jsonify({"message": "Ratings successfully submitted!"}), 201
    except Exception as e: 
        app.logger.error(f"Error sending to db: {e}")
        return jsonify({"error": f"Error sending to db: {e}"}), 500
    finally:
        db.close()

@rating_bp.route('/api/ratings/results', methods=['GET'])
def get_image_stats():      # Get image stats based on image points and unique users
    try:
        db = ImageDatabase(db_path=db_path)
        from API.surveyAPI import email
        db.cursor.execute("SELECT Images.image_id, Images.points FROM Images JOIN Rating ON Images.image_id = Rating.image_id WHERE Rating.userEmail = ?", (email,))
        ratings = db.cursor.fetchall()
        if not ratings:
            app.logger.error(f"No ratings found for userEmail: {email}")
            return jsonify({"error": f"No ratings found for userEmail: {email}"}), 404
        stats=[]
        db.cursor.execute("SELECT DISTINCT userEmaiL FROM Rating")
        unique_users_tuple = db.cursor.fetchall()
        unique_users = len(unique_users_tuple)
        for rating in ratings:
            stats.append({
                "image_id" : rating[0],
                "percentage" : f"{(rating[1] / unique_users) * 100:.2f}%"
            })
        return jsonify({"stats": stats}), 200
        
    except sqlite3.Error as e:
        app.logger.error(f"Database error: {e}")
        return jsonify({"error": "Database error: "}), 500  
    finally:
        db.close()

@rating_bp.route('/api/ratings/fetch', methods=['GET'])
def fetch_ratings():
    try:
        db = ImageDatabase(db_path=db_path)
        db.cursor.execute("SELECT * FROM Rating")
        ratings = db.cursor.fetchall()
        if not ratings:
            app.logger.error("No ratings found!")
            return jsonify({"error": "No ratings found!"}), 404
        return jsonify({"ratings": ratings}), 200
    except sqlite3.Error as e:
        app.logger.error(f"Database error: {e}")
        return jsonify({"error": "Database error: "}), 500
    finally:
        db.close()

# New endpoint for submitting ratings for generated images
@rating_bp.route('/api/ratings', methods=['POST'])
def submit_generated_image_ratings():
    try:
        data = request.get_json()
        if not data or 'ratings' not in data:
            return jsonify({"error": "Missing required fields: ratings"}), 400

        ratings = data['ratings']
        if not isinstance(ratings, dict):
            return jsonify({"error": "Invalid data format"}), 400

        db = ImageDatabase(db_path=db_path)  
        for image_id, rating in ratings.items():
            if not isinstance(image_id, int) or not (1 <= rating <= 10):
                return jsonify({"error": "Invalid rating format. It should be an integer between 1 and 10."}), 400
            db.cursor.execute("INSERT INTO GeneratedImageRatings (image_id, rating) VALUES (?, ?)", (image_id, rating))

        db.conn.commit()
        return jsonify({"message": "Generated image ratings successfully submitted!"}), 201

    except Exception as e:
        app.logger.error(f"Error processing request: {e}")
        return jsonify({"error": "Internal server error"}), 500

    finally:
        db.close()

if __name__ == '__main__':
    app.run(debug=True)