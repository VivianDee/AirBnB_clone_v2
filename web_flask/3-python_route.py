#!/usr/bin/python3
"""My Flask app"""
from flask import Flask
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

if __name__ == "__main__":
     app.run(host='0.0.0.0', port=5000, debug=True)
