"""
This module provides a CLI that...
"""
import argparse

import file_ops

parser = argparse.ArgumentParser(
    prog="My Cool Program",
    description="My cool program does a lot of cool things.",
    epilog="Thanks for using my cool program")

parser.add_argument("-f", "--filenames", nargs="+", metavar="FILENAME",
                    required=True, help="Names of files to copy.")

parser.add_argument('-d', '--destination', required=True,
                    help='Location to copy files to.')

program_arguments = parser.parse_args()
print(program_arguments)

file_ops.copy_files(
    files=program_arguments.filenames,
    destination=program_arguments.destination)


