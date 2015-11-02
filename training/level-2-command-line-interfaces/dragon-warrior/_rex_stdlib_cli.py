"""
This module provides a CLI that.....
"""

import argparse

import pprint

parser = argparse.ArgumentParser(
    prog="Kewl application",
    description="Does things",
    epilog="Thanks for using the program"
)
parser.add_argument("filenmes",nargs="+",metavar="FILENAME",
                    help="Name of files")

parser.add_argument("destination",metavar="DESTNAME",
                    help="Name of destination")

args = parser.parse_args()

print('Args:')
pprint.pprint(args)

