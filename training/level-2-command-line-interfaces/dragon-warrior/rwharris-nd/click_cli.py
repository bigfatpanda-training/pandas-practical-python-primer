"""
This module provides a CLI that...

Functions:
    move: Move given file(s) to a specified destination.
    copy: Copy given file(s) to a specified destination.
    delete: Delete given file(s).
    glob: Copy(-c) or Move(-m) file(s) matching a quoted wildcard string (-f)
     to a specified destination (-d) or delete (-r) matching files.
    merge: Fetch the given remote and merge updates with the given branch.
"""

import click
import file_ops


@click.group()
def cli():
    """Move, copy files to a given destination or delete file(s)."""
    pass

@cli.command('move')
@click.argument('files', nargs=-1, type=click.Path())
@click.argument('destination', nargs=1, type=click.Path(exists=True))
def move(files,destination):
    """
    Move, copy files to a given destination or delete file(s).

    Args:
        files: List of file(s) to move.
        destination: String specifying the destination to move files.
    """
    click.echo(files)
    click.echo(destination)
    file_ops.process_files(files,destination,'mv')

@cli.command('copy')
@click.argument('files', nargs=-1, type=click.Path())
@click.argument('destination', nargs=1, type=click.Path(exists=True))
def copy(files,destination):
    """
    Move, copy files to a given destination or delete file(s).

    Args:
        files: List of file(s) to copy.
        destination: String specifying the destination to copy files.
    """
    click.echo(files)
    click.echo(destination)
    file_ops.process_files(files,destination,'cp')

@cli.command('delete')
@click.argument('files', nargs=-1, type=click.Path())
def delete(files):
    """
    Move, copy files to a given destination or delete file(s).

    Args:
        files: List of file(s) to delete.
    """
    click.echo(files)
    file_ops.process_files(files,'','rm')

@cli.command('glob')
@click.option('-c','function',flag_value='cp')
@click.option('-r','function',flag_value='rm')
@click.option('-m','function',flag_value='mv')
@click.option('-f','--files',nargs=1)
@click.option('-d','--destination',nargs=1,type=click.Path(exists=True),default='/')
def glob_expand(function,files,destination):
    """
    Copy(-c) or Move(-m) file(s) matching a quoted wildcard string (-f)
     to a specified destination (-d) or delete (-r) matching files.

    Options:
        -f or --files: Wildcard string to find matching files to process.
        -d or --destination: String specifying the destination to move or copy
                             files. Flag is not needed for delete(-r) option
        function:
            -c: Copy files matching given string to a specified destination.
            -r: Delete files matching given string.
            -m: Move files matching given string to a specified destination.
    """
    file_ops.expand(function,files,destination)

@cli.command('merge')
@click.argument('remote', nargs=1)
@click.argument('branch', nargs=1)
def merge(remote,branch):
    """
    Fetch the given remote and merge updates with the given branch.

    Args:
        remote: Repository from which to obtain the latest file updates.
        branch: Local store of files with which to merge the remote files.
    """
    file_ops.git_merge(remote,branch)

@cli.command('commit')
@click.argument('folder',nargs=1,type=click.Path())
@click.argument('message',nargs=1)
def commit(folder,message):
    """
    Add the given folder to be updated. Commit the change(s) to be pushed with
    the given message.

    Args:
        folder: Folder path to add to commit.
        message: Message to include with the update.
    """
    file_ops.git_add(folder,message)


if __name__ == '__main__':
    cli()