"""
This module provides a CLI that.....
"""

import click

"""
This module provides a CLI allows users to perform a variety of
file related tasks.
"""

import file_ops

import pprint

import glob

@click.group()
def cli():
    pass

@cli.command(name="git_upstream", help="git merge upstream files")
#@click.option('--filename', '-f',  nargs=1, prompt='Enter <git> file name',
#                metavar='FILENAME', help='File name to git')
def _git_upstream():
    file_ops.git_upstream()


@cli.command(name="git_push", help="git merge upstream files")
@click.option('--destination', '-d' ,nargs=1, prompt='Enter destination path',
                metavar='DESTINATION', help='Destination for file copy')
@click.option('--message', '-m' ,nargs=1, prompt='Message for commit',
                metavar='MESSAGE', help='Message for commit')
def _git_push(destination:str, message:str):
    destination.rstrip('/')
    s = destination + '/*.*'
    msg = '-m"'+message+'"'
    filelist = glob.glob(s)
    file_ops.git_push(files = filelist, msg=msg)


@cli.command(name="copy", help="Copy files to a given destination.")
@click.option('--filename', '-f', nargs=1, prompt='Enter <copy> file name',
               metavar='FILENAME', help='File name to copy')
@click.option('--destination', '-d' ,nargs=1, prompt='Enter destination path',
                metavar='DESTINATION', help='Destination for file copy')
def _copy_files(filename,destination):
    print('HERE')
    filelist = glob.glob(filename)
    file_ops.copy_files(
        files = filelist,
        destination=destination)

@cli.command(name="move", help="Move files to a given destination.")
@click.option('--filename', '-f',  nargs=1, prompt='Enter <move> file name',
                metavar='FILENAME', help='File name to move')
@click.option('--destination', '-d' ,nargs=1, prompt='Enter destination path',
                metavar='DESTINATION', help='Destination for file move')
def _move_files(filename,destination):
    filelist = glob.glob(filename)
    file_ops.move_files(
        files = filelist,
        destination=destination)

@cli.command(name="delete", help="Delete files to a given destination.")
@click.option('--filename', '-f',  nargs=1, prompt='Enter <delete> file name',
                metavar='FILENAME', help='File name to delete')
def _delete_files(filename):
    filelist = glob.glob(filename)
    file_ops.delete_files(
        files = filelist)


if __name__ == '__main__':
    cli()
