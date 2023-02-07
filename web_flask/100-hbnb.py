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


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''
    Display index website with state and amenities
    '''
    st = storage.all('State')
    am = storage.all('Amenity')
    pl = storage.all('Place')
    return render_template('100-hbnb.html', states=st, amenities=am, places=pl)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
