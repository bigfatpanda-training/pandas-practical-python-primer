"""
This module provides a CLI that copies files using the 
Click third-party library.
"""

import click

import file_ops

# use click.argument and click.option
    
@click.group()
def file_cli():
    pass
        
        
@file_cli.command()
@click.argument('filename')
@click.argument('destination')
def copy_positional(filename, destination):
    file_ops.copy_files([filename], destination)
    
    
@file_cli.command()
@click.argument('filename')
@click.argument('destination')
def move_positional(filename, destination):
    file_ops.move_files([filename], destination)
    
    
@file_cli.command()
@click.argument('filename')
def delete_positional(filename):
    file_ops.delete_files([filename])
    
    
@file_cli.command()
@click.option('-f', '--filename', required=True)
@click.option('-d', '--destination', required=True)
def copy_keyword(filename, destination):
    file_ops.copy_files([filename], destination)
    

@file_cli.command()
@click.option('-f', '--filename', required=True)
@click.option('-d', '--destination', required=True)
def move_keyword(filename, destination):
    file_ops.move_files([filename], destination)

    
@file_cli.command()
@click.option('-f', '--filename', required=True)
def delete_keyword(filename, destination):
    file_ops.delete_files([filename], destination)

    
if __name__ == '__main__':
    file_cli()
    
