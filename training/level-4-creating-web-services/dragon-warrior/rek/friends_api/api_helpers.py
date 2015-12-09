"""
This modules provides functions that are commonly used by various
members of the friends.py module.
"""
import flask
from werkzeug.exceptions import BadRequest


def json_payload(request: flask.request) -> dict:
    """

    Args:
        request:

    Returns:

    """
    try:
        request_payload = request.get_json()
    except BadRequest:
        raise ValueError("JSON payload contains syntax errors. Please fix and try again.")

    if request_payload is None:
        raise ValueError("No JSON payload present. Make sure that the appropriate `content-type` "
                         "header is included in your request.")

    return request_payload


def check_required_elements(request_payload: dict):
    required_data_elements = {
        "id", "firstName", "lastName", "telephone", "email", "notes"}

    if not required_data_elements.issubset(request_payload.keys()):
        raise ValueError("Missing required payload elements. "
                         "The following elements are "
                         "required: {}".format(required_data_elements))
        return False

    return True
