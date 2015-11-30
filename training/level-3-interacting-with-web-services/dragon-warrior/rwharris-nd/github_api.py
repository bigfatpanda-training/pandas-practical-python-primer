"""
This module interacts with the Github API.
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
    
    def create_issue(self, username: str, repo_name: str,
                     title: str, body: str=None,
                     assignee: str=None, milestone: str=None,
                     labels: list=None) -> requests.Response:
        """
        This
        
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
        url = (
            self.urls['repository_url'].format(
                owner=username, repo=repo_name) + "/issues")
        payload = {
            "title": title, "body": body, "assignee": assignee,
            "milestone": milestone, "labels": labels
        }
        return requests.post(url, headers=headers, json=payload)

    def update_issue(self, username: str, repo_name: str, issue_number: int,
                     title: str, body: str=None,
                     assignee: str=None, state: str=None, milestone: str=None,
                     labels: list=None) -> requests.Response:
        """
        This

        Args:
            username:
            repo_name:
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
        url = (
            self.urls['repository_url'].format(
                owner=username, repo=repo_name) + "/issues/" + issue_number)
        payload = {
            "title": title, "body": body, "assignee": assignee,
            "state": state, "milestone": milestone, "labels": labels
        }

        if state is not None:
            payload['state'] = state

        return requests.patch(url, headers=headers, json=payload)

    def create_repo(self, name: str, **kwargs) -> requests.Response:
        """
        This creates a repository for the authenticated user with the given name.

        Arguments:
            name: A str specifying the name of the repository.
            kwargs: Refer to the Github API document for all other valid keyword arguments
                at https://developer.github.com/v3/repos/#create

        Returns:
            A requests.Response object.
        """
        headers = {'Authorization': 'token {}'.format(self.oauth_token)}
        url = (self.urls['current_user_url'] + "/repos")
        kwargs['name'] = name

        return requests.post(url, headers=headers, json=kwargs)

    def update_repo(self, username: str, repo_name: str, **kwargs):
        """
        This updates the given repository belonging the given user.

        Arguments:
            username: A str specifying a valid Github username.
            repo_name: A str specifying a repository belonging to the given owner.
            kwargs: Refer to the Github API document for all other valid keyword arguments
                at https://developer.github.com/v3/repos/#edit

        Returns:
            A requests.Response object.
        """
        headers = {'Authorization': 'token {}'.format(self.oauth_token)}
        url = self.urls['repository_url'].format(
            owner=username,repo=repo_name)

        return requests.patch(url, headers=headers, json=kwargs)

    def delete_repo(self, username: str, repo_name: str) -> requests.Response:
        """
        This deletes the specified repository belonging to the given user.

        Arguments:
            username: A str specifying a valid Github username.
            repo_name: A str specifying a repository belonging to the given owner.

        Returns:
            A requests.Response object.
        """
        headers = {'Authorization': 'token {}'.format(self.oauth_token)}
        url = self.urls['repository_url'].format(
            owner=username,repo=repo_name)

        return requests.delete(url, headers=headers)

    def create_pull_request(self, username: str, repo_name: str,
                            title: str, head: str, base: str, **kwargs
                            ) -> requests.Response:
        """
        This creates a pull request with the specified title targeting the given base to pull
        from the updated head from the specified repository belonging to the given user.

        Arguments:
            username: A str specifying a valid Github username.
            repo_name: A str specifying a repository belonging to the given owner.
            title: A str specifying the title of the pull request.
            head: A str specifying the name of the branch where your changes are implemented.
            base: A str specifying the name of the branch you want your changes pulled into.
            kwargs: Refer to the Github API document for all other valid keyword arguments
                at https://developer.github.com/v3/pulls/#create-a-pull-request

        Returns:
            A requests.Response object.
        """
        headers = {'Authorization': 'token {}'.format(self.oauth_token)}
        url = self.urls['repository_url'].format(
            owner=username,repo=repo_name) + "/pulls"

        kwargs['title'] = title
        kwargs['head'] = head
        kwargs['base'] = base

        return requests.post(url, headers=headers, json=kwargs)

    def update_pull_request(self, username: str, repo_name: str,
                            number: int, **kwargs) -> requests.Response:
        """
        This updates the specified pull request within the given repository belonging
        to the specified user.

        Arguments:
            username: A str specifying a valid Github username of the owner of the repository.
            repo_name: A str specifying a repository belonging to the given owner.
            number: An int specifying the number of the pull request to update.
            kwargs: Refer to the Github API document for all other valid keyword arguments
                at https://developer.github.com/v3/pulls/#update-a-pull-request

        Returns:
            A requests.Response object.
        """
        headers = {'Authorization': 'token {}'.format(self.oauth_token)}
        url = self.urls['repository_url'].format(
            owner=username,repo=repo_name) + "/pulls/" + str(number)

        return requests.patch(url,header=headers,json=kwargs)

if __name__ == "__main__":
    github = Github(oauth_token=credentials.tokens['github'])

    create_pull = github.create_pull_request(
        username= 'bigfatpanda-training',
        repo_name= 'pandas-practical-python-primer',
        title= '11/30 Homework Update',
        head= 'rwharris-nd:master',
        base= 'master'
    )
    
    update_pull = github.update_pull_request(
        username= 'bigfatpanda-training',
        repo_name= 'pandas-practical-python-primer',
        number= create_pull.json('number'),
        body= 'This pull request has been updated.'
    )