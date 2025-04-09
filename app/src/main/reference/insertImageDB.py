import sqlite3

class DatabaseInserter:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS images (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                img_path TEXT NOT NULL,
                rating INTEGER NOT NULL,
                userID INTEGER NOT NULL
            )
        ''')
        self.connection.commit()

    def insert_record(self, img_path, rating, userID):
        self.cursor.execute('''
            INSERT INTO images (img_path, rating, userID)
            VALUES (?, ?, ?)
        ''', (img_path, rating, userID))
        self.connection.commit()

    def close(self):
        self.connection.close()

# Example usage:
# db_inserter = DatabaseInserter('path_to_your_database.db')
# db_inserter.insert_record('path/to/image.jpg', 5, 123)
# db_inserter.close()