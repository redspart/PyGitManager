import os
import sys
import re
import math
import argparse
import requests
from github import Github
from .base_manager import BaseManagerClass

class ReleaseManager(BaseManagerClass):
    def get_arguments(self):
        parser = argparse.ArgumentParser()
        # Download
        download_group = parser.add_argument_group("Download")
        download_group.add_argument("-dl", "--download", help="Download the non-source code tag")
        download_group.add_argument("-o", "--output", help="Output directory for the download")

            
        # delete
        delete_group =parser.add_argument_group("Delete")
        delete_group.add_argument("-d", "--delete", help="Delete the following release name")

        # create`
        create_group = parser.add_argument_group("Create")
        create_group.add_argument("-c", "--create", help="Creates release with given name")
        create_group.add_argument("-m", "--message", required="-c" in sys.argv, help="Message of new release")

        # add an asset
        asset_group = parser.add_argument_group("Assets")
        asset_group.add_argument("-u", "--update", help="Update a release by adding another asset", action="store_true")
        asset_group.add_argument("-a", "--asset", required="-u" in sys.argv, help="Path to asset to upload")

        # optionals
        extras_group = parser.add_argument_group("Optional")
        extras_group.add_argument("-p", "--print", help="Print all release tags", action="store_true")
        extras_group.add_argument("-e", "--enterprise", help="Using enterprise Github account enter the address needed to connect to; provide a url like so: https://github.com/")
        extras_group.add_argument("-t", "--tag", required="-u" in sys.argv, help="Target tag")
        extras_group.add_argument("-gl", "--get_latest", help="Get latest tag", action="store_true")

        return parser

# def _error_out(msg):
#     print(msg)
#     sys.exit(1)

# def _file_exist(path):
#     return os.access(path, os.W_OK)

# def _get_release_based_tag(releases, tag):
#     release = [release for release in releases if release.tag_name == tag][0]
#     if not release:
#         _error_out("Release tag %s does not exists" % args.tag)
#     return release

# def create_release(repository, releases, name, message, tag=None):
#     if not tag:
#         tag = re.findall(".\d", releases[0].tag_name)
#         tag[-1] = str("%.1f" % (float(tag[-1]) + .1))[1:]
#         tag = "".join(tag)

#     release = repository.create_git_release(tag, name, message, prerelease=True)
#     return release

# def upload_asset(filep, tag=None, release=None, releases=None):
#     if not _file_exist(filep):
#         _error_out("File not found")
#     if not release:
#         release = _get_release_based_tag(releases, tag)
#     filep = os.path.abspath(filep)
#     release.upload_asset(filep)

# def download_asset(filep, tag, releases):
#     try:
#         if not _file_exist(filep):
#             filep = os.path.abspath(filep)
#             os.mkdir(filep)
#         release = _get_release_based_tag(releases, tag)
#         uri = release.get_assets()[0].browser_download_url
#         response = requests.get(uri, allow_redirects=True)
#         fname = re.findall("filename=(.+)", response.headers.get("content-disposition"))[0]
#         print("Writing file %s" % fname)
#         filep = os.path.abspath(filep + "/%s" % fname)
#         open(filep, "wb").write(response.content)
#     except Exception as e:
#         _error_out("Couldn't download file to %s based on tag %s, \n e: %s" % (filep, tag, e))