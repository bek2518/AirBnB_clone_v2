#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    '''
    Removes current SQLAlchemy session after each request
    '''
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    '''
    Displays HTML page of states sorted by name
    '''
    states = storage.all('State')
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    '''
    Displays HTML page of states sorted by name
    '''
    states = storage.all('State')
    state_id = 'State.' + id
    return render_template('9-states.html', states=states, state_id=state_id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
