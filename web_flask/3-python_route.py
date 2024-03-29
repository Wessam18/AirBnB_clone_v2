#!/usr/bin/python3
"""Flask web Application"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    new_text = text.replace('_', ' ')
    return "C {}".format(new_text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    new_text = text.replace('_', ' ')
    return "Python {}".format(new_text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)