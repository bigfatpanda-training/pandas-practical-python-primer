"""
GitHub api stuff
"""

from datetime import datetime
import pprint
import requests
from Models import GitHubCredentials


class Github:
    """
    Provides access to the Github API.

    Class Attributes:
        urls: Github API url templates for accessing various functionality.

    Attributes:
        oauth_token: A valid OAuth oath_token for access to the API.

    Methods:
        user_info:
        user_repos:
        repos_issues:
    """
    urls = requests.get("https://api.github.com").json()

    def __init__(self, oauth_token):
        self.oauth_token = oauth_token

    def user_info(self, username: str) -> requests.Response:
        """
        Obtain information about a given user in Github.
        Args:
            username: A string specifying a valid Github username

        Returns:
            A requests.Response object
        """
        api_urls = self.urls
        url = api_urls['user_url'].format(user=username)
        response = requests.get(url)
        return response


    def user_repos(self, username: str) -> requests.Response:
        """
        Obtain the repos for a given user in Github.
        Args:
            username: A string specifying a valid Github username

        Returns:
            A requests.Response object

        Reference:
            https://developer.github.com/v3/repos/#list-user-repositories
        """

        api_url = 'https://api.github.com/users/{username}/repos'
        url = api_url.format(username=username)
        response = requests.get(url)
        return response



        #user_url = self.user_info(username=username)
        #repos_url = user_url
        #pprint.pprint(repos_url)
        #url = repos_url['repos_url']
        #response = requests.get(url)
        #return response


    def repos_issues(self, username: str, repo_name: str) -> requests.Response:
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


    def create_issue(self, username: str, repo_name: str, title: str,
                     body: str=None, assignee: str=None, milestone: str=None,
                     labels: list=None) -> requests.Response:
        """

        Args:
            username:
            repo_name:
            title:
            body:
            assignee:
            milestone:
            labels:

        Returns:

        """
        if labels is None:
            labels = []

        headers = {'Authorization': 'token {}'.format(self.oauth_token)}
        issues_url = "https://api.github.com/repos/{owner}/{repo}/issues"
        url = issues_url.format(owner=username, repo=repo_name)
        payload = {
            "title": title,
            "body": body,
            "assignee": assignee,
            "milestone": milestone,
            "labels": labels
        }
        return requests.post(url, headers=headers, json=payload)


    def edit_issue(self, username: str, repo_name: str, issue_number: int,
                     title: str, body: str=None, assignee: str=None,
                     milestone: str=None, labels: list=None,
                     state: str=None) -> requests.Response:
        """

        Args:
            username:
            repo_name:
            issue_number:
            title:
            body:
            assignee:
            milestone:
            labels:
            state:
        Returns:

        """
        if labels is None:
            labels = []

        headers = {'Authorization': 'token {}'.format(self.oauth_token)}
        issues_url = "https://api.github.com/repos/{owner}/{repo}/issues/{id}"
        url = issues_url.format(owner=username, repo=repo_name, id=issue_number)
        payload = {
            "title": title,
            "body": body,
            "assignee": assignee,
            "milestone": milestone,
            "labels": labels
        }

        if state is not None:
            payload["state"] = state

        return requests.patch(url, headers=headers, json=payload)


    def create_repository(self, name: str, **kwargs) -> requests.Response:
        """

        Args:
            name:
            kwargs:

        Returns:

        Reference:
            https://developer.github.com/v3/repos/#create
        """

        headers = {'Authorization': 'token {}'.format(self.oauth_token)}
        url = "https://api.github.com/user/repos"
        kwargs.update({'name': name})
        return requests.post(url, headers=headers, json=kwargs)


    def update_repository(self, owner: str, repo: str,
                          **kwargs) -> requests.Response:
        """

        Args:
            owner:
            repo:
            **kwargs:

        Returns:

        Reference:
            https://developer.github.com/v3/repos/#edit
        """
        headers = {'Authorization': 'token {}'.format(self.oauth_token)}
        edit_url = "https://api.github.com/repos/{owner}/{repo}"
        url = edit_url.format(owner=owner, repo=repo)
        return requests.patch(url, headers=headers, json=kwargs["kwargs"])


    def delete_repository(self, owner: str, repo: str) -> requests.Response:
        """

        Args:
            owner:
            repo:

        Returns:

        Reference:
            https://developer.github.com/v3/repos/#delete-a-repository
        """

        headers = {'Authorization': 'token {}'.format(self.oauth_token)}
        url = "https://api.github.com/repos/{owner}/{repo}".format(
            owner=owner, repo=repo)
        return requests.delete(url, headers=headers)


    def create_pull_request(self, username: str, repo_name: str,
                            **kwargs) -> requests.Response:
        """

        Args:
            username:
            repo_name:
            kwargs:


        Returns:

        Reference:
            https://developer.github.com/v3/pulls/#create-a-pull-request
        """

        headers = {'Authorization': 'token {}'.format(self.oauth_token)}
        pulls_url = "https://api.github.com/repos/{owner}/{repo}/pulls"
        url = pulls_url.format(owner=username, repo=repo_name)
        return requests.post(url, headers=headers, json=kwargs["kwargs"])


    def update_pull_request(self, username: str, repo_name: str, pull: int,
                            **kwargs) -> requests.Response:
        """

        Args:
            username:
            repo_name:
            pull:
            kwargs:

        Returns:

        Reference:
            https://developer.github.com/v3/pulls/#update-a-pull-request
        """

        headers = {'Authorization': 'token {}'.format(self.oauth_token)}
        update_url = "https://api.github.com/repos/{owner}/{repo}/pulls/{pull}"
        url = update_url.format(owner=username, repo=repo_name, pull=pull)
        return requests.patch(url, headers=headers, json=kwargs["kwargs"])
