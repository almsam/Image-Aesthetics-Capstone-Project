import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import sqlite3
import os
import sys

# Add the src/main directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main')))
from reference.exportToCSV import ExportToCSV

class TestExportToCSV(unittest.TestCase):

    @patch('sqlite3.connect')
    def test_export_to_csv(self, mock_connect):
        mock_conn = mock_connect.return_value
        mock_cursor = mock_conn.cursor.return_value

        # Mock cursor to return rows as tuples
        mock_cursor.execute.return_value = None  # May not be necessary
        mock_cursor.fetchall.return_value = [
            (1, 'Alice'),
            (2, 'Bob')
        ]
        # Mock cursor description to provide column names
        mock_cursor.description = [('id', None), ('name', None)]

        df_expected = pd.DataFrame({'id': [1, 2], 'name': ['Alice', 'Bob']})

        exporter = ExportToCSV(':memory:')
        exporter.export_table_to_csv('SELECT * FROM test_table', 'test.csv')

        # Assertions:
        mock_connect.assert_called_once_with(':memory:')
        mock_cursor.execute.assert_called_once_with('SELECT * FROM test_table')
        mock_cursor.fetchall.assert_called_once()

        # Check if DataFrames are equal
        is_equal = pd.read_csv('test.csv').equals(df_expected)

        # Assert on the boolean value
        self.assertTrue(is_equal)  # Use `self.assertTrue` from the `unittest` module

        # Clean up the test file
        os.remove('test.csv')   # Comment this line to keep the file, created in root directory

if __name__ == '__main__':
    unittest.main()