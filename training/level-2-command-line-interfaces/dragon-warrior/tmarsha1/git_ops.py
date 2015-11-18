"""
This module provides various functions for operating on Git

Functions:
    git_fetch: get files from a specific remote.
    git merge: move file(s) to a specific location.
"""

import subprocess


def git_fetch(remote: str):
    """
    Get files from a specific remote.

    Args:
        remote: A string specifying the remote host.
    """

    try:
        byte_result = subprocess.check_output(
            args=['git', 'fetch', remote],
            stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as git_error:
        message = git_error.output.decode()

        if "does not appear" in message:
           print("ERROR: '{}' is not a valid remote host.".format(remote))
        else:
            print(message)
    else:
        result = byte_result.decode()
        result = result. rstrip()
        print(result)


def git_merge(remote_branch: str):
    """
    Merge the remote branch into the current branch.

    Args:
        remote_branch: A string specifying the remote branch.
    """

    try:
        byte_result = subprocess.check_output(
            args=['git', 'merge', remote_branch],
            stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as git_error:
        message = git_error.output.decode()

        if "not something we can merge" in message:
            print("ERROR: '{}' is not a valid remote branch.".format(remote_branch))
        else:
            print(message)
    else:
        result = byte_result.decode()
        result = result. rstrip()
        print(result)
