import os
import sys
import re
import math
import argparse
import importlib
from github import Github

from .logic.git_logic import GithubLogic

import click
import requests

from click import Context

pass_github = click.make_pass_decorator(GithubLogic)

@click.group()
@click.option("--key", "-k")
@click.option("--repo", "-repo", required=True)
@click.pass_context
def manager(context: Context, key: str, repo: str):
   # context.obj = ?
   # do something
   pass

@manager.command()
@pass_github
def release(git: GithubLogic):
   pass

@manager.command()
@pass_github
def create(git: GithubLogic):
   pass

@manager.command()
@pass_github
def delete_release(git: GithubLogic):
   pass

@manager.command()
@pass_github
def update_release(git: GithubLogic):
   pass


# TODO: Add more
cli = click.CommandCollection(sources=[manager])

if __name__ == "__main__":
   cli()