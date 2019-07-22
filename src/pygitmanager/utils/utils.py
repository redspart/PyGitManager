import os

def read_key(path_or_key):
    if _file_exist(path_or_key):
        path_or_key = os.path.abspath(path_or_key)
        with open(path_or_key, "r") as f:
            key = f.read()
            f.close()
        return key # key from path
    return path_or_key # key