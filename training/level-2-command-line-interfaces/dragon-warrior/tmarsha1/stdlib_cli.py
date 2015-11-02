"""
This module provides a CLI that is, as yet, undefined.
"""

import argparse

import file_ops


def _extract_arguments():
    parser = argparse.ArgumentParser(
        prog="tmarsha1_stdlib_cli.py",
        description="A brief description",
        epilog="an epilog description"
    )

    parser.add_argument("-f", "--filenames", nargs="+", metavar="filename",
                        required=True, help="Name(s) of file(s) to copy")
    parser.add_argument("-d", "--destination", required=True,
                        help="Destination for file(s)")

    return parser.parse_args()

if __name__ == '__main__':
    command_arguments = _extract_arguments()
    file_ops.copy_files(
        command_arguments.filenames, command_arguments.destination)
    # print(command_arguments)
