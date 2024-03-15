import os
import dotenv
from github import Github


class APIHandler:

    dotenv.load_dotenv()
    __GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

    def __init__(self):
        self.__token = Github(self.__GITHUB_TOKEN)
        self.__repositories = self.__get_repositories()

    def __get_repositories(self) -> list[str]:
        repositories = []
        for repo in self.__token.get_user().get_repos():
            repositories.append(repo.full_name)
        return repositories
