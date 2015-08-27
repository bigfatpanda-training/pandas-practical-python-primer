"""
Provides a Flask API to interact with Friendship data.
"""
import sqlite3

from flask import Flask, jsonify, make_response, request, g

from trainee_friends_api import datastore
from trainee_friends_api import api_helpers
from trainee_friends_api import auth

app = Flask(__name__)

FRIEND_RESOURCE_ELEMENTS = {"id", "firstName", "lastName",
                            "telephone", "email", "notes"}


@app.before_request
def connect_to_database():
    """nice docstring"""
    g.datastore = sqlite3.connect("/tmp/friends.db")


@app.teardown_request
def disconnect_from_database(exception):
    """nice docstring"""
    g.datastore.close()


"""
Operations for the Friends Resource Collection
"""
@app.route('/api/v1/friends', methods=['GET'])
@auth.requires_auth
def get_friends():
    """Return a representation of the collection of friend resources."""
    friends = datastore.get_friends(g.datastore)
    return jsonify({"friends": friends})


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

    if datastore.get_friend(g.datastore, json_payload['id']):
        error_response = make_response(
            jsonify(
                {"error": "An friend resource already exists with the "
                          "given id: {}".format(json_payload['id'])}),
            400)
        return error_response

    datastore.add_friend(g.datastore, json_payload)
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
        return jsonify(
            datastore.get_friend(g.datastore, id))
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

    existing_friend = datastore.get_friend(g.datastore, id)
    if existing_friend:
        datastore.fully_update_friend(g.datastore, request_payload)
        response = make_response(
            jsonify({"message": "Friend resource updated."}), 201)
        return response

    error_response = make_response(
        jsonify(
            {"error": "No friend resource exists that matches "
                      "the given id: {}".format(id)}),
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
        datastore.delete_friend(g.datastore, id)
    except ValueError:
        error_response = make_response(
            jsonify({"error": "No such friend exists."}), 404)
        return error_response

    return jsonify({"message": "Friend resource removed."})
