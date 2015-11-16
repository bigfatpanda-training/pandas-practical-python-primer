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

    Attributes:
        urls: Github API url templates for accessing various functionality.

    Methods:
        user_info: Provide information on a given Github user.
        user_repos: Provide information on a given users repositories.
        repo_issues: Provide information on a given repo's issues.
    """

    def __init__(self):
        self.urls = requests.get("https://api.github.com").json()

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
    import pprint
    github = Github()

    user_info = github.user_info('bigfatpanda-training')
    user_repos = github.user_repos('bigfatpanda-training')
    bigfatpanda_issues = github.repo_issues(
        username='bigfatpanda-training',
        repo_name='pandas-practical-python-primer')

    pprint.pprint(user_info.json())
    pprint.pprint(user_repos.json())
    pprint.pprint(bigfatpanda_issues.json())

