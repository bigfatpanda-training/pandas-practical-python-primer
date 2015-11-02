"""
This module provides various functions for operating on files.

Functions:
    copy_files: Copy file(s) to a specified destination

"""

import subprocess


def copy_files(files: list, destination: str):
    """
    Copy files to a given destination.

    Args:
        files: A list of files to copy.
        destination: A string specifying the destination to copy the files to.
    """

    for file in files:
        try:
            result = subprocess.check_output(
                args=['cp', '-vp', file, destination],
                stderr=subprocess.STDOUT
            )

            print(
                "Copying " + result.decode('utf-8').strip())
        except subprocess.CalledProcessError as error:
            exception_msg = error.output.decode()

            if "cannot stat" in exception_msg:
                print("ERROR: '{}' doesn't exist.".format(file))
            elif "Not a directory" in exception_msg:
                print("ERROR: '{}' doesn't exist.".format(destination))
            elif "Permission denied" in exception_msg:
                print("ERROR: You don't have permission to '{}'.".format(destination))
            else:
                print(error.output.decode())
