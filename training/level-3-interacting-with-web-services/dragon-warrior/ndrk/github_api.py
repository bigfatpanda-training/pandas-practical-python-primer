"""
This program...
"""

import requests
from configuration_panda import ConfigurationPanda


credentials = ConfigurationPanda(['PROGRAM_CREDENTIALS'])


class Github:
    """
    Provides access to the Github API.

    Class Attributes:
        urls: Github url templates for acessing verious functionality.

    Attributes:
        oauth_token: A valid OAuth oauth_token for access to the API.

    Methods:

    """
    urls = requests.get("https://api.github.com").json()

    def __init__(self, oauth_token: str):
        self.oauth_token = oauth_token

    def user_info(self, username: str) -> requests.Response:
        """
        Obtain information about a given user in Github.

        Args:
            username: A str specifying the Github username.

        Return:
            A request.Response object that represents the Github user.
        """
        url = self.urls['user_url'].format(user=username)
        response = requests.get(url)
        return response

    def user_repos(self, username: str) -> requests.Response:
        """

        :param username:
        :return:
        """
        api_urls = user_info(username).json()
        url = api_urls['repos_url']
        response = requests.get(url)
        return response

    def user_repo_issues(self, username: str, repository: str) -> requests.Response:
        """

        Args:
            username:
            repo:

        Returns:

        """
        url = self.urls['repository_url'].format(owner=username, repo=repository)
        response = requests.get(url)
        api_urls = response.json()
        url = api_urls['issues_url'].rsplit('{')[0]
        response = requests.get(url)
        return response

    def create_repo(
            self,
            username: str,
            repo_name: str,
            **kwargs) -> requests.Response:
        headers = {'Authorization': 'token {}'.format(self.oauth_token)}

        url = self.urls['user_repositories_url'].replace("{user}", username).rsplit('{')[0]

        return requests.post(url, headers=headers, json=kwargs)

    def update_repo(self, repo_name: str) -> requests.Response:
        pass

    def delete_repo(self, repo_name: str) -> requests.Response:
        pass

    def create_issue(
            self,
            username: str,
            repo_name: str,
            title: str,
            body: str=None,
            assignee: str=None,
            milestone: str=None,
            labels: list=None):
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

        url = self.urls['repository_url'].format(owner=username, repo=repo_name)
        response = requests.get(url)
        api_urls = response.json()
        url = api_urls['issues_url'].rsplit('{')[0]

        payload = {
            "title": title, "body": body, "assignee": assignee, "milestone": milestone, "labels": labels
        }

        return requests.post(url, headers=headers, json=payload)

    def update_issue(
            self,
            username: str,
            repo_name: str,
            issue_number: int,
            title: str,
            body: str=None,
            assignee: str=None,
            state: str=None,
            milestone: str=None,
            labels: list=None):
        """

        Args:
            username:
            repo_name:
            issue_number:
            title:
            body:
            assignee:
            state:
            milestone:
            labels:

        Returns:

        """
        if labels is None:
            labels = []

        headers = {'Authorization': 'token {}'.format(self.oauth_token)}

        url = self.urls['repository_url'].format(owner=username, repo=repo_name)
        response = requests.get(url)
        api_urls = response.json()
        url = api_urls['issues_url'].rsplit('{')[0]
        url += "/{}".format(issue_number)
        print(url)

        payload = {
            "title": title,
            "body": body,
            "assignee": assignee,
            "milestone": milestone,
            "labels": labels
        }

        if state is not None:
            payload['state'] = state

        return requests.patch(url, headers=headers, json=payload)


if __name__ == "__main__":
    github = Github(credentials.tokens['github'])
    # new_issue = github.create_issue(
    #     username='ndrk',
    #     repo_name='pandas-practical-python-primer',
    #     title='Example Issue'
    # )

    # updated_issue = github.update_issue(
    #     username='ndrk',
    #     repo_name='pandas-practical-python-primer',
    #     title='Updated Example Issue',
    #     issue_number=new_issue.json()['number']
    # )
    # import pprint
    # github_info = github_entry_point()
    # github_info = github_user_info('ndrk')
    # pprint.pprint(github_user_repo_issues('ndrk', 'pandas-practical-python-primer').json())
