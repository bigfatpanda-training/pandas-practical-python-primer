# Excerpt From: David Beazley and Brian K. Jones. “Python Cookbook.” iBooks.
"""
Hypothetical command-line tool for searching a collection of
files for one or more text patterns.
"""
import argparse
import subprocess

def copy_file(self):
        """
        Copy a file(s) from one location to another.

        First attempt to copy the file while maintaining current permissions.
        If this fails, it attempt to copy without maintaining permissions.

        """
        try:
            operation_result = subprocess.check_output(
                ['cp', '-vp', self.current_file,
                 self.program_arguments.dest_filename],
                stderr=subprocess.STDOUT)

        except subprocess.CalledProcessError:
            operation_result = subprocess.check_output(
                ['cp', '-v', self.current_file,
                 self.program_arguments.dest_filename],
                stderr=subprocess.STDOUT)

        print(operation_result)

parser = argparse.ArgumentParser(description="This programs copies files.",
                                 epilog="This programs copies files in "
                                        "case you forgot.")

parser.add_argument(dest='filenames', metavar='filename',
                    nargs='+', help="All the files to copy.")

parser.add_argument('-d', '--destination', required=True,
                    dest='destination', help='Location to copy files to.')

args = parser.parse_args()

# Output the collected arguments
print(args.filenames)
print(args.patterns)
print(args.verbose)
print(args.outfile)
print(args.speed)