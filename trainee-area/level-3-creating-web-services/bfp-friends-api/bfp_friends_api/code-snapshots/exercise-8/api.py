"""
Provides a Flask API to interact with Friendship data.
"""

from flask import Flask, jsonify, make_response, request

from bfp_friends_api import datastore
from bfp_friends_api import api_helpers

app = Flask(__name__)

FRIEND_RESOURCE_ELEMENTS = {"id", "firstName", "lastName",
                            "telephone", "email", "notes"}

"""
Operations for the Friends Resource Collection
"""
@app.route('/api/v1/friends', methods=['GET'])
def get_friends():
    """Return a representation of the collection of friend resources."""
    return jsonify({"friends": datastore.friends})


@app.route('/api/v1/friends', methods=['POST'])
def create_friend():
    """
    Create a new friend resource.

    Utilize a JSON representation in the request object to create
    a new friend resource.
    """

    try:
        json_payload = api_helpers.json_payload(request)
        api_helpers.verify_required_data_present(
            request_payload=json_payload,
            required_elements=FRIEND_RESOURCE_ELEMENTS)
    except ValueError as error:
        error_response = make_response(jsonify({"error": str(error)}), 400)
        return error_response

    if datastore.existing_friend(id=json_payload['id']):
        error_response = make_response(
            jsonify(
                {"error": "An friend resource already exists with the "
                          "given id: {}".format(json_payload['id'])}),
            400)
        return error_response


    datastore.friends.append(
        {"id": json_payload['id'],
         "first_name": json_payload['firstName'],
         "last_name": json_payload['lastName'],
         "telephone": json_payload['telephone'],
         "email": json_payload['email'],
         "notes": json_payload['notes']})

    response = make_response(jsonify({"message": "Friend resource created."}),
                             201)
    return response


"""
Operations for Individual Friend Resources
"""
@app.route('/api/v1/friends/<id>', methods=['GET'])
def get_friend(id: str):
    """Return a representation of a specific friend or an error."""

    try:
        return jsonify(datastore.existing_friend(id))
    except TypeError:
        error_response = make_response(
            jsonify({"error": "No such friend exists."}), 404)
        return error_response


@app.route('/api/v1/friends/<id>', methods=['PUT'])
def fully_update_friend(id: str):
    """
    Update all aspects of a specific friend or return an error.

    Use a JSON representation to fully update an existing friend
    resource.

    Returns
        HTTP Response (200): If an existing resource is successfully updated.
        HTTP Response (400): No JSON payload, bad syntax, or missing data.
        HTTP Response (404): No matching existing resource to update.
    """
    try:
        request_payload = api_helpers.json_payload(request)
        api_helpers.verify_required_data_present(
            request_payload, FRIEND_RESOURCE_ELEMENTS)
    except ValueError as error:
        error_response = make_response(jsonify({"error": str(error)}), 400)
        return error_response

    existing_friend = datastore.existing_friend(id)
    if existing_friend:
        existing_friend.update(
            {"id": request_payload['id'],
             "first_name": request_payload['firstName'],
             "last_name": request_payload['lastName'],
             "telephone": request_payload['telephone'],
             "email": request_payload['email'],
             "notes": request_payload['notes']})

        response = make_response(
            jsonify({"message": "Friend resource updated."}), 201)
        return response

    error_response = make_response(
        jsonify(
            {"error": "No friend resource exists that matches "
                      "the given id: {}".format(request_payload['id'])}),
        404)
    return error_response


@app.route('/api/v1/friends/<id>', methods=['DELETE'])
def destroy_friend(id: str):
    """
    Delete a specific friend resource or return an error.

    Returns
        HTTP Response (200): Friend resource deleted.
        HTTP Response (404): No matching existing resource to update.
    """
    try:
        existing_friend = datastore.existing_friend(id)
        datastore.friends.remove(existing_friend)
    except ValueError:
        error_response = make_response(
            jsonify({"error": "No such friend exists."}), 404)
        return error_response

    return jsonify({"message": "Friend resource removed."})
