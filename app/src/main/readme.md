
# Image Rating and Admin Management System

This project is a web application built using Flask that allows admins to manage user registrations and logins, as well as allowing users to rate images. It uses SQLite as the database for storing user and image data, and bcrypt for password hashing.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database Structure](#database-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Admin registration and login
- Edit admin details
- User image rating
- Database management with SQLite
- Password hashing for secure storage

## Technologies

- Python
- Flask
- SQLite
- bcrypt
- Flask-CORS (for handling Cross-Origin Resource Sharing)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/COSC-499-W2024/capstone-project-team-9-Order-Of-Aesthetics.git
   cd yourrepository
   ```

2. Install the required packages:
   ```bash
   pip install Flask Flask-CORS bcrypt
   
   npm install
   ```

3. Create your SQLite database files if they do not exist. This will be done automatically when you run the application.

## Usage

1. Run the application:
   ```bash
   npm run dev
   ```

2. The application will be available at localhost 5000: `http://127.0.0.1:5000/`.

## API Endpoints

### Admin Management

- **Register Admin**
  - `POST /register_admin`
  - Request body: 
    ```json
    {
      "username": "admin_username",
      "password": "admin_password"
    }
    ```

- **Login Admin**
  - `POST /login_admin`
  - Request body:
    ```json
    {
      "username": "admin_username",
      "password": "admin_password"
    }
    ```

-
### Image Rating

- **Submit Rating**
  - `POST /api/ratings`
  - Request body:
    ```json
    {
      "imageId": 1,
      "rating": 5
    }
    ```

### Rate Image (from `verifydb.py`)

- **Rate Image**
  - `POST /rate_image`
  - Request body:
    ```json
    {
      "image_url": "http://example.com/image.jpg",
      "rating": 4,
      "user_id": 1
    }
    ```

## Database Structure

The application uses SQLite databases. The following tables are created:

- **Admin**
  - `admin_id`: INTEGER PRIMARY KEY
  - `username`: TEXT UNIQUE
  - `password_hash`: TEXT

- **Images**
  - `image_id`: INTEGER PRIMARY KEY
  - `image_path`: TEXT
  - `height`: INTEGER
  - `width`: INTEGER

- **User**
  - `userEmail`: TEXT UNIQUE PRIMARY KEY
  - `userAge`: INTEGER
  - `userGender`: TEXT
  - `visualArtsCourse`: BOOLEAN

- **Question**
  - `qid`: INTEGER PRIMARY KEY
  - `question_text`: TEXT
  - `image_id`: INTEGER (FK)

- **Rating**
  - `rating_id`: INTEGER PRIMARY KEY
  - `userEmail`: TEXT (FK)
  - `image_id`: INTEGER (FK)
  - `rating`: INTEGER

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any improvements or bugs.

## License

This project is licensed under the MIT License.
