#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    '''Displays HTML page with states'''
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    '''Removes SQL Alchemy session after each request'''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
