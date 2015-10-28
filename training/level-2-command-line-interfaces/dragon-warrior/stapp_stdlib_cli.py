"""
Arparse example program
"""

# stapp 10/28/15

import argparse

#parser = argparse.ArgumentParser(prog="steve",usage="pray")

# parser.add_argument("filenames",nargs="+", metavar="FILENAME",
#                    help="Name of file(s) to copy")

parser = argparse.ArgumentParser(prog="CLIArgs", usage="filein [fileout]")
parser.add_argument("filein", nargs='?', default="stdin")
parser.add_argument("fileout", nargs='?', default="stdout")
parser.add_argument("junk", nargs='*')

args = parser.parse_args()

print(args.filein, args.fileout, args.junk)

# print(help(argparse.ArgumentParser))


