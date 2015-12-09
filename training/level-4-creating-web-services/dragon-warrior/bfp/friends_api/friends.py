from flask import Flask, jsonify, make_response, request, Response
from werkzeug.exceptions import BadRequest

from friends_api import datastore, api_helpers

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
    friend = datastore.existing_friend(id)
    if friend:
        return jsonify(friend)
    else:
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
        datastore.create_friend(request_payload)
    except BadRequest as error:
        response = make_response(
            jsonify(
                {"error": "JSON payload contains syntax errors. "
                          "Please fix and try again."}),
                400)
        return response
    except ValueError as error:
        response = make_response(
            jsonify({"error": str(error)}), 400)
        return response
    else:
        response = make_response(
            jsonify({"message": "Friend resource created."}), 201)
        return response


@app.route('/api/v1/friends/<id>', methods=['PUT'])
def fully_update_friend(id: str) -> Response:
    """
    Update all aspects of a specific friend or return an error.

    Use a JSON representation to fully update an existing friend
    resource.

    Args:
        id: The unique identifier of a friend resource.

    Returns:
        HTTP Response (200): If an existing resource is successfully updated.
        HTTP Response (400): No JSON payload, bad syntax, or missing data.
        HTTP Response (404): No matching existing resource to update.
    """
    try:
        request_payload = api_helpers.json_payload(request)
    except ValueError as error:
        response = make_response(
            jsonify({"error": str(error)}), 400)
        return response

    required_elements = {
        "id", "firstName", "lastName", "telephone", "email", "notes"}

    if not required_elements.issubset(request_payload.keys()):
        response = make_response(
                jsonify(
                    {"error": "Missing required payload elements. The "
                     "following are required: {}".format(
                        required_elements.difference(request_payload.keys()))}),
                400)
        return response

    friend = datastore.existing_friend(request_payload['id'])
    if friend:
        friend.update(
            {"id": request_payload['id'],
             "first_name": request_payload['firstName'],
             "last_name": request_payload['lastName'],
             "telephone": request_payload['telephone'],
             "email": request_payload['email'],
             "notes": request_payload['notes']
             })

        response = jsonify(
            {"message": "{} friend resource updated.".format(
                request_payload['id'])})
        return response
    else:
        response = make_response(
            jsonify(
                {"error": "No friend resource exists that matches "
                          "the given id: {}".format(request_payload['id'])}),
            404)
        return response


