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


@app.route('/filters', strict_slashes=False)
def filters():
	'''
	Display index website with state and amenities
	'''
	states = storage.all('State')
	amenities = storage.all('Amenity')
	return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
