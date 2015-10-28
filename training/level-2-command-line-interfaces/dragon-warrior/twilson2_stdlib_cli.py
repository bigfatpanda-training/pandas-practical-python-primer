"""
CLI DocString Stub
"""

import argparse
import sys

parser = argparse.ArgumentParser(
    prog="TSW Arg Parser",
    description="Tim Wilsons Argument Parsing Routine",
    epilog="TSW END")

parser.add_argument("infile", nargs="+",
                    metavar="In File",
                    type=argparse.FileType('r'),
                    default=sys.stdin,
                    help="Name or names of file(s) to copy")

parser.add_argument("outfile", nargs="+",
                    metavar="Out File",
                    type=argparse.FileType('w'),
                    default=sys.stdout,
                    help="Name or names of file(s) to copy")

#parser.parse_args()
print(parser.parse_args())


#print(help(argparse.ArgumentParser))