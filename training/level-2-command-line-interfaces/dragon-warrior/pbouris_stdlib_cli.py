"""
This module provides a CLI that...
"""

import argparse

parser = argparse.ArgumentParser(epilog="The epilog text message")

parser.add_argument("filenames", nargs="+", metavar="FILENAME",
                     help="Name or name(s) of file to copy")

parser.add_argument("destination", metavar="dest_of_files",
                     help="Name of destination to copy to copy files to")

# print(help(argparse.ArgumentParser))
parser.parse_args("FILENAME, dest_of_files")
