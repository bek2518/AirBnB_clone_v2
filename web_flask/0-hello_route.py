#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    '''
    Index that displays hello HBNB when / used
    '''
    return 'Hello HBNB!'
