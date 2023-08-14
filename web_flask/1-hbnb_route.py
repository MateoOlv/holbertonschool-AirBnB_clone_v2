#!/usr/bin/python3
"""
imports
"""
from flask import Flask


app = Flask(__name__)
"""
Routes
"""


@app.route("/", strict_slashes=False)
def index():
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def index():
    return ("HBNB")


"""
Define the host and port that the web app is listening
"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
