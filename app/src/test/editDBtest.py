import unittest
import os
import sys

# Add the src/main directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main')))

from reference.editDB import EditDatabase  

class TestEditDatabase(unittest.TestCase):
    def setUp(self):
        #Set up a temporary database for testing.
        self.test_db_path = 'test_edit_database.db'
        self.db = EditDatabase(self.test_db_path)
        
        # Create tables 
        self.db.cursor.execute("""--sql
            CREATE TABLE IF NOT EXISTS Images (
                image_id INTEGER PRIMARY KEY AUTOINCREMENT,
                image_path TEXT NOT NULL,
                height INTEGER,
                width INTEGER                       
            )
        """)
        #create user table with user id, email, age, gender
        self.db.cursor.execute("""--sql
            CREATE TABLE IF NOT EXISTS User (
                userEmail TEXT NOT NULL UNIQUE PRIMARY KEY,
                userAge INTEGER,
                userGender TEXT,
                visualArtsCourse BOOLEAN 
            )
        """)
        #create questions table with qid, text, and imageid
        self.db.cursor.execute("""--sql
            CREATE TABLE IF NOT EXISTS Question (
                qid INTEGER PRIMARY KEY AUTOINCREMENT,
                question_text TEXT NOT NULL,
                image_id INTEGER,
                FOREIGN KEY (image_id) REFERENCES Images(image_id)
            )
        """)
        #create rating table with ratingid, uid, imageid, and rating
        self.db.cursor.execute("""--sql
            CREATE TABLE IF NOT EXISTS Rating (
                rating_id INTEGER PRIMARY KEY AUTOINCREMENT,
                userEmail TEXT NOT NULL,
                image_id INTEGER NOT NULL,
                rating INTEGER,
                FOREIGN KEY (userEmail) REFERENCES User(userEmail),
                FOREIGN KEY (image_id) REFERENCES Images(image_id)
                UNIQUE(userEmail, image_id)
            )
        """)
        # create admin table with adminEmail, adminUsername, and adminPassword
        self.db.cursor.execute("""--sql
            CREATE TABLE IF NOT EXISTS Admin (
                adminEmail TEXT NOT NULL UNIQUE PRIMARY KEY,
                adminUsername TEXT NOT NULL,
                adminPassword TEXT NOT NULL                     
            )
        """)

    def tearDown(self):
        #Clean up the temporary database after tests.
        self.db.close()
        os.remove(self.test_db_path)



    def test_update_question(self):
        # Insert a question to update
        self.db.cursor.execute("INSERT INTO Question (question_text, image_id) VALUES (?, ?)", ('Original question', 1))
        self.db.conn.commit()

        # Update the question
        editor = EditDatabase(self.test_db_path)  
        editor.update_question(qid=1, new_text='Updated question')


        # Verify the update
        self.db.cursor.execute("SELECT question_text FROM Question WHERE qid = 1")
        result = self.db.cursor.fetchone()
        self.assertEqual(result[0], 'Updated question')
        
    def test_update_rating(self):
        # Insert a rating to update
        self.db.cursor.execute("INSERT INTO User (userEmail, userAge, userGender, visualArtsCourse) VALUES (?, ?, ?, ?)", ('test@example.com', 25, 'Male', True))
        self.db.cursor.execute("INSERT INTO Images (image_path, height, width) VALUES (?, ?, ?)", ('/path/to/image.jpg', 100, 200))
        self.db.cursor.execute("INSERT INTO Rating (userEmail, image_id, rating) VALUES (?, ?, ?)", ('test@example.com', 1, 3))
        self.db.conn.commit()

        # Update the rating
        editor = EditDatabase(self.test_db_path)  
        editor.update_rating(rating_id=1, new_rating=5)

        # Verify the update
        self.db.cursor.execute("SELECT rating FROM Rating WHERE rating_id = 1")
        result = self.db.cursor.fetchone()
        self.assertEqual(result[0], 5)
                
if __name__ == '__main__':
    unittest.main()