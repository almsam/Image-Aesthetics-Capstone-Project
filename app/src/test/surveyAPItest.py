import pytest
from flask import Flask
from flask.testing import FlaskClient
import sys
import os
import json  # Import json module for serialization

# Adjust the system path to import the app correctly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main')))
from API.surveyAPI import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Snapshot test for the /api/survey endpoint
def test_submit_survey(client, snapshot):
    print("Running test_submit_survey")
    
    # Define test data for survey submission
    test_data = {
    "age": 25,
    "gender": "male",
    "email": "unique_testuser_56789@example.com",  # Change this to ensure uniqueness
    "artsDegree": True
}
    
    print(f"Test data for survey: {test_data}")
    response = client.post('/api/survey', json=test_data)
    print(f"Response status code: {response.status_code}")
    print(f"Response JSON: {response.json}")

    assert response.status_code == 201  # Check for successful submission

    # Serialize the response JSON to a string for snapshot testing
    snapshot.assert_match(json.dumps(response.json), "submit_survey_snapshot")
    print("Finished test_submit_survey\n")

# Snapshot test for /api/survey with missing required fields
def test_submit_survey_missing_fields(client, snapshot):
    print("Running test_submit_survey_missing_fields")
    
    test_data = {
    "age": 25,
    "gender": "male",
    "email": "unique_testuser_67890@example.com",  # Using a unique email
   # not including artsDegree field here to check for the missing field
}

    print(f"Test data for missing fields: {test_data}")
    response = client.post('/api/survey', json=test_data)

    print(f"Response status code: {response.status_code}")
    print(f"Response JSON: {response.json}")

    assert response.status_code == 400  # Check for bad request due to missing fields

    # Serialize the response JSON to a string for snapshot testing
    snapshot.assert_match(json.dumps(response.json), "submit_survey_missing_fields_snapshot")
    print("Finished test_submit_survey_missing_fields\n")

# Test for the GET /api/survey endpoint
def test_get_surveys(client, snapshot):
    print("Running test_get_surveys")
    
    response = client.get('/api/survey')

    print(f"Response status code: {response.status_code}")
    print(f"Response JSON: {response.json}")

    assert response.status_code == 200  # Check for successful retrieval

    # Serialize the response JSON to a string for snapshot testing
    snapshot.assert_match(json.dumps(response.json), "get_surveys_snapshot")
    print("Finished test_get_surveys\n")

# Test for the DELETE /api/survey endpoint
def test_delete_survey(client, snapshot):
    print("Running test_delete_survey")
    
    # Define test data for survey deletion
    test_data = {
        "email": "unique_testuser_56789@example.com"  # Use the email from the submit test
    }
    
    print(f"Test data for survey deletion: {test_data}")
    response = client.delete('/api/survey', json=test_data)

    print(f"Response status code: {response.status_code}")
    print(f"Response JSON: {response.json}")

    assert response.status_code == 200  # Check for successful deletion

    # Serialize the response JSON to a string for snapshot testing
    snapshot.assert_match(json.dumps(response.json), "delete_survey_snapshot")
    print("Finished test_delete_survey\n")