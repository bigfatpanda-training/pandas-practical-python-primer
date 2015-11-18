"""
GitHub api stuff
"""

import pprint
import requests
from configuration_panda import ConfigurationPanda

credentials = ConfigurationPanda(['PROGRAM_CREDENTIALS'])


def github_entry_point() -> requests.Response:
    """
    Return information on URLs for Github API.

    Returns:
        A requests.Response object.
    """

    url = "https://api.github.com"
    response = requests.get(url)
    return response


def github_user_info(username: str) -> requests.Response:
    """
    Obtain information about a given user in Github.
    Args:
        username: A string specifying a valid Github username

    Returns:
        A requests.Response object
    """
    api_urls = github_entry_point().json()
    url = api_urls['user_url'].format(user=username)
    response = requests.get(url)
    return response


def github_user_repos(username: str) -> requests.Response:
    """
    Obtain the repos for a given user in Github.
    Args:
        username: A string specifying a valid Github username

    Returns:
        A requests.Response object
    """

    repos_url = github_user_info(username).json()
    url = repos_url['repos_url']
    response = requests.get(url)
    return response


def github_repos_issues(username: str, repo_name: str) -> requests.Response:
    """
    Obtain the issues for a given user in Github.
    Args:
        username: A string specifying a valid Github username
        repo_name: A string specifying a valid repository name for a user

    Returns:
        A requests.Response object

    Reference:
        https://developer.github.com/v3/issues/#list-issues-for-a-repository
    """

    issues_url = "https://api.github.com/repos/{owner}/{repo}/issues"
    url = issues_url.format(owner=username, repo=repo_name)
    response = requests.get(url)
    return response


if __name__ == "__main__":
    #github_info = github_entry_point()
    #pprint.pprint(dict(github_info.json()))
    #github_user = github_user_info("bigfatpanda-training")
    #pprint.pprint(github_user.json())
    #github_repos = github_user_repos("troylmarshall")
    #github_repos = github_user_repos("bigfatpanda-training")
    #pprint.pprint(github_repos.json())
    issues = github_repos_issues("bigfatpanda-training",
                                 "pandas-practical-python-primer")
    pprint.pprint(issues.json())

