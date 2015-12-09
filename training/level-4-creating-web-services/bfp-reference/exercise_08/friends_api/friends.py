from flask import Flask, jsonify, make_response, request, Response
from werkzeug.exceptions import BadRequest

from friends_api import datastore

app = Flask(__name__)


@app.route('/api/v1/friends', methods=['GET'])
def friends() -> Response:
    """
    Return a representation of the collection of friend resources.

    Returns:
        A flask.Response object.
    """
    return jsonify({"friends": datastore.friends})


@app.route('/api/v1/friends/<id>', methods=['GET'])
def specific_friend(id: str) -> Response:
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
        jsonify({"error": "You have no friends.  LOSER."}), 404)
    return error_response


@app.route('/api/v1/friends', methods=['POST'])
def create_friend() -> Response:
    """
    Create a new friend resource.

    Utilize a JSON representation/payload in the request object to
    create a new friend resource.

    Returns:
        A flask.Response object.
    """
    try:
        request_payload = request.get_json()
    except BadRequest as error:
        response = make_response(
            jsonify({"error": "JSON payload contains syntax errors. "
                              "Please fix and try again."}),
            400)
        return response

    try:
        datastore.create_friend(request_payload)
    except ValueError as error:
        response = make_response(
            jsonify({"error": str(error)}),
            400)
        return response

    response = make_response(
        jsonify({"message": "Friend resource created."}), 201)
    return response


@app.route('/api/v1/friends/<id>', methods=['PATCH'])
def update_friend(id: str) -> Response:
    """
    Update an existing friend resource.

    Utilize a JSON representation/payload in the request object to
    updated an existing friend resource.

    Args:
        id: The unique ID value of a given friend.

    Returns:
        A flask.Response object.
    """
    try:
        request_payload = request.get_json()
    except BadRequest as error:
        response = make_response(
            jsonify({"error": "JSON payload contains syntax errors. "
                              "Please fix and try again."}),
            400)
        return response

    try:
        datastore.update_friend(id, request_payload)
    except ValueError as error:
        response = make_response(
            jsonify({"error": str(error)}),
            400)
        return response

    response = make_response(
        jsonify({"message": "Friend resource updated."}), 201)
    return response