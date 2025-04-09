import sqlite3

class DeleteFromDatabase:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def delete_item(self, table_name, where_clause, where_params):
        """Deletes items from a specified table based on a WHERE clause.

        Args:
            table_name: The name of the table to delete from.
            where_clause: The WHERE clause to specify the deletion criteria.
            where_params: A tuple of parameters for the WHERE clause.
        """
        try:
            delete_statement = f"DELETE FROM {table_name} WHERE {where_clause}"
            self.cursor.execute(delete_statement, where_params)
            self.conn.commit()
            print(f"Item(s) deleted successfully from {table_name}.")
        except sqlite3.Error as e:
            print(f"Error deleting item(s): {e}")

    def close(self):
        self.conn.close() 