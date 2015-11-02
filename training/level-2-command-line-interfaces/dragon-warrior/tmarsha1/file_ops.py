"""This module provides various functions for operating on files"""

import subprocess


def copy_files(files: list, destination: str):
    """
    Copy files to a given destination.

    Args:
        files: A list of files to copy.
        destination: A string specifying the destination of the files.
    """

    for file in files:
        byteresult = subprocess.check_output(
            args=['cp', '-vp', file, destination],
            stderr=subprocess.STDOUT)
        result = byteresult.decode()
        result = result. rstrip()
        print(result)