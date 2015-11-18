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
        url = (self.urls['repository_url'].format(
            owner=username, repo=repo_name) + "/issues")
        return requests.get(url)

    def create_issue(self, username: str, repo_name: str,
                     title: str, body: str=None,
                     assignee: str=None, milestone: str=None,
                     labels: list=None) -> requests.Response:
        """
        Create an issue on a given repo.

        This method requires authentication and will fail if the requesting
        user does not have pull access on the designated repo.

        Args:
            username: A str of a valid Github username designating
                the owner of the repo.
            repo_name: A str designating the repo to create the issue for.
            title: A str designating the title of the issue.
            body: A str designating the body/description of the issue.
            assignee: Github username to assign the issue to.  Will be
                ignored if issue creator does not have push access to
                repository.
            milestone: Project milestone to assign issue to.  Will be
                ignored if issue creator does not have push access to
                repository.
            labels: A list of strs containing labels for the issue. Will be
                ignored if issue creator does not have push access to
                repository.

        Returns:
            A requests.Response object.
        """
        if labels is None:
            labels = []

        arguments = locals().copy()
        arguments.pop('self')

        headers = {'Authorization': 'token {}'.format(self.oauth_token)}
        url = (self.urls['repository_url'].format(
            owner=username, repo=repo_name) + "/issues")
        payload = dict(title=title, body=body, assignee=assignee,
                       milestone=milestone, labels=labels)

        return requests.post(url, headers=headers, json=arguments)

    def update_issue(self, username: str, repo_name: str,
                     issue_number: int, **kwargs) -> requests.Response:
        """
        Create an issue on a given repo.

        This method requires authentication and will fail if the requesting
        user does not have pull access on the designated repo.

        Args:
            username: A str of a valid Github username designating
                the owner of the repo.
            repo_name: A str designating the repo to create the issue for.
            issue_number: A int designating the unique issue number.
            kwargs: All additional keyword arguments will be passed
                as JSON elements to the Github API.

        Returns:
            A requests.Response object.
        """
        headers = {'Authorization': 'token {}'.format(self.oauth_token)}
        url = (self.urls['repository_url'].format(
            owner=username, repo=repo_name) + "/issues/" + str(issue_number))

        return requests.patch(url, headers=headers, json=kwargs)


if __name__ == "__main__":
    github = Github(oauth_token=credentials.tokens['github'])
    new_issue = github.create_issue(
        username='bigfatpanda-training',
        repo_name='pandas-practical-python-primer',
        title='A Example Issue',
        body="This is an example issue.",
        labels=['bug', 'help wanted'])

    update_issue = github.update_issue(
        username='bigfatpanda-training',
        repo_name='pandas-practical-python-primer',
        issue_number=new_issue.json()['number'],
        title='A KWARGS PATCHED Example Issue',
        body="This is an example issue that has been patched.",
        assignee='eikonomega',
        labels=['enhancement', 'help wanted'],
        extra_junk='test')
