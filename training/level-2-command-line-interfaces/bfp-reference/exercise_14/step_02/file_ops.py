"""
This modules provides various functions for operating on files.

Functions:
    copy_files: Copy file(s) to a specified location.
    move_files: Move file(s) to a specified location.
"""

import subprocess
import glob


def copy_files(filename: str, destination: str):
    """
    Copy file(s) to a given destination.

    Args:
        filename: A str indicating the file to copy.  If a wildcard is in
            the string, all matching files will be operated on.
        destination: A str specifying the destination for copied
            files.

    Raises:
        subprocess.CalledProcessError: When the call to `cp` results in
            a non-zero exit code and is not handled in this function.
    """

    for matched_file in glob.glob(filename):
        try:
            operation_result = subprocess.check_output(
                args=['cp', '-vp', matched_file, destination],
                stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as error:
            error_output = error.output.decode()
            if "cannot stat" in error_output:
                print("ERROR: '{}' doesn't exist.  Therefore, "
                      "it can't be moved.".format(filename))
            elif "Not a directory" in error_output:
                print(
                    "ERROR: Can't move '{file}' to '{directory}'. "
                    "'{directory}' doesn't exist.".format(
                        file=filename, directory=destination))
            elif "Permission denied" in error_output:
                print(
                    "ERROR: Can't move '{1}' to '{0}'. You do not "
                    "have access rights to '{0}' "
                    "or its parent(s).".format(destination, filename))
            else:
                print("ERROR: {}".format(error_output))
        else:
            print(operation_result.decode().rstrip())


def move_files(filename: str, destination: str):
    """
    Move file(s) to a given destination.

    Args:
        filename: A str indicating the file to move.  If a wildcard is in
            the string, all matching files will be operated on.
        destination: A str specifying the destination for moved files.

     Raises:
        subprocess.CalledProcessError: When the call to `mv` results in
            a non-zero exit code and is not handled in this function.
    """

    for matched_file in glob.glob(filename):
        try:
            operation_result = subprocess.check_output(
                args=['mv', '-v', matched_file, destination],
                stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as error:
            # TODO: Fill this in.
            print("ERROR: {}".format(error.output.decode()))
        else:
            print(operation_result.decode().rstrip())


def delete_files(filename: str):
    """
    Delete file(s).

    Args:
        filename: A str indicating the file to delete.  If a wildcard
            is in the string, all matching files will be operated on.

     Raises:
        subprocess.CalledProcessError: When the call to `mv` results in
            a non-zero exit code and is not handled in this function.
    """

    for matched_file in glob.glob(filename):
        try:
            operation_result = subprocess.check_output(
                args=['rm', '-v', matched_file],
                stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as error:
            # TODO: Fill this in.
            print("ERROR: {}".format(error.output.decode()))
        else:
            print(operation_result.decode().rstrip())
