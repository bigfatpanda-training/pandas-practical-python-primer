# Excerpt From: David Beazley and Brian K. Jones. “Python Cookbook.” iBooks.
"""
Hypothetical command-line tool for searching a collection of
files for one or more text patterns.
"""
import argparse
import subprocess


def process_user_input() -> argparse.Namespace:
    """
    Process input from the command line and return the results.

    Returns:
        argparse.Namespace: A dictionary-like object containing the
        results of parsing the command line input.
    """
    parser = argparse.ArgumentParser(description="This programs copies files.",
                                     epilog="This programs copies files in "
                                            "case you forgot.")

    parser.add_argument(dest='filenames', metavar='filename',
                        nargs='+', help="All the files to copy.")

    parser.add_argument('-d', '--destination', required=True,
                        dest='destination', help='Location to copy files to.')

    return parser.parse_args()


def copy_files(files: list, destination: str):
    """
    Copy files to a given destination.
    """


if __name__ == "__main__":
    cli_arguments = process_user_input()
    print(cli_arguments)