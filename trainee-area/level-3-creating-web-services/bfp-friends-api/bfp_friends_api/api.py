"""
Provides a Flask API to interact with Friendship data.
"""

from flask import Flask, jsonify, make_response

from bfp_friends_api.datastore import friends

app = Flask(__name__)


@app.route('/api/v1/friends', methods=['GET'])
def get_friends():
    """Return a representation of the collection of friend resources."""
    return jsonify({"friends": friends})


@app.route('/api/v1/friends/<id>', methods=['GET'])
def get_friend(id: str):
    """Return a representation of a specific friend or an error."""
    for friend in friends:
        if friend["id"].lower() == id.lower():
            return jsonify(friend)

    error_response = make_response(
        jsonify({"error": "No such friend exists."}), 404)
    return error_response

