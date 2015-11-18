"""
This program...
"""

import requests
from configuration_panda import ConfigurationPanda


credentials = ConfigurationPanda(['PROGRAM_CREDENTIALS'])


def github_entry_point() -> requests.Response:
    """
    Return information on URLs for Github API.

    Returns:
        A request.Response object.
    """
    url = "https://api.github.com"
    response = requests.get(url)
    return response


def github_user_info(username: str) -> requests.Response:
    """
    Obtain information about a given user in Github.

    Args:
        username: A str specifying the Github username.

    Return:
        A request.Response object that represents the Github user.
    """
    api_urls = github_entry_point().json()
    url = api_urls['user_url'].format(user=username)
    response = requests.get(url)
    return response


def github_user_repos(username: str) -> requests.Response:
    """

    :param username:
    :return:
    """

    api_urls = github_user_info(username).json()
    url = api_urls['repos_url']
    response = requests.get(url)
    return response


def github_user_repo_issues(username: str, repository: str) -> requests.Response:
    """

    Args:
        username:
        repo:

    Returns:

    """
    api_urls = github_entry_point().json()
    url = api_urls['repository_url'].format(owner=username, repo=repository)
    response = requests.get(url)
    api_urls = response.json()
    url = api_urls['issues_url'].rsplit('{')[0]
    response = requests.get(url)
    return response


if __name__ == "__main__":
    import pprint
    # github_info = github_entry_point()
    # github_info = github_user_info('ndrk')
    pprint.pprint(github_user_repo_issues('ndrk', 'pandas-practical-python-primer').json())
