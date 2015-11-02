"""This is module provides various functions for operating on files"""

import argparse

import subprocess


def copy_files(files: list, destination: str):
    """
    Copy files to a given destination,

    Args:
        files: List of files to copy.
        destination: String specifying the destination of copied files.
    """


    for file in files:
        result = subprocess.check_output(
            args=['cp', '-vp', file, destination],
            stderr=subprocess.STDOUT)
        print(
            result.decode('utf-8').strip())

def return_args():
    parser = argparse.ArgumentParser(
        prog="My Program",
        description="This is a useful description.",
        epilog="This is epic.")

    parser.add_argument("-f", "--filenames", nargs="+", metavar="FILENAME",
                        required=True, help="Name of file(s) to copy.")

    parser.add_argument("-d", "--destination", metavar="DESTINATION",
                    required=True, type=str, help="Destination file path.")

    return parser.parse_args()