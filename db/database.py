import sqlite3

class Database:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('testing.db')
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(e)

    def create_table(self):
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
            for statement in sql_statements:
                self.cursor.execute(statement)

            self.conn.commit()
        except sqlite3.Error as e:
            print(e)

    def close_connection(self):
        if self.conn:
            self.conn.close()

    def add_account(self, account):
        sql = ''' INSERT INTO accounts(id, account_name, username, url, cipher_location, notes, group_id)
                VALUES(?,?,?,?,?,?,?) '''
        try:
            self.cursor.execute(sql, account)
            self.conn.commit()

            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(e)
            return None