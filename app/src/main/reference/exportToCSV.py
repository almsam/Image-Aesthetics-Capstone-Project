import pandas as pd
import sqlite3
import os

class ExportToCSV:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)

    def export_table_to_csv(self, sql_query, csv_file_path):
        try:
            df = pd.read_sql_query(sql_query, self.conn)

            # Check if the DataFrame is empty
            if df.empty:
                print("Error: DataFrame is empty. No data to export.")
                return

            df.to_csv(csv_file_path, index=False)
            print(f"Data exported to '{csv_file_path}' successfully.")

        except (sqlite3.Error, IOError, pd.errors.EmptyDataError) as e:
            print(f"Error exporting data: {e}")

            # Check if the file exists and is empty
            if os.path.exists(csv_file_path):
                if os.path.getsize(csv_file_path) == 0:
                    print("CSV file is empty.")
                else:
                    print("CSV file exists but may be corrupted.")

    def close(self):
        self.conn.close()