"""
This module provides a CLI allows users to perform a variety of
file related tasks.
"""

import click


import file_ops

@click.group()
def cli():
    pass


@cli.command(name="copy", help="Copy files to a given destination.")
@click.option('-f', '--filename', metavar="FILENAME",
              required=True, help="File to copy. Wildcards supported.")
@click.option('-d', '--destination', metavar="DESTINATION",
              required=True, help="Destination for copied file.")
def _copy_files(filename, destination):
    file_ops.copy_files(**locals())
    
    
@cli.command(name="move", help="Move files to a given destination.")
@click.option('-f', '--filename', metavar="FILENAME",
              required=True, help="File to move. Wildcards supported.")
@click.option('-d', '--destination', metavar="DESTINATION",
              required=True, help="Destination for moved file(s).")
def _move_files(filename, destination):
    file_ops.move_files(**locals())
    
    
@cli.command(name="delete", help="Delete files to a given destination.")
@click.option('-f', '--filename', metavar="FILENAME",
              required=True, help="File to delete. Wildcards supported.")
@click.option('-d', '--destination', metavar="DESTINATION",
              required=True, help="Destination for deleted file(s).")
def _delete_files(filename, destination):
    file_ops.delete_files(**locals())


if __name__ == "__main__":
    cli()
