#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes=False


@app.route('/')
def index():
    '''
    Index that displays hello HBNB when / used
    '''
    return 'Hello HBNB!'
