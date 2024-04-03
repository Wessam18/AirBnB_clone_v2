#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from operator import attrgetter


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db():
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page with the states listed in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=attrgetter('name'))
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
