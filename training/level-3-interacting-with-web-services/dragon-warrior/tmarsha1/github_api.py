"""
GitHub api stuff
"""

from datetime import datetime
import pprint
import requests
from configuration_panda import ConfigurationPanda
from Models import Credentials
from Models import GitHubCredentials

credentials = ConfigurationPanda(['PROGRAM_CREDENTIALS'])


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
        """

        user_url = self.user_info(username=username)
        repos_url = user_url
        pprint.pprint(repos_url)
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


if __name__ == "__main__":
    newCredentials = GitHubCredentials.GitHubCredentials()

    github = Github(oauth_token=newCredentials.tokens)

    #github_info = Github.urls
    #pprint.pprint(dict(github_info))

    #github_user = github.user_info("bigfatpanda-training")
    #pprint.pprint(github_user.json())

    #github_repos = github.user_repos("troylmarshall")
    #github_repos = github.user_repos("bigfatpanda-training")
    #pprint.pprint(github_repos.json())
    #issues = github_repos_issues("bigfatpanda-training",
    #                             "pandas-practical-python-primer")

    # for issue in issues:
    #    print(issue["title"])
    #pprint.pprint(issues.json())

    new_issue = github.create_issue(
        username="troylmarshall",
        repo_name="pandas-practical-python-primer",
        title="Example Issue {id}".format(id=datetime.now()))

    #edit_issue = github.edit_issue(
    #    username="troylmarshall",
    #    repo_name="pandas-practical-python-primer",
    #    title="EDITED Example Issue",
    #    issue_number=new_issue.json()['number'],
    #    body="This is my edited issue.",
    #    assignee="troylmarshall",
    #    labels=["label1", "label2"])
