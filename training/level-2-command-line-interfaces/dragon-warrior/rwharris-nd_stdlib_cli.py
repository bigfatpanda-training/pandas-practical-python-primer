"""This module provides a CLI that..."""

import argparse

parser = argparse.ArgumentParser(
    prog="myprogram",
    description="This is a useful description.",
    epilog="This is epic."
)

parser.add_argument("filenames", nargs="+", metavar="FILENAME",
                    help="Name of file(s) to copy.")

parser.add_argument("-d", dest='destination', metavar="DESTINATION",
                    required=True, type=str, help="Destination file path.")

print(parser.parse_args())