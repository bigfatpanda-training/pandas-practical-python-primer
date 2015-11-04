"""
This is module provides various functions for operating on files

Functions:
    copy_files: Copy file(s) to a specified location.
"""

import subprocess


def copy_files(files: list, destination: str):
    """
    Copy files to a given destination,

    Args:
        files: List of files to copy.
        destination: String specifying the destination of copied files.
    """


    for file in files:
        try:
            result = subprocess.check_output(
                args=['cp', '-vp', file, destination],
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
                print(output)
                raise
        else:
            print(
                result.decode('utf-8').strip())
        finally:
            pass

