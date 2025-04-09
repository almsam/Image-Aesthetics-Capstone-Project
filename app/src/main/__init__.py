from flask import Flask, redirect
from flask_cors import CORS
import logging
#from imageDB import ImageDatabase

#def create_app():
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
#db = ImageDatabase(db_path='imageDB.db')

logging.basicConfig(level=logging.DEBUG)  # Log all requests and errors to a file to check in case any errors are there to debug

# Register blueprints or import modules
from API.surveyAPI import survey_bp
from API.adminAPI import admin_bp
from API.ratingAPI import rating_bp

app.register_blueprint(survey_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(rating_bp)

@app.route('/')
def index():
    return redirect('http://localhost:3001')

#return app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
#create_app().run(debug=True)