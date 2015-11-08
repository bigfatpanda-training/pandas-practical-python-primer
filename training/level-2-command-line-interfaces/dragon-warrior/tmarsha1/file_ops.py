"""
This module provides various functions for operating on files

Functions:
    copy_files: copy file(s) to a specific location.
    move_files: move file(s) to a specific location.
"""

import subprocess


def copy_files(files: list, destination: str):
    """
    Copy files to a given destination.

    Args:
        files: A list of files to copy.
        destination: A string specifying the destination of the files.
    """

    for file in files:
        try:
            byte_result = subprocess.check_output(
                args=['cp', '-vp', file, destination],
                stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as file_error:
            message = file_error.output.decode()

            if "cannot stat" in message:
                print("ERROR: '{}' does not exist.".format(file))
            elif "failed to access" in message:
                print("ERROR: '{}' destination does not exist.".format(destination))
            elif "Permission" in message:
                print("ERROR: Insufficient rights to destination '{}'.".format(destination))
        else:
            result = byte_result.decode()
            result = result. rstrip()
            print(result)
        finally:
            pass


def move_files(files: list, destination: str):
    """
    Move files to a given destination.

    Args:
        files: A list of files to move.
        destination: A string specifying the destination of the files.
    """

    for file in files:
        try:
            byte_result = subprocess.check_output(
                args=['mv', '-v', file, destination],
                stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as file_error:
            message = file_error.output.decode()

            if "cannot stat" in message:
                print("ERROR: '{}' does not exist.".format(file))
            elif "failed to access" in message:
                print("ERROR: '{}' destination does not exist.".format(destination))
            elif "Permission" in message:
                print("ERROR: Insufficient rights to destination '{}'.".format(destination))
        else:
            result = byte_result.decode()
            result = result. rstrip()
            print(result)
        finally:
            pass


def delete_files(files: list):
    """
    Deletes files.

    Args:
        files: A list of files to delete.
    """

    for file in files:
        try:
            byte_result = subprocess.check_output(
                args=['rm', '-v', file],
                stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as file_error:
            message = file_error.output.decode()

            if "cannot remove" in message:
                print("ERROR: '{}' does not exist.".format(file))
        else:
            result = byte_result.decode()
            result = result. rstrip()
            print(result)
        finally:
            pass