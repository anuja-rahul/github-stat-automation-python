import os
import json
import dotenv
import datetime as dt
from github import Github


class APIHandler:

    dotenv.load_dotenv()
    __GITHUB_TOKEN = os.getenv('SECRET_TOKEN')

    def __init__(self):
        self.__init_env()
        self.__today = dt.datetime.today()
        self.__token = self.__get_token()

        self.__repositories = self.__get_repositories()
        self.__stars = self.__get_stars()
        self.__views = self.__get_repo_views()
        self.__clones = self.__get_repo_clones()
        self.__collaborators = self.__get_repo_collaborators()
        self.__stargazers = self.__get_stargazers()
        self.__content = self.__get_repo_content()

        self.__json_content = self.__generate_jason_content()
        self.__dump_to_json()

    @staticmethod
    def __init_env():
        if "stats" not in os.listdir():
            os.mkdir("stats")

    def __get_token(self):
        return Github(self.__GITHUB_TOKEN)

    def __get_repositories(self) -> list[str]:
        repositories = []
        for repo in self.__token.get_user().get_repos():
            repositories.append(repo.full_name)
        return repositories

    def __get_stars(self) -> dict[str:int]:
        stars = {}
        for repo in self.__repositories:
            current_repo = self.__token.get_repo(repo)
            stars[f'{repo}'] = current_repo.stargazers_count
        return stars

    def __get_repo_views(self) -> dict[str:int]:
        views = {}
        for repo in self.__repositories:
            current_repo = self.__token.get_repo(repo)
            views[f'{repo}'] = current_repo.get_views_traffic()['count']
        return views

    def __get_repo_clones(self) -> dict[str:int]:
        clones = {}
        for repo in self.__repositories:
            current_repo = self.__token.get_repo(repo)
            clones[f'{repo}'] = current_repo.get_clones_traffic()['count']
        return clones

    def __get_repo_collaborators(self) -> dict[str:list[str]]:
        collaborators = {}
        collab_list = []
        for repo in self.__repositories:
            current_repo = self.__token.get_repo(repo)
            for collabs in current_repo.get_collaborators():
                collab_list.append(collabs.name)
            collaborators[f'{repo}'] = collab_list
            collab_list = []
        return collaborators

    def __get_stargazers(self) -> dict[str:list[str]]:
        stargazers = {}
        star_list = []
        for repo in self.__repositories:
            current_repo = self.__token.get_repo(repo)
            for stars in current_repo.get_stargazers():
                star_list.append(stars.name)
            stargazers[f'{repo}'] = star_list
            star_list = []
        return stargazers

    def __get_repo_content(self) -> dict[str:list[str]]:
        contents = {}
        file_list = []
        for repo in self.__repositories:
            current_repo = self.__token.get_repo(repo)
            for files in current_repo.get_contents(""):
                file_list.append(files.path)
            contents[f'{repo}'] = file_list
            file_list = []
        return contents

    def __generate_jason_content(self):
        json_dict = {}
        for repo in self.__repositories:
            json_dict[f'{repo}'] = {
                "stars": self.__stars[f'{repo}'],
                "views": self.__views[f'{repo}'],
                "clones": self.__clones[f'{repo}'],
                "collaborators": self.__collaborators[f'{repo}'],
                "stargazers": self.__stargazers[f'{repo}'],
                "content": self.__content[f'{repo}']
            }
        return json_dict

    def __dump_to_json(self):
        json_file = f"stats/{self.__today.day:02d}-{self.__today.month:02d}-" f"{self.__today.year}.json"
        with open(json_file, 'w') as file:
            file.write(json.dumps(self.__json_content, indent=3))

    def __repr__(self):
        return (f"({self.__repositories}, {self.__stars}, {self.__views}, {self.__clones}, "
                f"{self.__collaborators}, {self.__stargazers}, {self.__content})")
