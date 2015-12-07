from flask import Flask, jsonify, make_response, request

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
    request_payload = request.get_json()

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
    return response