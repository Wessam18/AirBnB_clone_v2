#!/usr/bin/python3
""" Start a web application """

from flask import Flask


web_app = Flask(__name__)


@web_app.route("/", strict_slashes=False)
def Home():
    return "Hello HBNB!"


@web_app.route("/hbnb", strict_slashes=False)
def prompt():
    return "HBNB"


@web_app.route("/c/<text>", strict_slashes=False)
def language(text):
    new = text.replace('_', ' ')
    return f"C {new}"


@web_app.route("/python", strict_slashes=False)
@web_app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    new = text.replace('_', ' ')
    return f"Python {new}"


@web_app.route("/number/<n>", strict_slashes=False)
def integer(n):
    try:
        n = int(n)
        return f"{n} is a number"
    except ValueError:
        pass


if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=5000)
