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
    import sys
    try:
        request_payload = request.get_json()

        if request_payload is None:
            response = make_response(
                jsonify(
                    {"error": "No JSON payload present.  Make sure that "
                     "appropriate `content-type` header is "
                     "included in your request."}),
                    400)
        else:
            datastore.friends.append(
                {"id": request_payload['id'],
                 "first_name": request_payload['firstName'],
                 "last_name": request_payload['lastName'],
                 "telephone": request_payload['telephone'],
                 "email": request_payload['email'],
                 "notes": request_payload['notes']
                 })

            response = make_response(
                jsonify({"message": "Friend resource created."}), 201)

    except BadRequest as error:
        response = make_response(
            jsonify(
                {"error": "JSON payload contains syntax errors. "
                          "Please fix and try again."}),
                400)
        return response

    except Exception as error:
        response = make_response(
            jsonify(
                {"errorType": str(sys.exc_info()[0]),
                 "errorMessage": str(sys.exc_info()[1]),
                 "errorLocation": sys.exc_info()[2].tb_lineno}),
                400)

    return response
