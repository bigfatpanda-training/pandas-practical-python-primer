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


def github_user_info(username: str) -> requests.Response:
    """
    Obtain information about a given user in Github.

    Args
        username: A str specifying a valid Github username.

    Returns
        A requests.Response object.
    """
    github_api_info = github_entry_point().json()
    url = github_api_info['user_url'].format(user=username)
    response = requests.get(url)
    return response


def github_user_repos(username: str) -> requests.Response:
    """
    Obtain information about a given user's repositories in Github.

    Args
        username: A str specifying a valid Github username.

    Returns
        A requests.Response object.
    """
    github_api_info = github_entry_point().json()
    url = github_api_info['user_url'].format(user=username) + "/repos"
    response = requests.get(url)
    return response


def github_repo_issues(username: str, repo_name: str) -> requests.Response:
    """
    Obtain information about a given repositories issues in Github.

    Args
        username: A str specifying a valid Github username.
        repo_name: A str specifying a Github repo that belongs to the
            specified user.

    Returns
        A requests.Response object.
    """
    github_api_info = github_entry_point().json()
    url = (
        github_api_info['repository_url'].format(
            owner=username, repo=repo_name) + "/issues")
    print(url)
    response = requests.get(url)
    return response


class Github:
    """
    Provides access to the Github API.

    Class Attributes:
        urls: Github API url templates for accessing various functionality.

    Attributes:
        oauth_token: A valid OAuth oauth_token for access the API.

    Methods:
        user_info: Provide information on a given Github user.
        user_repos: Provide information on a given users repositories.
        repo_issues: Provide information on a given repo's issues.
    """
    urls = requests.get("https://api.github.com").json()

    def __init__(self, oauth_token: str):
        self.oauth_token = oauth_token


if __name__ == "__main__":
    github_1 = Github(oauth_token='pretend token 1')
    github_2 = Github(oauth_token='pretend token 2')

