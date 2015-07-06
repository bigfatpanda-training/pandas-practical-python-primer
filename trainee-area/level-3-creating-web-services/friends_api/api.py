"""
Provides a Flask API to interact with Friendship data.
"""

from flask import Flask

from friends_api import datastore

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)