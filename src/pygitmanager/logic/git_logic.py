import os
import sys
import logging
import re

from github import Github, Repository, GitRelease, PaginatedList
import requests

#Typing
from logging import Logger

class GithubLogic:
    git: Github
    repo: Repository
    releases: PaginatedList
    logger: Logger

    def __init(self, key: str, repo: str, url: str, logger: Logger):
        self.logger = logger
        self.git = Github(base_url=url + "/api/v3", login_or_token=key) if url else Github(key)
        self._setup_logic(repo)

    def _setup_logic(self, repo: str):
        self.logger.info("Getting repos..")
        self.repo = self.git.get_repo(repo)

        self.logger.info("Getting releases..")
        self.releases = self.repo.get_releases()

    def download(self, out_path: str, tag: str):
        os.makedirs(out_path, exist_ok=True)
        release = [r for r in self.releases if r.tag_name == tag]

        if len(release) == 0:
            print(f"No release found with tag: {tag}")
            sys.exit(1)

        res = requests.get(
            release[0].get_assets()[0].browser_download_url, 
            allow_redirects=True)
        
        file_name = re.findall("filename=(.+)", res.headers.get("content-disposition"))[0]
        path = os.path.abspath(os.path.join(out_path, file_name))
        open(path, "wb").write(res.content)

    def create_release(self):
        pass

    def update_release(self):
        pass

    def delete_release(self):
        pass