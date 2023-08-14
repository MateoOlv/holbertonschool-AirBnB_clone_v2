#!/usr/bin/python3
"""
imports
"""
from flask import Flask, render_template

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


"""
python
"""


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    text = text.replace("_", " ")
    return (f"Python {text}")


"""
is int
"""


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return (f"{n} is a number")


"""
is int
"""


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


"""
is odd or even
"""


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_template(n):
    if n % 2:
        res = "is odd"
    else:
        res = "is even"
    return render_template('6-number_odd_or_even.html', n=n, res=res)


"""
Define the host and port that the web app is listening
"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
