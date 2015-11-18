"""
This module interacts with the Github API.
"""

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
    url += "?access_token=" + credentials['tokens']['github']
    response = requests.get(url)
    return response

def github_user_info(username: str) -> requests.Response:
    """
    Obtain information about the given user in Github.

    Args:
        username: A str specifying a valid Github username.

    Returns:
        A requests.Response object.
    """
    api_urls = github_entry_point().json()
    url = api_urls['user_url'].format(user=username)
    url += "?access_token=" + credentials['tokens']['github']
    response = requests.get(url)
    return response

def github_repo_info(username: str) -> requests.Response:
    """
    Obtain list of repos for the given user on Github.

    Args:
        username: A str specifying a valid Github username.

    Returns:
        A requests.Response object.
    """
    user_info = github_user_info(username).json()
    url = user_info['repos_url']
    url += "?access_token=" + credentials['tokens']['github']
    response = requests.get(url)
    return response

def github_repo_issues(username: str, repo: str) -> requests.Response:
    """
    Obtain list of issues for the given repo belonging to the given user on Github.

    Args:
        username: A str specifying a valid Github username.
        repo: A str specifying the repository for which to return issues.

    Returns:
        A requests.Reponse object.
    """
    #'https://api.github.com/repos/rwharris-nd/pandas-practical-python-primer/issues{/number}'
    #'id': 43707658
    response = github_repo_info(username).json()
    i = 0
    while i < len(response):
        if response[i]['name'] == repo:
            url = response[i]['issues_url'].replace("{/number}","")
        i += 1
    print(url)
    response = requests.get(url)
    return response

if __name__ == '__main__':
    # github_info = github_entry_point()
    import pprint
    github_info = github_repo_issues('rwharris-nd','pandas-practical-python-primer')
    pprint.pprint(github_info.json())