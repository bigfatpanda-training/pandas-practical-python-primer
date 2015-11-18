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


if __name__ == "__main__":
    import pprint
    user_info = github_user_info('bigfatpanda-training')
    user_repos = github_user_repos('bigfatpanda-training')
    bigfatpanda_issues = github_repo_issues(
        username='bigfatpanda-training',
        repo_name='pandas-practical-python-primer')
    pprint.pprint(user_info.json())
    pprint.pprint(user_repos.json())
    pprint.pprint(bigfatpanda_issues.json())

