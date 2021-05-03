#!/usr/bin/python3
'''Working with Flask Module'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Function hello"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """Function HBNB"""
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
