"""
This module provides a CLI that copies files using the 
Click third-party library.
"""

import click
import file_ops


@click.group()
def file_cli():
    pass


@file_cli.command()
@click.argument('filename', nargs=-1)
@click.argument('destination')
def copy_positional(filename, destination):
    for file in filename:
        file_ops.copy_files(file, destination)


@file_cli.command()
@click.argument('filename', nargs=-1)
@click.argument('destination')
def move_positional(filename, destination):
    for file in filename:
        file_ops.move_files(file, destination)


@file_cli.command()
@click.argument('filename', nargs=-1)
def delete_positional(filename):
    for file in filename:
        file_ops.delete_files(file)


@file_cli.command()
@click.option('-f', '--filename', multiple=True, required=True)
@click.option('-d', '--destination', required=True)
def copy_keyword(filename, destination):
    for file in filename:
        file_ops.copy_files(file, destination)


@file_cli.command()
@click.option('-f', '--filename', multiple=True, required=True)
@click.option('-d', '--destination', required=True)
def move_keyword(filename, destination):
    for file in filename:
        file_ops.move_files(file, destination)


@file_cli.command()
@click.option('-f', '--filename', multiple=True, required=True)
def delete_keyword(filename):
    for file in filename:
        file_ops.delete_files(file)


if __name__ == '__main__':
    file_cli()
