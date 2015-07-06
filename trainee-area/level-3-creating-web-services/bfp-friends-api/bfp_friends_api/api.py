"""
Provides a Flask API to interact with Friendship data.
"""

from flask import Flask

from bfp_friends_api.datastore import friends

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)