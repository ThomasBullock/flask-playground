from flask import Flask, jsonify
import mysql.connector
import time

app = Flask(__name__)

# Configure MySQL connection
# app.config['MYSQL_HOST'] = 'localhost' # 'mysql_db' # Use the service name 'mysql' instead of 'localhost'
# app.config['MYSQL_USER'] = 'root'  # Change this to your MySQL username
# app.config['MYSQL_PASSWORD'] = 'password' # 'easy123'  # Change this to your MySQL password
# app.config['MYSQL_DB'] = 'mydatabase'  # Change this to your MySQL database name


# Initialize MySQL connection
# mysql = mysql.connector.connect(
#     host=app.config['MYSQL_HOST'],
#     user=app.config['MYSQL_USER'],
#     password=app.config['MYSQL_PASSWORD'],
#     database=app.config['MYSQL_DB']
# )

# def connect_to_mysql():
#     attempts = 0
#     while attempts < 5:
#         try:
#             db = mysql.connector.connect(
#             host=app.config['MYSQL_HOST'],
#             user=app.config['MYSQL_USER'],
#             password=app.config['MYSQL_PASSWORD'],
#             database=app.config['MYSQL_DB']
#             )
#             return db
#         except mysql.connector.Error as err:
#             print(f"Error connecting to MySQL: {err}")
#             attempts += 1
#             time.sleep(3)  # Wait for 2 seconds before retrying
#     raise Exception("Failed to connect to MySQL after multiple attempts")

# db_connection = connect_to_mysql()

cnx = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='mydatabase')
cnx.close()

@app.route("/", methods=["GET"])
def home():
    return "Api running you cunt@@!"

@app.route("/hello", methods=["GET"])
def say_hello():
    return jsonify({"msg": "Hello from Flask"})

# Define a route to test the database connection
@app.route('/db')
def index():
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM pet")
    data = cursor.fetchall()
    cursor.close()
    return str(data)


if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=5000, debug=True)