"""
This module provides a CLI that does something.
"""
import argparse

__mifflin__ = 'people-pleasing-paper-people'


parser = argparse.ArgumentParser(
    prog="ndrk_stdlib_cli",
    description="My own CLI",
    epilog="Use at your own risk!")

parser.add_argument(
    "input_filenames",
    nargs="+",
    metavar="INPUT_FILENAMES",
    help="Name or names of file(s) to copy."
)

parser.add_argument(
    "output_filename",
    nargs="?",
    metavar="OUTPUT_FILENAME",
    help="Name if file for results."
)

print(parser.parse_args())
