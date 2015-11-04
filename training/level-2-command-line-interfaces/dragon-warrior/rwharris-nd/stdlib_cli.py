"""This module provides a CLI that..."""

import argparse

import file_ops


def process_user_input() -> argparse.Namespace:
    """
    Process input from the command line and return the results.

    Returns:
        A argparse.Namespace object containing the
        results of parsing the command line input.
    """


    parser = argparse.ArgumentParser(
        prog="My Program",
        description="This is a useful description.",
        epilog="This is epic.")


    subcommand_parser = parser.add_subparsers(
        prog="Available Commands",
        description="The following sub-commands are available:",
        dest="command")
    subcommand_parser.required = True

    # Copy Command Subparser
    copy_parser = subcommand_parser.add_parser(name='copy', help='Copy files.')

    copy_parser.add_argument(
        "-f", "--filenames", nargs="+", metavar="FILENAME",
        required=True, help="Name of file(s) to copy.")

    copy_parser.add_argument(
        "-d", "--destination", metavar="DESTINATION",
        required=True, type=str, help="Destination file path.")

    # Move Command Subparser
    move_parser = subcommand_parser.add_parser(name='move', help="Move files.")

    move_parser.add_argument(
        "-f," "--filenames", narg="+", metavar="FILENAME",
        required=True, help="Names of files to move.")

    move_parser.add_argument(
        '-d', '--destination', required=True,
        help='Location to move files to.')

    return parser.parse_args()


if __name__ == '__main__':

    program_arguments = parser.parse_args()

    file_ops.copy_files(
        program_arguments.filenames,
     program_arguments.destination)

# print(program_arguments)