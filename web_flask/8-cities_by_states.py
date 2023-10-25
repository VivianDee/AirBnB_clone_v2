#!/usr/bin/python3
"""My Flask app"""
from flask import Flask, render_template
from markupsafe import escape
from models.__init__ import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def reload_db(error=None):
    """Closes the current database session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays content from my database"""
    all_objs = storage.all(State).values()
    all_objs = sorted(all_objs, key=lambda state: state.name)

    return render_template("7-states_list.html", all_objs=all_objs)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays content from my database"""
    all_objs = storage.all(State).values()
    all_objs = sorted(all_objs, key=lambda state: state.name)

    return render_template("8-cities_by_states.html", all_objs=all_objs)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
