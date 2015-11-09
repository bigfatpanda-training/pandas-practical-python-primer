"""
This is module provides various functions for operating on files

Functions:
    copy_files: Copy file(s) to a specified location.
"""

import subprocess


def _process_files(files: list, destination: str, type: str):
    """
    Copy files to a given destination,

    Args:
        files: List of files to copy.
        destination: String specifying the destination of copied files.
    """
    for file in files:
        try:
            if type == 'cp':
                flags = '-vp'
            elif type == 'mv' or type == 'rm':
                flags = '-v'
            else:
                flags = ''
            args = [type, flags, file]
            if type != 'rm':
                args.append(destination)
            result = subprocess.check_output(
                args,
                stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as error:
            output = error.output.decode()
            if "cannot stat" in output:
                print("ERROR: '{}' doesn't exist.".format(file))
            elif "Not a directory" in output:
                print("ERROR: Cannot move '{file}'  to '{directory}'. "
                    "'{directory}' does not exist.".format(
                    file=file, directory=destination))
            elif "Permission denied" in output:
                print("ERROR: Can't move '{0}' to '{1}'. You do not "
                "have access rights to '{1}'".format(
                    file, destination))
            else:
                output = error.output.decode()
                print(output)
                raise
        else:
            print(
                result.decode('utf-8').strip())
        finally:
            pass

def copy_files(files: list, destination: str):
    _process_files(files,destination,"cp")

def move_files(files: list, destination: str):
    _process_files(files,destination,"mv")

def delete_files(files: list):
    _process_files(files,"","rm")

def git_merge(remote,branch):
    try:
        result = subprocess.check_output(
            args = ["git", "fetch", "-v", remote],
            stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as error:
        output = error.output.decode()
        if "does not appear to be a git repository" in output:
            print("ERROR: '{remote}' is not a valid repository.".format(remote=remote))
        else:
            print(output)
    else:
        print(result.decode('utf-8').strip())
        try:
            string = remote + "/" + branch
            merge = subprocess.check_output(
                args = ["git", "merge", string],
                stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as error:
            output = error.output.decode()
            print(output)
        else:
            print(result.decode().strip())
