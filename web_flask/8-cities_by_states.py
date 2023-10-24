#!/usr/bin/python3
"""My Flask app"""
from flask import Flask, render_template
from markupsafe import escape
from models.__init__ import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays content from my database"""
    all_objs = storage.all(State).values()

    return render_template("7-states_list.html", all_objs=all_objs)


@app.teardown_appcontext
def reload_db(error=None):
    """Closes the current database session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
