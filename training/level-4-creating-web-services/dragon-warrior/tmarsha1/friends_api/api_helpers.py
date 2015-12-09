"""
This module provides functions that are commonly used by verious
members of the friends.py module
"""

import flask
from werkzeug.exceptions import BadRequest


def json_payload(request: flask.request) -> dict:
    """
    Verify that a payload exists and no syntax errors
    Args:
        request:

    Returns:

    Raises:
       ValueError:
    """
    try:
        request_payload = request.get_json()
    except BadRequest:
        raise ValueError("JSON payload contains syntax errors.")

    if request_payload is None:
        raise ValueError("No JSON payload present. Make sure that "
                         "'application/json' content-type header is included "
                         "in your request.")

    return request_payload


def required_elements_exist(payload: dict):
    """

    Args:
        payload:

    Raises:
        ValueError:
    """
    required_elements = {"id", "firstName", "lastName", "telephone",
                     "email", "notes"}

    if not required_elements.issubset(payload.keys()):
        raise ValueError("Missing required payload elements. The "
                 "following are required: {}".format(
                    required_elements.difference(payload.keys()))
        )
