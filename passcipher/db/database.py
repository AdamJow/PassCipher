import os
import sqlite3

class Database:
    def __init__(self):
        """
        Initialise the Database class by setting up a connection to the SQLite database.

        :param self: The instance of the class
        """
        # Get the directory of the current file (passcipher folder)
        current_dir = os.path.dirname(__file__)
        
        # Navigate to the top level data folder
        project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
        data_dir = os.path.join(project_root, "data", "db")
        
        # Ensure the directory exists
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        # Specify the database file path
        db_path = os.path.join(data_dir, 'testing.db')
        
        try:
            # Connect to the newly created db file
            self.conn = sqlite3.connect(db_path)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(e)

    def create_table(self):
        """
        Creates the necessary tables for the application.

        :param self: The instance of the class
        """
        sql_statements = [ 
            """CREATE TABLE IF NOT EXISTS groups (
                    id INTEGER PRIMARY KEY NOT NULL, 
                    group_name TEXT NOT NULL
            );""",
            """CREATE TABLE IF NOT EXISTS accounts (
                    id INTEGER PRIMARY KEY NOT NULL, 
                    account_name TEXT NOT NULL, 
                    username TEXT NOT NULL, 
                    url TEXT, 
                    cipher_location TEXT NOT NULL,
                    notes TEXT,
                    group_id INTEGER NOT NULL,
                    FOREIGN KEY (group_id) REFERENCES groups (id)
            );"""]
        try:
            # Create the tables
            for statement in sql_statements:
                self.cursor.execute(statement)

            self.conn.commit()
        except sqlite3.Error as e:
            print(e)

    def close_connection(self):
        """
        Closes the connection to the SQLite database.

        :param self: The instance of the class
        """
        if self.conn:
            self.conn.close()

    def add_account(self, account):
        """
        Add new account tuple to the account table

        :param account: The account tuple containing the data
        :return: Return the Id of the newly added account
        """ 
        sql = ''' INSERT INTO accounts(id, account_name, username, url, cipher_location, notes, group_id)
                VALUES(?,?,?,?,?,?,?) '''
        try:
            self.cursor.execute(sql, account)
            self.conn.commit()

            # Return the id of the last row
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(e)
            return None
        
    def get_data(self, table, filters=None):
        """
        Fetch data from a specified table with optional filters.

        :param table: Table name to fetch data from (e.g., 'accounts', 'groups')
        :param filters: Specify key and value pairs to filter results (e.g., {'account_name': 'example'})
        :return: List of rows fetched from the table
        """
        try:
            # Base SQL query
            query = f"SELECT * FROM {table} as T "
            
            # If filters are provided, build the WHERE clause
            if filters:
                query += "WHERE "
                filter_conditions = []

                for index, key in enumerate(filters.keys()):
                    if index == 0:
                        # First condition
                        filter_conditions.append(f"T.{key} = ?")
                    else:
                        # Subsequent conditions
                        filter_conditions.append(f"AND T.{key} = ?")

                # Join all filter conditions togethor and add to the base query
                query += " ".join(filter_conditions)
            
            # Execute the query with filter values if filters exist
            if filters:
                self.cursor.execute(query, tuple(filters.values()))
            else:
                self.cursor.execute(query)

            # Fetch and return all rows
            rows = self.cursor.fetchall()
            return rows

        except sqlite3.Error as e:
            print(e)
            return None