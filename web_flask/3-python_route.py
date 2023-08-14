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


"""
HBNB
"""


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    return ("HBNB")


"""
C is fun
"""


@app.route("/c/<text>", strict_slashes=False)
def C(text):
    newtext = text.replace("_", " ")
    return (f"C {newtext}")


@app.route("/python/<text>", strict_slashes=False)
def Python(text):
    newtext = text.replace("_", " ")
    return (f"Python {newtext}")


"""
Define the host and port that the web app is listening
"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
