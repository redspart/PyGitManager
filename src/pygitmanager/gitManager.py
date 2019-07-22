import os
import sys
import re
import math
import argparse
import requests
import importlib
from github import Github

from managers.release_manager import ReleaseManager


def parse_cli():
   parser = argparse.ArgumentParser(description='Manages release assets for a Github release')

   required_groups = parser.add_argument_group("Required (key not required if downloading")
   required_groups.add_argument("-k", "--key", required="-dl" not in sys.argv, help="Key or path to .key file")
   required_groups.add_argument("-repo", "--repo", required=True, help="Repository name in the format of <user>/<project_name>")
   parser.add_argument("--use", required=True, help="--use release")

   args, unknown = parser.parse_known_args()
   known, instance = get_instance(args.use, unknown)
   args = {**vars(args), **vars(known)}
   return (args, instance)

def get_instance(use, unknown):
   module = importlib.import_module("managers.%s_manager" % use)
   _class = getattr(module, "%sManager" % use.capitalize())
   _instance = _class()
   parser = _instance.get_arguments()
   known = parser.parse_args(unknown)
   return (known, _instance)



# def run(args):
    # if args.download:
    #     gh = Github()
    # else:
    #     key = read_key(args.key)
    #     gh = Github(base_url=args.e + "/api/v3", login_or_token=key) if args.enterprise else Github(key)
    # repository = gh.get_repo(args.repo)
    # releases = repository.get_releases()

    # if args.download:
    #     download_asset(args.output, args.download, releases)
    #     print("Download complete")

    # if args.create:
    #     release = create_release(repository, releases, args.create, args.message, args.tag)
    #     print("Created release: %s" % args.create)
    #     if args.asset:
    #         upload_asset(args.asset, release=release)
    #         print("Added asset to release")

    # if args.update:
    #     upload_asset(args.asset, tag=args.tag, releases=releases)
    #     print("Uploaded asset")
        
    # if args.delete:
    #     [x.delete_release() for x in releases if x.title == args.delete or x.tag_name == args.delete]
    #     print("Deleted release")

    # if args.print:
    #     [print("%s | %s" %(release.title, release.tag_name)) for release in releases]
    
    # if args.get_latest:
    #     print(releases[0].tag_name) # 0 is always the last


if __name__ == "__main__":
    args = parse_cli()
    #run(args)