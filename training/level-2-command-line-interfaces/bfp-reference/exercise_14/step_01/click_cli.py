"""
This module provides a CLI allows users to perform a variety of
file related tasks.
"""

import click

import file_ops


@click.group()
def cli():
    pass


@cli.command(name="copy", short_help="Copy files to a given destination.",
             help="Copy files to a given destination.  The last value given "
                  "is taken as the destination.")
@click.argument('filenames', nargs=-1, metavar="FILENAME", required=True)
@click.argument('destination')
def _copy_files(filenames, destination):
    file_ops.copy_files(filenames, destination)


@cli.command(name="move", short_help="Move files to a given destination.",
             help="Move files to a given destination.  The last value given "
                  "is taken as the destination.")
@click.argument('filenames', nargs=-1, metavar="FILENAME", required=True)
@click.argument('destination')
def _move_files(filenames, destination):
    file_ops.move_files(filenames, destination)


@cli.command(name="delete", short_help="Delete file(s).",
             help="Delete one or more files.")
@click.argument('filenames', nargs=-1, metavar="FILENAME", required=True)
def _delete_files(filenames, destination):
    file_ops.delete_files(filenames)


if __name__ == "__main__":
    cli()
