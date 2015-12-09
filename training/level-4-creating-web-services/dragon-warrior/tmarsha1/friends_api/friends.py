"""
some module to do something class related
"""

from flask import Flask, jsonify, make_response, request, Response
from friends_api import datastore, api_helpers
from werkzeug.exceptions import BadRequest

app = Flask(__name__)


@app.route('/api/v1/friends', methods=["GET"])
def friends() -> Response:
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
def specific_friend(id: str) -> Response:
    """
    Return a representation of a specific friend resource.

    Args:
        id: The unique ID value of a given friend.

    Returns:
        A flask.Response object.
    """

    # DEP_01: Remove dependency on datastore
    friend = datastore.existing_friend(id)
    if friend:
        return  jsonify(friend)
    else:
        error_response = make_response(jsonify(
            {"error": "Friend ID '{friend}' not found.".format(friend=id)}), 404)
        return error_response


@app.route('/api/v1/friends', methods=["POST"])
def create_friend() -> Response:
    """
    Create a new friend resource.

    Utilize a JSON  representation/payload in the request object to
    create a new friend resource.

    Returns:
        A flask.Response object.
    """

    #DEP_01: Remove dependency on datastore
    try:
        payload = api_helpers.json_payload(request)
        api_helpers.required_elements_exist(payload)
    except ValueError as error:
        error_response = make_response(jsonify({"error": str(error)}), 400)
        return error_response

    if datastore.existing_friend(payload['id']):
        response = make_response(
            jsonify(
                {"error": "The specified friend resource already exists."}), 400
            )
    else:
        datastore.friends.append({
                "id": payload["id"],
                "first_name": payload["firstName"],
                "last_name": payload["lastName"],
                "telephone": payload["telephone"],
                "email": payload["email"],
                "notes": payload["notes"],
            })

        response = make_response(
            jsonify({"message": "Friend resource created."}), 201)

    return response

@app.route('/api/v1/friends/<id>', methods=["PUT"])
def update_friend(id: str) -> Response:
    """
    Update all aspects of a Friend resource.

    Use a JSON representation to fully update an existing friend resource.
    Args:
        id: The unique identifier of a Friend resouce

    Returns:
        A flask.Response object.
    """
    try:
        payload = api_helpers.json_payload(request)
        api_helpers.required_elements_exist(payload)
    except ValueError as error:
        error_response = make_response(jsonify({"error": str(error)}), 400)
        return error_response

    friend = datastore.existing_friend(payload['id'])
    if friend:
        friend.update({
                "id": payload["id"],
                "first_name": payload["firstName"],
                "last_name": payload["lastName"],
                "telephone": payload["telephone"],
                "email": payload["email"],
                "notes": payload["notes"],
            })

        response = make_response(
            jsonify({"message": "Friend resource {} updated.".format(
                payload['id'])}))
        return response
    else:
        response = make_response(
            jsonify({"error": "Friend resource {} not found.".format(
                payload['id'])}), 404)
        return response
