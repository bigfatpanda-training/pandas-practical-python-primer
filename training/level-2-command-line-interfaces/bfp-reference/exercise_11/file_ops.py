"""
This modules provides various functions for operating on files.

Functions:
    copy_files: Copy file(s) to a specified location.
    move_files: Move file(s) to a specified location.
"""

import subprocess


def copy_files(files: list, destination: str):
    """
    Copy files to a given destination.

    Args:
        files: A list of files to copy.
        destination: A str specifying the destination for copied
            files.

    Raises:
        subprocess.CalledProcessError: When the call to `cp` results in
            a non-zero exit code and is not handled in this function.
    """

    for file in files:
        # Can you see the unnecessary processing in this block?
        # See past the new error handling keywords.
        try:
            operation_result = subprocess.check_output(
                args=['cp', '-vp', file, destination],
                stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as error:
            if "cannot stat" in error.output.decode():
                print("ERROR: '{}' doesn't exist.  Therefore, "
                      "it can't be moved.".format(file))
            elif "Not a directory" in error.output.decode():
                print(
                    "ERROR: Can't move '{file}' to '{directory}'. "
                    "'{directory}' doesn't exist.".format(
                        file=file, directory=destination))
            elif "Permission denied" in error.output.decode():
                print(
                    "ERROR: Can't move '{1}' to '{0}'. You do not "
                    "have access rights to '{0}' "
                    "or its parent(s).".format(destination, file))
            else:
                print("ERROR: {}".format(error.output.decode()))
        else:
            print(operation_result.decode().rstrip())


def move_files(files: list, destination: str):
    """
    Copy files to a given destination.

    Args:
        files: A list of files to copy.
        destination: A str specifying the destination for copied
            files.

     Raises:
        subprocess.CalledProcessError: When the call to `mv` results in
            a non-zero exit code and is not handled in this function.
    """

    for file in files:
        # Can you see the unnecessary processing in this block?
        # See past the new error handling keywords.
        try:
            operation_result = subprocess.check_output(
                args=['mv', '-v', file, destination],
                stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as error:
            # TODO: Fill this in.
            print("ERROR: {}".format(error.output.decode()))
        else:
            print(operation_result.decode().rstrip())
