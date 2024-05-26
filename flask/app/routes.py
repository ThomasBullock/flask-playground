import json
from flask import Blueprint, render_template

from typing import List, Dict
# from .db import get_db
from .. import db, flask_bcrypt

routing = Blueprint("routing", __name__)

@routing.route('/')
def index() -> str:
    return json.dumps({'favortite_colours': favorite_colors()})


@routing.route('/admin')
def admin():
    print('>>>>>> admin')
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)


def favorite_colors() -> List[Dict]:
    db = get_db()
    cursor = db.cursor(dictionary=True, buffered=True)
    cursor.execute('SHOW TABLES')
    # results = [{first_name: last_name} for (first_name, last_name) in cursor.item()]
    cursor.close()
    # connection.close()

    return #results