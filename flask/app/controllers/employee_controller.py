from flask import request, Blueprint, current_app, render_template

routing = Blueprint("routing", __name__)

@routing.route('/admin')
def admin():
    print('>>>>>> admin')
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)


@routing.route('/')
def index() -> str:
    # Access the database instance via current_app.db
    db = current_app.db
    cursor = db.query('SELECT * FROM employees', ())
    # TODO convert results to a list of dictionaries

    # Fetch the results
    results = cursor.fetchall()

    # Iterate over the results and print each row
    for row in results:
        print(row)
    return render_template('index.html', title='Home', user=results)
