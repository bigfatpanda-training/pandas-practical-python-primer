from configuration_panda import ConfigurationPanda
from Models.Credentials import Credentials


class GitHubCredentials(Credentials):
    __credentials = ConfigurationPanda(['PROGRAM_CREDENTIALS'])

    def __init__(self):
        pass

    def tokens(self) -> str:
        api_key = GitHubCredentials.__credentials.tokens["github"]
        return str(api_key)