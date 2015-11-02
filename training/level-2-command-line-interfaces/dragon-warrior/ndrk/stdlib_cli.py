"""
This module provides a CLI that does something.
"""
import argparse

import file_ops


def _extract_arguments():
    parser = argparse.ArgumentParser(
        prog="ndrk_stdlib_cli",
        description="My own CLI",
        epilog="Use at your own risk!")

    parser.add_argument(
        "-f", "--filenames",
        dest="input_filenames",
        nargs="+",
        required=True,
        metavar="INPUT_FILENAMES",
        help="Name or names of file(s) to copy."
    )

    parser.add_argument(
        "-d", "--destination",
        dest="output_path",
        required=True,
        metavar="OUTPUT_PATH",
        help="Destination to copy files to."
    )

    return parser.parse_args()


if __name__ == '__main__':
    program_arguments = _extract_arguments()
    
    file_ops.copy_files(
        program_arguments.input_filenames,
        program_arguments.output_path
    )

