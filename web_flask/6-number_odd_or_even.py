#!/usr/bin/python3
'''Working with Flask Module'''
from flask import Flask, escape, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Function hello"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """Function HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Function c, with variable text"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Function python, with variable text by default is cool"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Only if n is int"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>/', strict_slashes=False)
def is_a_number_template(n):
    """
    Template html
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>/', strict_slashes=False)
def number_odd_or_even(n):
    """
    Template html | odd or even
    """
    return render_template('6-number_odd_or_even.html', number=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
