"""
This module provides functions that are commonly used by various
members of the friends.py module.
"""
import flask
from werkzeug.exceptions import BadRequest


def json_payload(request: flask.request) -> dict:
    """
    Verify that a flask.request object has a JSON payload and
    that it does not contain syntax errors.

    Args:
        request (flask.request): A request object that you want to
            verify has a valid JSON payload.

    Raises:
        ValueError: If the incoming request object is either missing
            a JSON payload or has one with syntax errors.
    """
    try:
        request_payload = request.get_json()
    except BadRequest:
        raise ValueError(
            "JSON payload contains syntax errors. Please fix and try again.")

    if request_payload is None:
        raise ValueError(
            "No JSON payload present. Make sure that "
            "the appropriate `content-type` header is included "
            "in your request.")
