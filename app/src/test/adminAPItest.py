import pytest
from flask import Flask
from flask.testing import FlaskClient
import sys
import os
import json  # Import json module for serialization

# Adjust the system path to import the app correctly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main')))
from API.adminAPI import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_admin_login_success(client, mocker):
    print("Running test_admin_login_success")
    
    mocker.patch('app.src.test.adminAPItest.ImageDatabase')
    mock_db = app.src.test.adminAPItest.ImageDatabase.return_value
    mock_db.cursor.fetchone.return_value = {'adminUsername': 'admin', 'adminPassword': 'hashed_password'}

    response = client.post('/api/admin-login', json={
        'username': 'admin',
        'password': 'password'
    })

    print(f"Response status code: {response.status_code}")
    print(f"Response JSON: {response.json}")
    
    assert response.status_code == 200
    assert response.json == {"message": "Login successful!"}
    print("Finished test_admin_login_success\n")

def test_admin_login_missing_fields(client):
    print("Running test_admin_login_missing_fields")
    
    response = client.post('/api/admin-login', json={})

    print(f"Response status code: {response.status_code}")
    print(f"Response JSON: {response.json}")
    
    assert response.status_code == 400
    assert response.json == {"error": "Missing required fields: username, password"}
    print("Finished test_admin_login_missing_fields\n")

def test_admin_login_invalid_credentials(client, mocker):
    print("Running test_admin_login_invalid_credentials")
    
    mocker.patch('app.src.test.adminAPItest.ImageDatabase')
    mock_db = app.src.test.adminAPItest.ImageDatabase.return_value
    mock_db.cursor.fetchone.return_value = None

    response = client.post('/api/admin-login', json={
        'username': 'admin',
        'password': 'wrong_password'
    })

    print(f"Response status code: {response.status_code}")
    print(f"Response JSON: {response.json}")
    
    assert response.status_code == 401
    assert response.json == {"error": "Invalid credentials!"}
    print("Finished test_admin_login_invalid_credentials\n")