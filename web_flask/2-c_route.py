#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask
from markupsafe import escape
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''
    Index that displays hello HBNB for / route
    '''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''
    Index that displays HBNB for /hbnb route
    '''
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    '''
    Index that displays C followd by value of text for /c/<text> route
    '''
    return f'C {escape(text)}'.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
