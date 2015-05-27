"""
Insert docstring here.
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

    First attempt to copy the file while maintaining current permissions.
    If this fails, it attempt to copy without maintaining permissions.

    """

    for file in files:
        operation_result = subprocess.check_output(
            ['cp', '-vp', file, destination],
            stderr=subprocess.STDOUT)

        print(operation_result.decode('utf-8'))


if __name__ == "__main__":
    cli_arguments = process_user_input()
    copy_files(cli_arguments.filenames, cli_arguments.destination)