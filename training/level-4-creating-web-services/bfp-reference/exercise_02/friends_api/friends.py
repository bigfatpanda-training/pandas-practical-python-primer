from flask import Flask, jsonify

from friends_api import datastore

app = Flask(__name__)