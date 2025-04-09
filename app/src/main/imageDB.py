import sqlite3
import os

class ImageDatabase:
    def __init__(self, db_path='imageDB.db'):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Create Images table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Images (
                image_id INTEGER PRIMARY KEY AUTOINCREMENT,
                image_path TEXT NOT NULL,
                height INTEGER,
                width INTEGER,
                points INTEGER                       
            )
        """)
        
        # Create User table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS User (
                userEmail TEXT NOT NULL UNIQUE PRIMARY KEY,
                userAge INTEGER,
                userGender TEXT,
                visualArtsCourse BOOLEAN 
            )
        """)
        
        # Create Question table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Question (
                qid INTEGER PRIMARY KEY AUTOINCREMENT,
                question_text TEXT NOT NULL,
                image_id INTEGER,
                FOREIGN KEY (image_id) REFERENCES Images(image_id)
            )
        """)
        
        # Create Rating table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Rating (
                rating_id INTEGER PRIMARY KEY AUTOINCREMENT,
                userEmail TEXT NOT NULL,
                questionNumber INTEGER NOT NULL,
                image_id INTEGER NOT NULL,
                FOREIGN KEY (userEmail) REFERENCES User(userEmail),
                FOREIGN KEY (image_id) REFERENCES Images(image_id)
            )
        """)
        
        # Create Admin table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Admin (
                adminID INTEGER PRIMARY KEY AUTOINCREMENT,
                adminUsername TEXT NOT NULL,
                adminPassword TEXT NOT NULL                     
            )
        """)
        
        # Create GeneratedImageRatings table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS GeneratedImageRatings (
                rating_id INTEGER PRIMARY KEY AUTOINCREMENT,
                image_id INTEGER NOT NULL,
                rating INTEGER NOT NULL,
                FOREIGN KEY (image_id) REFERENCES Images(image_id)
            )
        """)
        
        self.conn.commit()

    def insert_initial_images(self):
        # Insert 100 records into the Images table
        for i in range(1, 101):
            self.cursor.execute("SELECT COUNT(*) FROM Images WHERE image_id = ?", (i,))
            if self.cursor.fetchone()[0] == 0:
                self.cursor.execute(
                    "INSERT INTO Images (image_id, image_path, points) VALUES (?, ?, ?)",
                    (i, "..\\..\\data\\VAST_Images", 0)
                )
        self.conn.commit()

    def insert_Admin(self, username, password):
        self.cursor.execute("INSERT INTO Admin (adminUsername, adminPassword) VALUES (?, ?)", (username, password))
        self.conn.commit()
        
    def close(self):
        self.conn.close()

if __name__ == "__main__":
    # Get the root directory of the project
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    db_path = os.path.join(root_dir, 'imageDB.db')
    db = ImageDatabase(db_path)
    print("Database initialized.")
    db.insert_initial_images()
    db.insert_Admin("admin", "admin123")
    db.close()
    print("Database connection closed.")