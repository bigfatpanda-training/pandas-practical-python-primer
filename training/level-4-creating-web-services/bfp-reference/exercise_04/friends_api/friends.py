from flask import Flask, jsonify

from friends_api import datastore

app = Flask(__name__)


@app.route('/api/v1/friends', methods=['GET'])
def friends():
    """
    Return a representation of the collection of friend resources.

    Returns:
        A flask.Response object.
    """
    return jsonify({"friends": datastore.friends})