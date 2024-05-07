from typing import List, Dict
import mysql.connector
import json
from flask import Flask, render_template
from config import Config
from .db import get_db

app = Flask(__name__)
app.config.from_object(Config)


def favorite_colors() -> List[Dict]:
    # config = {
    #     'user': 'root',
    #     'password': 'root',
    #     'host': 'db',
    #     'port': '3306',
    #     'database': 'knights'
    # }
    # connection = mysql.connector.connect(**config)
    # cursor = connection.cursor()
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM favorite_colors')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    # connection.close()

    return results


@app.route('/')
def index() -> str:
    return json.dumps({'favorite_colors': favorite_colors()})


@app.route('/admin')
def admin():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)