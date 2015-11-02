"""
This module provides a CLI that...
"""

import argparse
import sys

parser = argparse.ArgumentParser(
    prog="My Cool Progam",
    description='Type some Junk.',
    epilog='Welcome to the Jungle')


parser.add_argument("filenames",nargs="+", metavar="FILENAME",
                    help="Name or names of file(s) to copy")
parser.add_argument('copyto', nargs='?',
                    type=argparse.FileType('w'), default=sys.stdout)


print(parser.parse_args())
