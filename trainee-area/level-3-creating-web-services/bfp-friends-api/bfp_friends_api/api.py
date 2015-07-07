"""
Provides a Flask API to interact with Friendship data.
"""

from flask import Flask, jsonify, abort

from bfp_friends_api.datastore import friends

app = Flask(__name__)


@app.route('/api/v1/friends', methods=['GET'])
def get_friends():
    return jsonify({"friends": friends})


@app.route('/api/v1/friends/<id>', methods=['GET'])
def get_friend(id):
    for friend in friends:
        if friend["id"] == id:
            return jsonify(friend)
    abort(404)

    return jsonify({"friends": friends})
