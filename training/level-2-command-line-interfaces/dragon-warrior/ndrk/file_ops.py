"""
This module provides various functions for operating on files.

Functions:
    copy_files: Copy file(s) to a specified destination

"""

import shutil


def copy_files(files: list, destination: str):
    """
    Copy files to a given destination.

    Args:
        files: A list of files to copy.
        destination: A string specifying the destination to copy the files to.
    """

    for file in files:
        try:
            shutil.copy2(file, destination)
        except shutil.Error as error:
            print('Error: %s' % error)
        except FileNotFoundError as error:
            print('Error: %s' % error)
        except PermissionError as error:
            print('Error: %s' % error)
        except IsADirectoryError as error:
            print('Error: %s' % error)
        else:
            print("Copying " + file)
        finally:
            pass


def move_files(files: list, destination: str):
    """
    Move files to a given destination.

    Args:
        files: A list of files to move.
        destination: A string specifying the destination to move the files to.
    """

    for file in files:
        try:
            shutil.move(file, destination)
        except shutil.Error as error:
            print('Error: %s' % error)
        except FileNotFoundError as error:
            print('Error: %s' % error)
        except PermissionError as error:
            print('Error: %s' % error)
        except IsADirectoryError as error:
            print('Error: %s' % error)
        else:
            print("Moving " + file)
        finally:
            pass


def rename_file(file: str, destination: str):
    """
    Rename file.

    Args:
        file: A file to rename.
        destination: A string specifying the destination to rename the files to.
    """

    move_files([file], destination)
