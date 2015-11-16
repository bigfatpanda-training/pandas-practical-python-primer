"""
This module provides a CLI that.....
"""

import argparse

import pprint

import file_ops

def get_args():
    parser = argparse.ArgumentParser(
        prog="Kewl application",
        description="Does things",
        epilog="Thanks for using the program"
    )
    parser.add_argument("-f","--filenames",nargs="+",metavar="FILENAME",
                        required=True,
                        help="Name(s) of files")

    parser.add_argument("-d","--destination",required=True,
                        help="Name of destination")

    theargs = parser.parse_args()
    return theargs

if __name__ == '__main__':

    args = get_args()
#    pprint.pprint(args.filenames)
#    pprint.pprint(args.destination)

    file_ops.copy_files(
       files = args.filenames,
       destination=args.destination)

    pprint.pprint('Args:')
    pprint.pprint(args)

