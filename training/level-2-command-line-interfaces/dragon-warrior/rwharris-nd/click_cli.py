"""This module provides a CLI that..."""

import click
import file_ops


@click.group()
def cli():
    pass

@cli.command('move')
@click.argument('files', nargs=-1, type=click.Path())
@click.argument('destination', nargs=1, type=click.Path(exists=True))
def _move_files(files,destination):
    click.echo(files)
    click.echo(destination)
    file_ops.move_files(files,destination)

@cli.command('copy')
@click.argument('files', nargs=-1, type=click.Path())
@click.argument('destination', nargs=1, type=click.Path(exists=True))
def copy(files,destination):
    click.echo(files)
    click.echo(destination)
    file_ops.copy_files(files,destination)

@cli.command('delete')
@click.argument('files', nargs=-1, type=click.Path())
def copy(files):
    click.echo(files)
    file_ops.delete_files(files)

@cli.command('merge')
@click.argument('remote', nargs=1)
@click.argument('branch', nargs=1)
def merge(remote,branch):
    file_ops.git_merge(remote,branch)


if __name__ == '__main__':
    cli()