#!/usr/bin/python3
"""a script to run a flask web application """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ function is  called with / route"""
    return "Hello HBNB!"


if __name__ == "__main__":
    """ main function to start the application """
    app.run(host='0.0.0.0', port=5000)
