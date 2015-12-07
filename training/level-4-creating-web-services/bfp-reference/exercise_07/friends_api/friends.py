from flask import Flask, jsonify, make_response, request
from werkzeug.exceptions import BadRequest

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
        jsonify({"error": "You have no friends.  LOSER."}), 404)
    return error_response


@app.route('/api/v1/friends', methods=['POST'])
def create_friend():
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
            jsonify(
                {"error": "JSON payload contains syntax errors. "
                          "Please fix and try again."}),
                400)
        return response

    if not request_payload:
        response = make_response(
            jsonify(
                {"error": "No JSON payload present.  Make sure that "
                 "appropriate `content-type` header is "
                 "included in your request."}),
                400)
        return response

    missing_json_elements = set(datastore.friends[0].keys()).difference(
        request_payload.keys())

    if missing_json_elements:
        response = make_response(
            jsonify(
                {"error": "Missing required payload elements. "
                          "The following elements are "
                          "required: {}".format(
                    missing_json_elements.difference(request_payload.keys()))}),
            404)
        return response

    for potential_duplicate in datastore.friends:
        if request_payload['id'].lower() == potential_duplicate['id'].lower():
            response = make_response(
                jsonify(
                    {"error": "An friend resource already exists with the "
                              "given id: {}".format(request_payload['id'])}),
                400)
            return response

    response = make_response(
        jsonify({"message": "Friend resource created."}), 201)
    return response