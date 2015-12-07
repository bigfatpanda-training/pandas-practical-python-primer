"""
This module provides a CLI that copies files.
"""

import argparse

import file_ops


def _extract_arguments():
    parser = argparse.ArgumentParser(
        prog="tmarsha1_stdlib_cli.py",
        description="A program to manage files.",
        epilog="an epilog description"
    )

    subcommand_parsers = parser.add_subparsers(
        title='Available Commands',
        description="The follow sub-commands are available:",
        dest="command"
    )
    subcommand_parsers.required = True

    # copy command
    copy_parser = subcommand_parsers.add_parser(
        name="copy",
        help="Copy files."
    )

    copy_parser.add_argument(
        "-f",
        "--filenames",
        nargs="+",
        metavar="filename",
        required=True,
        help="Name(s) of file(s) to copy"
    )
    copy_parser.add_argument(
        "-d",
        "--destination",
        required=True,
        help="Destination for file(s)"
    )

    # move command
    move_parser = subcommand_parsers.add_parser(
        name="move",
        help="Move files."
    )

    move_parser.add_argument(
        "-f",
        "--filenames",
        nargs="+",
        metavar="filename",
        required=True,
        help="Name(s) of file(s) to move"
    )
    move_parser.add_argument(
        "-d",
        "--destination",
        required=True,
        help="Destination for file(s)"
    )

    return parser.parse_args()

if __name__ == '__main__':
    command_arguments = _extract_arguments()

    if command_arguments.command == "copy":
        file_ops.copy_files(
            command_arguments.filenames,
            command_arguments.destination
        )
    elif  command_arguments.command == "move":
        file_ops.move_files(
            command_arguments.filenames,
            command_arguments.destination
        )
