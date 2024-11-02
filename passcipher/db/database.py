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
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    group_name TEXT NOT NULL
            );""",
            """CREATE TABLE IF NOT EXISTS accounts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
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

    def add_group(self, group):
        """
        Add new group tuple to the group table

        :param group: The group tuple containing the data
        :return: Return the Id of the newly added group
        """ 
        sql = ''' INSERT INTO groups(group_name)
                VALUES(?) '''
        try:
            self.cursor.execute(sql, group)
            self.conn.commit()

            # Return the id of new group
            group_id = self.cursor.lastrowid
            return group_id
        except sqlite3.Error as e:
            print(e)
            self.conn.rollback()
            return None
    
    def add_account(self, account):
        """
        Add new account tuple to the account table

        :param account: The account tuple containing the data
        :return: Return the Id of the newly added account
        """ 
        sql = ''' INSERT INTO accounts(account_name, username, url, cipher_location, notes, group_id)
                VALUES(?,?,?,?,?,?) '''
        try:
            self.cursor.execute(sql, account)
            self.conn.commit()

            # Return the id of new account
            account_id = self.cursor.lastrowid
            return account_id
        except sqlite3.Error as e:
            print(e)
            self.conn.rollback()
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
            self.conn.rollback()
            return None
        
    def update_account(self, account_details):
        """
        Update exisitng account entry in accounts table

        :param accountId: The id of the account to update
        :param account: A tuple containing the new data for the account
            (account_name, username, url, cipher_location, notes, groupId, accountId)
        :return: True if the update was successful, False otherwise
        """ 
        sql = ''' UPDATE accounts
                SET account_name = ?, 
                    username = ?, 
                    url = ?, 
                    cipher_location = ?, 
                    notes = ?,
                    group_id = ?
                WHERE id = ? '''
        try:
            # Execute the update statement with the account data and accountId
            self.cursor.execute(sql, account_details)
            self.conn.commit()

            # Check if account entry was updated
            if self.cursor.rowcount == 0:
                print("No account found with the given ID.")
                return False
            return True
        except sqlite3.Error as e:
            print(e)
            self.conn.rollback()
            return False
    
    def delete_group(self, group_id):
        """
        Delete a group by its ID and remove all associated accounts.

        :param group_id: The ID of the group to delete
        :return: True if the deletion was successful, False otherwise
        """
        try:
            # Delete the group itself
            delete_group_sql = "DELETE FROM groups WHERE id = ?"
            self.cursor.execute(delete_group_sql, (group_id,))
            
            self.conn.commit()
            
            # Check if group was deleted
            if self.cursor.rowcount == 0:
                print("No group found with the given ID.")
                return False
            return True
        except sqlite3.Error as e:
            print(e)
            self.conn.rollback()
            return False
        
    def delete_account(self, account_id):
        """
        Delete a account by its ID

        :param account_id: The ID of the account to delete
        :return: True if the deletion was successful, False otherwise
        """
        try:
            # First, delete associated accounts
            delete_accounts_sql = "DELETE FROM accounts WHERE id = ?"
            self.cursor.execute(delete_accounts_sql, (account_id,))
            
            self.conn.commit()
            
            # Check if group was deleted
            if self.cursor.rowcount == 0:
                print("No account found with the given ID.")
                return False
            return True
        except sqlite3.Error as e:
            print(e)
            self.conn.rollback()
            return False