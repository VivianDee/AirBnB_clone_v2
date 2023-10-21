#!/usr/bin/python3
"""My Flask app"""
from flask import Flask, render_template
from markupsafe import escape
from models.__init__ import storage

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """Display the homepage"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_text(text=None):
    """Displays text from the URL"""
    text = text.replace('_', ' ')
    return 'C {}'.format(escape(text))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text="is_cool"):
    """Displays text from the URL"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(escape(text))


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n=0):
    """Displays number from the URL"""
    return '{} is a number'.format(escape(0))


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n=0):
    """Displays number from the URL"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_odd_or_even(n=0):
    """Displays content based on number from the URL"""
    return render_template("6-number_odd_or_even.html", n=n)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays content from my database"""
    all_objs = storage.all()

    objects = {}
    for obj_id, obj_data in all_objs.items():
        objects[obj_id] = obj_data
    return render_template("7-states_list.html", all_objs=objects.values())


@app.teardown_appcontext
def reload_db(error=None):
    """Closes the current database session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
