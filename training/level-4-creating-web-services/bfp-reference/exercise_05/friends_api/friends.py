from flask import Flask, jsonify, make_response

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


@app.route('/api/v1/friends/<id>', methods=['GET'])
def specific_friend(id: str):
    """
    Return a representation of a specific friend resource.

    Args:
        id: The unique ID value of a given friend.

    Returns:
        A flask.Response object.
    """
    for friend in datastore.friends:
        if friend['id'].lower() == id.lower():
            return jsonify(friend)

    error_response = make_response(
        jsonify(
            {"error": "No friend found with the specified identifier. "
                      "BFP is a Big Fat Panda Loser!"}), 404)

    return error_response
