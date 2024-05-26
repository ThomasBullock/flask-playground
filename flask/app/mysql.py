import mysql.connector
from flask import current_app, g
import time


class DB:
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.connection = None
        self.connect()
        
    def connect(self):
        attempts = 0
        max_attempts = 5
        while attempts < max_attempts:
            try:
                print("Attempting to connect to database...")
                self.connection = mysql.connector.connect(
                    user=self.user,
                    password=self.password,
                    host=self.host,
                    database=self.database
                )
                print("Connected to database successfully")
                return
            except mysql.connector.Error as e:
                attempts += 1
                print(f"Failed to connect to database (attempt {attempts}/{max_attempts}): {e}")
                time.sleep(5)
        raise Exception("Failed to connect to database after multiple attempts")

    def query(self, sql, args):
        if self.connection is None:
            raise Exception("Database connection is not established")
        cursor = self.connection.cursor()
        cursor.execute(sql, args)
        return cursor


# def get_db():
#     if 'db' not in g:
#         # Connect to the database
        # g.db = mysql.connector.connect(
        #     user='root',
        #     password='root', #current_app['DB_PASSWORD']
        #     host='db',
        #     database='sql_hr'
        # )

#         return g.db
    
# def close_db(e=None):
#     db = g.pop("db", None)

#     if db is not None:
#         # close the database 
#         db.close()

# def init_app(app):
#     app.teardown_appcontext(close_db)