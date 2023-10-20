#!/usr/bin/python3
"""My Flask app"""
from flask import Flask, render_template
from markupsafe import escape

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


if __name__ == "__main__":
     app.run(host='0.0.0.0', port=5000, debug=True)
