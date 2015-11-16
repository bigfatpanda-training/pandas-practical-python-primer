"""
This module interacts with the Github API to demonstrate
interaction with RESTful web services.
"""

import requests

from configuration_panda import ConfigurationPanda

credentials = ConfigurationPanda(['PROGRAM_CREDENTIALS'])


def github_entry_point() -> requests.Response:
    """
    HTTP GET `https://api.github.com`

    Obtain information about the Github API from its entry point.
    """
    url = "https://api.github.com"
    response = requests.get(url)
    return response


if __name__ == "__main__":
    import pprint
    github_info = github_entry_point()
    print(github_info.status_code)
    pprint.pprint(dict(github_info.headers))
    pprint.pprint(github_info.json())
