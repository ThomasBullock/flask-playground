import json
from flask import Blueprint, render_template

from typing import List, Dict
from .db import get_db

routing = Blueprint("routing", __name__)

@routing.route('/')
def index() -> str:
    return json.dumps({'favorite_colors': favorite_colors()})


@routing.route('/admin')
def admin():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)


def favorite_colors() -> List[Dict]:
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM favorite_colors')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    # connection.close()

    return results