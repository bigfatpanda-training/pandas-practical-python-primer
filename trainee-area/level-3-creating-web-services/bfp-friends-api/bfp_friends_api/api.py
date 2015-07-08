"""
Provides a Flask API to interact with Friendship data.
"""

from flask import Flask, jsonify, make_response, request
from werkzeug.exceptions import BadRequest

from bfp_friends_api import datastore

app = Flask(__name__)


@app.route('/api/v1/friends', methods=['GET'])
def get_friends():
    """Return a representation of the collection of friend resources."""
    return jsonify({"friends": datastore.friends})


@app.route('/api/v1/friends/<id>', methods=['GET'])
def get_friend(id: str):
    """Return a representation of a specific friend or an error."""
    for friend in datastore.friends:
        if friend["id"].lower() == id.lower():
            return jsonify(friend)

    error_response = make_response(
        jsonify({"error": "No such friend exists."}), 404)
    return error_response


@app.route('/api/v1/friends', methods=['POST'])
def create_friend():
    """
    Create a new friend resource.

    Utilize a JSON representation in the request object to create
    a new friend resource.
    """

    try:
        import sys
        required_data_elements = {
            "id", "firstName", "lastName", "telephone", "email", "notes"}
        try:
            request_payload = request.get_json()
        except BadRequest:
            error_response = make_response(
                jsonify({"error": "JSON payload contains syntax errors. Please "
                                  "fix and try again."}),
                400)
            return error_response

        if request_payload is None:
            error_response = make_response(
                jsonify({"error": "No JSON payload present.  Make sure that "
                                  "appropriate `content-type` header is "
                                  "included in your request."}),
                400)
            return error_response

        # if not required_data_elements.issubset(request_payload.keys()):
        #     error_response = make_response(
        #         jsonify(
        #             {"error": "Missing required payload elements. "
        #                       "The following elements are "
        #                       "required: {}".format(required_data_elements)}),
        #         404)
        #     return error_response

        datastore.friends.append(
            {"id": request_payload['id'],
             "first_name": request_payload['firstName'],
             "last_name": request_payload['lastName'],
             "telephone": request_payload['telephone'],
             "email": request_payload['email'],
             "notes": request_payload['notes']})

        response = make_response(jsonify({"message": "Friend resource created."}),
                                 201)
    except Exception as error:
        response = make_response(
            jsonify({"errorType": str(sys.exc_info()[0]),
                     "errorMessage": str(sys.exc_info()[1]),
                     "errorLocation": sys.exc_info()[2].tb_lineno}),
            400)

    return response
