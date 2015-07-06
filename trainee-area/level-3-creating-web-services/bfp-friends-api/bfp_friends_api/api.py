"""
Provides a Flask API to interact with Friendship data.
"""

from flask import Flask, jsonify

from bfp_friends_api.datastore import friends

app = Flask(__name__)


@app.route('/api/v1/friends', methods=['GET'])
def get_friends():
    return jsonify({"friends": friends})
