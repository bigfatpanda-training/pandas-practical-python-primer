"""
some module to do something class related
"""

from flask import Flask, jsonify, make_response, request
from friends_api import datastore

app = Flask(__name__)


@app.route('/api/v1/friends', methods=["GET"])
def friends():
    """
    Returns a representation of the collection of friend resources.

    Returns:
        A flask.Response object.
    """

    # DEP_01: Remove dependency on datastore
    return jsonify({
        "friends": datastore.friends
    })


@app.route('/api/v1/friends/<id>', methods=["GET"])
def specific_friend(id: str):
    """
    Return a representation of a specific friend resource.

    Args:
        id: The unique ID value of a given friend.

    Returns:
        A flask.Response object.
    """

    # DEP_01: Remove dependency on datastore
    for friend in datastore.friends:
        if friend['id'].lower() == id.lower():
            return  jsonify(friend)

    error_response = make_response(jsonify(
        {"error": "Friend ID '{friend}' not found.".format(friend=id)}), 404)
    return error_response


@app.route('/api/v1/friends', methods=["POST"])
def create_friend():
    """
    Create a new friend resource.

    Utilize a JSON  representation/payload in the request object to
    create a new friend resource.

    Returns:
        A flask.Response object.
    """
    payload = request.get_json()

    #DEP_01: Remove dependency on datastore
    datastore.friends.append({
            "id": payload["id"],
            "first_name": payload["firstName"],
            "last_name": payload["lastName"],
            "telephone": payload["telephone"],
            "email": payload["email"],
            "notes": payload["notes"],
        })

    response = make_response(
        jsonify({"message": "Friend resource created."}), 201
    )

    return response;