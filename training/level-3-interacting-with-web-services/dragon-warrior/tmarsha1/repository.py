"""
This module provides a CLI that interacts with cloud
repositories such as GitHub.
"""

import click
from datetime import datetime
import pprint
import github_api
from Models import GitHubCredentials

newCredentials = GitHubCredentials.GitHubCredentials()


@click.group()
def repository_cli():
    pass


# get_user_info -u TroyLMarshall
@repository_cli.command()
@click.option('-u', '--user', required=True)
def get_user_info(user: str):
    github = github_api.Github(oauth_token=newCredentials.tokens())
    user_info = github.user_info(username=user)
    pprint.pprint(user_info.json())


# user_repositories -u bigfatpanda-training
@repository_cli.command()
@click.option('-u', '--user', required=True)
def user_repositories(user: str):
    github = github_api.Github(oauth_token=newCredentials.tokens())
    repos = github.user_repos(username=user)
    pprint.pprint(repos.json())


# repository_issues -u bigfatpanda-training -r pandas-practical-python-primer
@repository_cli.command()
@click.option('-u', '--user', required=True)
@click.option('-r', '--repository', required=True)
def repository_issues(user: str, repository: str):
    github = github_api.Github(oauth_token=newCredentials.tokens())
    issues = github.repos_issues(username=user, repo_name=repository)
    pprint.pprint(issues.json())


# create_issue -u troylmarshall -r pandas-practical-python-primer -t "Example Issue"
@repository_cli.command()
@click.option('-u', '--user', required=True)
@click.option('-r', '--repository', required=True)
@click.option('-t', '--title', required=True)
def create_issue(user: str, repository: str, title: str):
    github = github_api.Github(oauth_token=newCredentials.tokens())
    mod_title = (title + ' {stamp}').format(stamp=datetime.now())
    new_issue = github.create_issue(username=user, repo_name=repository,
                                    title=mod_title)
    pprint.pprint(new_issue.json())


# edit_issue -u troylmarshall -r pandas-practical-python-primer -t "EDITED Example Issue" -id 8
@repository_cli.command()
@click.option('-u', '--user', required=True)
@click.option('-r', '--repository', required=True)
@click.option('-t', '--title', required=True)
@click.option('-id', required=True)
def edit_issue(user: str, repository: str, title: str, issue: int):
    github = github_api.Github(oauth_token=newCredentials.tokens())
    mod_title = (title + ' {stamp}').format(stamp=datetime.now())
    edit_issue = github.edit_issue(username=user, repo_name=repository,
                                   issue_number=issue, title=mod_title,
                                   body="This is my edited issue.",
                                   assignee="troylmarshall",
                                   labels=["Test1", "Test2"])
    pprint.pprint(edit_issue.json())


# create_repository -n "A test repository"
@repository_cli.command()
@click.option('-n', '--name', required=True)
def create_repository(name: str):
    github = github_api.Github(oauth_token=newCredentials.tokens())
    payload = {'has_issues': True}
    repo = github.create_repository(name=name, kwargs=payload)
    pprint.pprint(repo.json())


# edit_repository -u TroyLMarshall -r A-test-repository
@repository_cli.command()
@click.option('-u', '--user', required=True)
@click.option('-r', '--repository', required=True)
def edit_repository(user: str, repository: str):
    github = github_api.Github(oauth_token=newCredentials.tokens())
    payload = {'name': repository,
               'description': 'A short description of my programmatically'
                              ' added repository - {date}.'.format(
                                    date=datetime.now())}
    repo = github.update_repository(owner=user, repo=repository,
                                    kwargs=payload)
    pprint.pprint(repo.json())


# delete_repository -u TroyLMarshall -r A-test-repository
@repository_cli.command()
@click.option('-u', '--user', required=True)
@click.option('-r', '--repository', required=True)
def delete_repository(user: str, repository: str):
    github = github_api.Github(oauth_token=newCredentials.tokens())
    result = github.delete_repository(owner=user, repo=repository)
    pprint.pprint(result)


# create_pull_request -u bigfatpanda-training -r pandas-practical-python-primer
@repository_cli.command()
@click.option('-u', '--user', required=True)
@click.option('-r', '--repository', required=True)
def create_pull_request(user: str, repository: str):
    github = github_api.Github(oauth_token=newCredentials.tokens())
    payload = {"title": "A programmatic pull request",
        "head": "TroyLMarshall:master",
        "base": "master",
        "body": "Submitted from CLI"}
    new_pull_request = github.create_pull_request(username=user,
        repo_name=repository, kwargs=payload)
    pprint.pprint(new_pull_request.json())



# update_pull_request -u bigfatpanda-training -r pandas-practical-python-primer -p 99
@repository_cli.command()
@click.option('-u', '--user', required=True)
@click.option('-r', '--repository', required=True)
@click.option('-p', '--pull', required=True)
def update_pull_request(user: str, repository: str, pull: int):
    github = github_api.Github(oauth_token=newCredentials.tokens())
    payload = {"title": "Update pull request from CLI",
        "body": "{date}".format(date=datetime.now())}
    new_pull_request = github.update_pull_request(username=user,
        repo_name=repository, pull=pull, kwargs=payload)
    pprint.pprint(new_pull_request.json())


if __name__ == "__main__":
    repository_cli()
