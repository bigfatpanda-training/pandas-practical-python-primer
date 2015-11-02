"""This module provides various functions for operating on files."""

import subprocess


def copy_files(files: list, destination: str):
    """
    Copy files to a given destination.

    Args:
        files: A list of files to copy.
        destination: A string specifying the destination to copy the files to.
    """

    for file in files:
        result = subprocess.check_output(
            args=['cp', '-vp', file, destination],
            stderr=subprocess.STDOUT
        )

        print(
            "Copying " + result.decode('utf-8').rstrip())
