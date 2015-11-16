"""
This is module provides various functions for operating on files

Functions:
    process_files: Copy or move files to a specified destination or delete file(s).
    expand: Expands a given string to produce files list to process.
    git_fetch: Fetches the latest file changes from the git remote or bookmark.
    git_merge: Merges the latest file changes from the git remote with the local branch.
"""

import subprocess
import glob


def process_files(files: list, destination: str, function: str):
    """
    Move, copy files to a given destination or delete file(s).

    Args:
        files: List of file(s) to copy.
        destination: String specifying the destination to move or copy files.
        function: Identified whether to move (mv), copy (cp) or delete (rm) files.
    """
    for file in files:
        try:
            if function == 'cp':
                flags = '-vp'
            elif function == 'mv' or function == 'rm':
                flags = '-v'
            else:
                flags = ''
            args = [function, flags, file]
            if function != 'rm':
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
            print(result.decode().strip())
        finally:
            pass

def expand(function: str, files: str, destination: str):
    """
    Expands given string to produce files list to process.

    Args:
        files: File or string with %, ?, or * to be expanded
        destination: String specifying the destination to move or copy files.
        function: Identified whether to move (mv), copy (cp) or delete (rm) files.
    """
    if files.find('%') > -1 or files.find('?') > -1 or files.find('*') > -1:
        files = glob.glob(files)
    process_files(files,destination,function)

# Git add functionality
def git_add(folder,message):
    """
    Add the files to be committed.

    Args:
        folder: Folder path to add to commit.
        message: Message to include with the update.
    """
    try:
        file_add = subprocess.check_output(
            args = ["git", "add", folder],
            stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as error:
        file_add_output = error.output.decode()
        if "is outside repository" in file_add_output:
            print("ERROR: '{folder}' is not a valid file path".format(folder=folder))
        else:
            print(file_add_output)
    else:
        print(file_add.decode().strip())
        git_commit(message)

#Git commit functionality
def git_commit(message):
    """
    Commit the files to be pushed to pushed to origin.

    Args:
        message: Message to include with the update.
    """
    try:
        commit = subprocess.check_output(
            args = ["git", "commit", "-m", message],
            stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as error:
        commit_output = error.output.decode()
        print(commit_output)
    else:
        print(commit.decode().strip())

# Git merge functionality
def git_merge(remote,branch):
    """
    Merges the latest file changes from the git remote with the local branch.

    Args:
        remote: Repository from which the latest file updates were obtained.
        branch: Local store of files with which to merge the remote files.
    """
    try:
        string = remote + "/" + branch
        merge = subprocess.check_output(
            args = ["git", "merge", string],
            stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as error:
        merge_output = error.output.decode()
        if "not something we can merge" in merge_output:
            print("ERROR: '{branch}' is not a valid branch".format(branch=branch))
        else:
            print(merge_output)
    else:
        print(merge.decode().strip())

def git_fetch(remote,branch):
    """
    Fetches the latest file changes from the git remote or bookmark.

    Args:
        remote: Repository from which to obtain the latest file updates.
        branch: Local store of files with which to merge the remote files.
    """
    try:
        fetch = subprocess.check_output(
            args = ["git", "fetch", "-v", remote],
            stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as error:
        fetch_output = error.output.decode()
        if "does not appear to be a git repository" in fetch_output:
            print("ERROR: '{remote}' is not a valid repository.".format(remote=remote))
        else:
            print(fetch_output)
    else:
        print(fetch.decode('utf-8').strip())
        git_merge(remote,branch)

