#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template
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
    Index that displays C followed by value of text for /c/<text> route
    '''
    return 'C %s' % escape(text).replace('_', ' ')


@app.route('/python')
@app.route('/python/<text>')
def python_text(text='is cool'):
    '''
    Index that displays Python followed by value of text for
    /python/<text> route
    '''
    return 'Python %s' % escape(text).replace('_', ' ')


@app.route('/number/<int:n>')
def number(n):
    '''
    Index that display n is a number only if n is an integer
    '''
    return '%d is a number' % n


@app.route('/number_template/<int:n>')
def number_template(n):
    '''
    Index that display n is a number only if n is an integer
    '''
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
