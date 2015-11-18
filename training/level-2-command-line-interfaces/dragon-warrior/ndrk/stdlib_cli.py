"""
This module provides a CLI that copies files.
"""
import argparse

import file_ops


def _extract_arguments():
    parser = argparse.ArgumentParser(
        prog="File Utils",
        description="This CLI allows operations on files.",
        epilog="Use at your own risk!")

    subcommand_parsers = parser.add_subparsers(
        title="Available Commands",
        description="The following sub-commands are available:",
        dest="command")
    subcommand_parsers.required = True

    # Copy Command Subparser
    copy_parser = subcommand_parsers.add_parser(
        name="copy",
        help="Copy files.")

    copy_parser.add_argument(
        "-f", "--filenames",
        dest="input_filenames",
        nargs="+",
        required=True,
        metavar="INPUT_FILENAMES",
        help="Name or names of file(s) to copy."
    )

    copy_parser.add_argument(
        "-d", "--destination",
        dest="output_path",
        required=True,
        metavar="OUTPUT_PATH",
        help="Destination to copy files to."
    )

    # Move Command Subparser
    move_parser = subcommand_parsers.add_parser(
        name="move",
        help="Move files.")

    move_parser.add_argument(
        "-f", "--filenames",
        dest="input_filenames",
        nargs="+",
        required=True,
        metavar="INPUT_FILENAMES",
        help="Name or names of file(s) to move."
    )

    move_parser.add_argument(
        "-d", "--destination",
        dest="output_path",
        required=True,
        metavar="OUTPUT_PATH",
        help="Destination to move files to."
    )

    # Copy Command Subparser
    copy_parser = subcommand_parsers.add_parser(
        name="rename",
        help="rename file.")

    copy_parser.add_argument(
        "-f", "--filename",
        dest="input_filename",
        required=True,
        metavar="INPUT_FILENAME",
        help="Name of file to rename."
    )

    copy_parser.add_argument(
        "-d", "--destination",
        dest="output_path",
        required=True,
        metavar="OUTPUT_PATH",
        help="New name for file."
    )

    return parser.parse_args()


if __name__ == '__main__':
    program_arguments = _extract_arguments()

    if program_arguments.command == 'copy':
        file_ops.copy_files(
            program_arguments.input_filenames,
            program_arguments.output_path
        )
    elif program_arguments.command == 'move':
        file_ops.move_files(
            program_arguments.input_filenames,
            program_arguments.output_path
        )
    elif program_arguments.command == "rename":
        file_ops.rename_file(
            program_arguments.input_filename,
            program_arguments.output_path
        )
        pass
