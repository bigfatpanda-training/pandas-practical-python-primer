"""
This module provides functions that are commonly used by various
members of the api.py module.
"""

from werkzeug.exceptions import BadRequest


def json_payload(request):
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
        raise ValueError("JSON payload contains syntax errors. Please "
                         "fix and try again.")

    if request_payload is None:
        raise ValueError("No JSON payload present.  Make sure that "
                         "appropriate `content-type` header is "
                         "included in your request and that you've "
                         "specified a payload.")

    return request_payload


def verify_required_data_present(request_payload: dict, required_elements: set):
    """
    Verify that a request_payload has all the keys indicated
    in required_elements.

    Args:
        request_payload (dict): A set of request_payload to evaluate.
        required_elements (set): The names of keys that must be present
            in request_payload.

    Raises:
        ValueError: If any of the names in required_elements is not a
            member of request_payload.keys()
    """

    if not required_elements.issubset(request_payload.keys()):
        raise ValueError(
            "Missing required payload elements. "
            "The following elements are "
            "required: {}".format(required_elements))

