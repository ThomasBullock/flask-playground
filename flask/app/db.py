import mysql.connector
from flask import current_app, g

def get_db():
    print(current_app.config['DB_PASSWORD'])
    if 'db' not in g:
        # Connect to the database
        g.db = mysql.connector.connect(
            user='root',
            password='root',
            host='db',
            database='knights'
        )

        return g.db
    
def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        # close the database 
        db.close()