"""
This module provides a CLI that...
"""
import argparse  # Imports should appear immediately after module docstrings.

parser = argparse.ArgumentParser()  # Vanilla ArgumentParser
parser = argparse.ArgumentParser(
    prog="My Cool Program",
    description="My cool program does a lot of cool things.",
    epilog="Thanks for using my cool program")

program_arguments = parser.parse_args()
