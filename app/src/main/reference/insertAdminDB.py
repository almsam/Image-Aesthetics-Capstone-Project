import sqlite3

class DatabaseInserter:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS admin (
                adminEmail TEXT NOT NULL UNIQUE PRIMARY KEY,
                adminUsername TEXT NOT NULL,
                adminPassword TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def insert_record(self, email, username, password):
        self.cursor.execute('''
            INSERT INTO admin (adminEmail, adminUsername, adminPassword)
            VALUES (?, ?, ?)
        ''', (email, username, password))
        self.connection.commit()

    def close(self):
        self.connection.close()

# Example usage:
# db_inserter = DatabaseInserter('path_to_your_database.db')
# db_inserter.insert_record('adminEmail', 'adminUsername', 'adminPassword')
# db_inserter.close()