"""
This module provides various functions for operating on files

Functions:
    copy_files: copy file(s) to a specific location.
    move_files: move file(s) to a specific location.
"""

import subprocess


class FolderNotFoundError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
        

class InsufficientRightsError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


def _process_files(
        command: str, 
        options: str, 
        file: str, 
        destination: str
) -> str:
    try:
        byte_result = subprocess.check_output(
            args=[command, options, file, destination],
            stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as file_error:
        message = file_error.output.decode()

        if "cannot stat" in message:
            raise FileNotFoundError()
        elif "Not a directory" in message:
            raise FolderNotFoundError(destination)
        elif "Permission" in message:
            raise InsufficientRightsError(destination)
        else:
            print(message)
    else:
        result = byte_result.decode()
        result = result. rstrip()
        return result    
    
    
def copy_files(file: str, destination: str):
    """
    Copy files to a given destination.

    Args:
        file: The file(s) to copy.
        destination: A string specifying the destination of the file(s).
    """

    try:
        result = _process_files("cp", "-vp", file, destination)
    except FileNotFoundError:
        print("ERROR: '{}' does not exist.".format(file))
    except FolderNotFoundError:
        print("ERROR: '{}' destination does not exist.".format(
            destination)
        )
    except InsufficientRightsError:
        print("ERROR: Insufficient rights to destination '{}'.".format(
            destination)
        )
    else:
        print(result)


def move_files(file: str, destination: str):
    """
    Move file(s) to a given destination.

    Args:
        file: The file(s) to move.
        destination: A string specifying the destination of the files.
    """

    try:
        result = _process_files("mv", "-v", file, destination)
    except FileNotFoundError:
        print("ERROR: '{}' does not exist.".format(file))
    except FolderNotFoundError:
        print(
            "ERROR: '{}' destination does not exist.".format(destination)
        )
    except InsufficientRightsError:
        print("ERROR: Insufficient rights to destination '{}'.".format(
            destination)
        )
    else:
        print(result)


def delete_files(file: str):
    """
    Deletes file(s).

    Args:
        file: The file(s) to delete.
    """

    try:
        byte_result = subprocess.check_output(
            args=['rm', '-v', file],
            stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as file_error:
        message = file_error.output.decode()

        if "cannot remove" in message:
            print("ERROR: '{}' does not exist.".format(file))
        else:
            print(message)
    else:
        result = byte_result.decode()
        result = result. rstrip()
        print(result)