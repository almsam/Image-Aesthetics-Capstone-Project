import sqlite3

class QueryDatabase:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def query_table(self, table_name, where_clause=None, where_params=None):
        """Queries a table with an optional WHERE clause.

        Args:
            table_name: The name of the table to query.
            where_clause: An optional WHERE clause string (e.g., "column = ?").
            where_params: A tuple of parameters for the WHERE clause.

        Returns:
            A list of tuples representing the query results.
        """
        query = f"SELECT * FROM {table_name}"
        if where_clause:
            query += f" WHERE {where_clause}"
        self.cursor.execute(query, where_params or ())
        return self.cursor.fetchall()

    def close(self):
        self.conn.close