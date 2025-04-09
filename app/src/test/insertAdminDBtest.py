import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main')))
from reference.insertAdminDB import DatabaseInserter

class TestDatabaseInserter(unittest.TestCase):
    def setUp(self):
        self.test_db_path = 'test_database.db'
        self.db_inserter = DatabaseInserter(self.test_db_path)

    def tearDown(self):
        self.db_inserter.close()
        os.remove(self.test_db_path)

    def test_create_table(self):
        self.db_inserter.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='admin'")
        table = self.db_inserter.cursor.fetchone()
        self.assertIsNotNone(table)

    def test_insert_record(self):
        self.db_inserter.insert_record('testEmail', 'testUser', 'testPassword')
        self.db_inserter.cursor.execute("SELECT * FROM admin WHERE adminUsername='testUser'")
        record = self.db_inserter.cursor.fetchone()
        self.assertIsNotNone(record)
        self.assertEqual(record[0], 'testEmail')
        self.assertEqual(record[1], 'testUser')
        self.assertEqual(record[2], 'testPassword')

if __name__ == '__main__':
    unittest.main()