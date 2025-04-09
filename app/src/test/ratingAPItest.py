


import pytest
from flask import Flask
from flask.testing import FlaskClient
import sys
import os
import json  # Import json module for serialization

# Adjust the system path to import the app correctly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main')))
from API.ratingAPI import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Snapshot test for the /api/ratings endpoint
def test_submit_rating(client, snapshot):
    print("Running test_submit_rating")
    
    # Define test data for rating submission
    test_data = {
        "imageId": 1,
        "rating": 8
    }
    
    print(f"Test data for rating: {test_data}")
    response = client.post('/api/ratings', json=test_data)

    print(f"Response status code: {response.status_code}")
    print(f"Response JSON: {response.json}")
    
    assert response.status_code == 201  # Check for successful submission
    
    # Serialize the response JSON to a string for snapshot testing
    snapshot.assert_match(json.dumps(response.json), "submit_rating_snapshot")
    print("Finished test_submit_rating\n")

def test_submit_rating_missing_fields(client):
    test_data = {
        "choices": [
            {"pairIndex": 0}
        ]
    }
    response = client.post('/api/ratings', json=test_data)
    assert response.status_code == 400
    assert response.json == {"error": "Missing required fields: pairIndex, selectedImageId"}

def test_increment_image_points(client):
    response = client.post('/api/ratings/increment')
    assert response.status_code == 200
    assert response.json == {"message": "Image points successfully incremented based on CSV data!"}

def test_get_image_stats(client):
    response = client.get('/api/ratings/stats?image_id=1')
    assert response.status_code == 200
    assert "image_points" in response.json
    assert "unique_users" in response.json
    assert "percentage" in response.json

def test_get_image_stats_missing_image_id(client):
    response = client.get('/api/ratings/stats')
    assert response.status_code == 400
    assert response.json == {"error": "Missing required field: image_id"}

