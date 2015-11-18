"""
This module interacts with the Github API to demonstrate
interaction with RESTful web services.
"""

import requests

from configuration_panda import ConfigurationPanda

credentials = ConfigurationPanda(['PROGRAM_CREDENTIALS'])


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

    def user_info(self, username: str) -> requests.Response:
        """
        Obtain information about a given user in Github.

        Args
            username: A str specifying a valid Github username.

        Returns
            A requests.Response object.
        """
        url = self.urls['user_url'].format(user=username)
        return requests.get(url)

    def user_repos(self, username: str) -> requests.Response:
        """
        Obtain information about a given user's repositories in Github.

        Args
            username: A str specifying a valid Github username.

        Returns
            A requests.Response object.
        """
        url = self.urls['user_url'].format(user=username) + "/repos"
        return requests.get(url)

    def repo_issues(self, username: str, repo_name: str) -> requests.Response:
        """
        Obtain information about a given repositories issues in Github.

        Args
            username: A str specifying a valid Github username.
            repo_name: A str specifying a Github repo that belongs to the
                specified user.

        Returns
            A requests.Response object.
        """
        url = (
            self.urls['repository_url'].format(
                owner=username, repo=repo_name) + "/issues")
        return requests.get(url)


if __name__ == "__main__":
    github = Github(oauth_token=credentials.tokens['github'])

