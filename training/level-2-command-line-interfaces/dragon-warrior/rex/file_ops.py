"""This module provides various functions for operating on file."""

import subprocess


def copy_files(files:list,destination:str):
    """
    Copy files to a given destination

    Args:
        files: for copying
        destination: specifies dest
    """
    for file in files:
        operation_result = subprocess.check_output(
            args = ['cp','-vp',file, destination],
            stderr=subprocess.STDOUT)
        print(
            operation_result.decode('UTF-8').rstrip('\n'))
